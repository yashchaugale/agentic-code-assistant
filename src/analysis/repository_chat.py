from pathlib import Path

from llm import ask_llm


class RepositoryChat:

    def ask(self, repository_path, metadata, question):

        readme = ""

        readme_path = Path(repository_path) / "README.md"

        if readme_path.exists():
            readme = readme_path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

        prompt = f"""
You are RepoMind.

You are helping a developer understand a GitHub repository.

Repository Metadata:

{metadata}

README:

{readme}

Question:

{question}

Answer clearly.

If the README does not contain enough information,
say that more source-code analysis is required.

Never invent facts.
"""

        return ask_llm(
            [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )