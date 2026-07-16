from services.repository_service import RepositoryService
from analysis.repository_chat import RepositoryChat


class RepoMindEngine:

    def __init__(self):

        self.repository_service = RepositoryService()
        self.chat = RepositoryChat()

        self.current_repository = None

    def analyze(self, github_url):

        result = self.repository_service.analyze_repository(
            github_url
        )

        if result["success"]:
            self.current_repository = result["data"]

        return result

    def ask(self, question):

        if self.current_repository is None:

            return {
                "success": False,
                "error": "No repository analyzed."
            }

        answer = self.chat.ask(
            self.current_repository,
            question
        )

        return {
            "success": True,
            "answer": answer
        }