from llm import ask_llm
from analysis.query_router import QueryRouter
from analysis.code_navigator import CodeNavigator


class RepositoryChat:

    def __init__(self):

        self.router = QueryRouter()
        self.navigator = CodeNavigator()

    def ask(self, knowledge, question):
        route = self.router.route(question)

        if route == "class_lookup":

            symbol = (
                question.replace("Where is", "")
                .replace("where is", "")
                .replace("?", "")
                .strip()
            )

            path = self.navigator.where_is(
                knowledge,
                symbol
            )

            if path:
                return f"{symbol} is defined in:\n\n{path}"

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