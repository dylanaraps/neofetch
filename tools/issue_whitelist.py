import os
import time

from github import Github

if __name__ == '__main__':
    gh = Github(per_page=100, login_or_token=os.environ.get('GH_TOKEN'))

    repo = gh.get_repo("hykilpikonna/hyfetch")

    while True:
        iss = repo.get_issues(state='open')

        for i in iss:
            if i.user.login in ['Symbolic11']:
                i.edit(title="[Redacted]", body="[Redacted by Content Moderation Bot]", state="closed")
                i.create_comment("Issue closed by bot for offensive content.")

                print(f"Closed {i.number}")

        time.sleep(2)
