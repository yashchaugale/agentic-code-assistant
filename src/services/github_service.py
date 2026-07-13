from pathlib import Path
import subprocess


class GitHubService:

    def clone_repository(self, repo_url):

        repo_name = repo_url.rstrip("/").split("/")[-1]

        clone_path = Path("repositories") / repo_name

        if clone_path.exists():
            return clone_path

        clone_path.parent.mkdir(exist_ok=True)

        subprocess.run(
            [
                "git",
                "clone",
                repo_url,
                str(clone_path)
            ],
            check=True
        )

        return clone_path