# Start the server with:
#
# uvicorn tools.gh_moderator:app --reload --port 59523

import hashlib
import hmac
import json
import unicodedata
from datetime import datetime
from pathlib import Path

import openai
import toml
from fastapi import FastAPI, Request, Response
from github import Github
from hypy_utils import write, json_stringify
from hypy_utils.logging_utils import setup_logger
from openai.openai_object import OpenAIObject

from hyfetch.color_util import printc

log = setup_logger()


def read_config():
    with open(Path.home() / ".config/gh_moderator.toml") as f:
        return toml.load(f)


app = FastAPI()
config = read_config()
webhook_secret = bytes(config["webhook_secret"], "utf-8")

gh = Github(per_page=100, login_or_token=config["gh_token"])
me = gh.get_user()
repo = gh.get_repo(config["gh_repo"])
printc(f"&a[+] Logged in as {me.login}")

harm_classifier_url, harm_classifier_token = config["harm_classifier_url"], config["harm_classifier_token"]

script_path = Path(__file__).parent
supported_events = ["issue_comment", "issues", "pull_request", "pull_request_review_comment"]
ai_notice = f"If you think this is a false-positive, please contact the owner of this repo."

openai.organization = config['OpenAI']['org']
openai.api_key = config['OpenAI']['key']
openai_model = config['OpenAI']['model']


def get_content(event: str, obj: dict) -> str:
    # Get the content of the event
    match event:
        case "issue_comment" | "pull_request_review_comment":
            return obj["comment"]["body"]
        case "issues":
            return obj["issue"]["title"] + "\n\n" + obj["issue"]["body"]
        case "pull_request":
            return obj["pull_request"]["title"] + "\n\n" + obj["pull_request"]["body"]


def redact(event: str, obj: dict, id: str, reason: str):
    """
    Redact the event
    """
    printc(f"&c[!] Redacting {event} {id} for {reason}.")
    tail = f"\n\n> Reason: {reason}\n> {ai_notice}"
    redact_notice = f"[Redacted by [AI Content Moderator]({me.html_url})]{tail}"

    match event:
        case "issue_comment":
            # Redact the comment
            comment = repo.get_issue(obj["issue"]["number"]).get_comment(obj["comment"]["id"])
            comment.edit(body=redact_notice)

        case "pull_request_review_comment":
            # Redact the comment
            comment = repo.get_pull(obj["pull_request"]["number"]).get_review_comment(obj["comment"]["id"])
            comment.edit(body=redact_notice)

        case "issues" | "pull_request":
            # Close the issue
            iss = repo.get_issue(obj["issue"]["number"])
            iss.edit(title="[Redacted]", body=redact_notice, state="closed")
            iss.create_comment(f"Issue closed for potentially offensive content.{tail}")
            iss.lock("spam")


async def process_event(event: str, obj: dict, id: str):
    # Preliminary checks
    if event not in supported_events:
        printc(f"&7[-] Unknown event: {event}")
        return

    if obj['repository']['full_name'] != repo.full_name:
        printc(f"&7[-] Unknown repository: {obj['repository']['full_name']}")
        return

    blacklist_users = {v for v in (script_path / "blacklist_users.csv").read_text().split("\n") if v}
    actor = obj["sender"]["login"]
    if actor == me.login:
        printc(f"&7[-] Ignoring event by myself: {id} {event} by {actor}")
        return
    printc(f"&e[+] Received event: {id} {event} by {actor}")

    if actor in blacklist_users:
        redact(event, obj, "User is blacklisted", id)
        return

    # Normalize content
    content = unicodedata.normalize("NFKC", get_content(event, obj))

    # Ask OpenAI to predict if it's offensive
    res: OpenAIObject = openai.Moderation.create(content, openai_model).results[0]
    write(f"moderator-data/openai/{id}.json", json_stringify(res))
    if res.flagged:
        printc(f"\n&c[!] AI classified {event} {id} by {actor} as offensive !!!\n> Content: {content}\n\n")
        reason = " | ".join(f"{k} {res.category_scores.get(k) * 100:.0f}%" for k, v in res.categories.items() if v)
        redact(event, obj, id, f"Flagged by OpenAI : {reason}")
        return

    printc(f"&a[~] AI classified {event} {id} by {actor} as safe.")


@app.post("/")
async def handle_webhook(request: Request, response: Response):
    # Read headers
    event = request.headers.get("X-GitHub-Event")
    signature = request.headers.get("X-Hub-Signature")

    # Verify the signature
    body = await request.body()
    if not verify_signature(signature, body):
        response.status_code = 401
        return {"message": "Invalid signature"}

    # Parse the event body
    obj = json.loads(body.decode())

    # Log the request
    id = datetime.now().isoformat()
    write(f"moderator-data/webhook/{id}-{event}.json", json_stringify(obj, indent=4))

    await process_event(event, obj, id)

    return {"message": "OK"}


# Helper function to verify the signature
def verify_signature(signature: str, payload: bytes) -> bool:
    hash_type, signature = signature.split("=")
    digest = hmac.new(webhook_secret, msg=payload, digestmod=getattr(hashlib, hash_type)).hexdigest()
    return hmac.compare_digest(digest, signature)

