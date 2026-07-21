from llm import ask_llm
from analysis.query_router import QueryRouter
from analysis.code_navigator import CodeNavigator


class RepositoryChat:

    def __init__(self):

        self.router = QueryRouter()
        self.navigator = CodeNavigator()

    def ask(self, knowledge, retrieved_chunks, question):
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
            
        code_context = ""

        for chunk in retrieved_chunks:
            code_context += f"""
        File: {chunk['file']}
        Lines: {chunk['start_line']} - {chunk['end_line']}

        {chunk['content']}

        ----------------------------------------
        """

        prompt = f"""
You are RepoMind, an expert software architect.

Repository Metadata:
Language: {knowledge.get("language")}
Framework: {knowledge.get("framework")}
Entry Point: {knowledge.get("entry_point")}

Important Files:
{knowledge.get("important_files")}

Relevant Code:
{code_context}

Instructions:
- Use the retrieved code as the primary source.
- Mention filenames when appropriate.
- If the answer isn't present in the code, say so.
- Never invent implementation details.

Question:
{question}
"""

        return ask_llm(
            [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )