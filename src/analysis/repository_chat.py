from llm import ask_llm


class RepositoryChat:

    def ask(self, knowledge, question):

        prompt = f"""
You are RepoMind.

You are an AI software architect helping developers understand repositories.

Repository Knowledge:

{knowledge}

Question:

{question}

Rules:

1. Answer only using the repository knowledge.
2. If you don't know the answer, say:
   "More source-code analysis is required."
3. Never invent information.
4. Keep answers concise and technical.
"""

        return ask_llm(
            [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )