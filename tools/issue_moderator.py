import os
import time
from pathlib import Path

from github import Github

if __name__ == '__main__':
    gh = Github(per_page=100, login_or_token=os.environ.get('GH_TOKEN'))
    repo = gh.get_repo("hykilpikonna/hyfetch")

    print("Running issue moderator...")

    while True:
        # Update blacklist every loop
        blacklist = {v for v in Path("blacklist_users.csv").read_text().split("\n") if v}
        iss = repo.get_issues(state='open')

        for i in iss:
            if i.user.login in blacklist:
                i.edit(title="[Redacted]", body="[Redacted by Content Moderation Bot]", state="closed")
                i.create_comment("Issue closed by bot for offensive content.")

                print(f"Closed {i.number}")

        time.sleep(5)
