from knowledge.knowledge_builder import KnowledgeBuilder
from indexing.repository_indexer import RepositoryIndexer
from knowledge.knowledge_store import KnowledgeStore
from services.github_service import GitHubService


class RepositoryService:

    def __init__(self):

        self.github = GitHubService()
        self.indexer = RepositoryIndexer()
        self.builder = KnowledgeBuilder()
        self.store = KnowledgeStore()

    def analyze_repository(self, repo_url):

        repo_path = self.github.clone_repository(repo_url)

        result = self.indexer.build(repo_path)

        if result["success"]:

            knowledge = self.builder.build(
                repo_path,
                result["data"]
            )

            self.store.save(knowledge)

        return {
            "success": result["success"],
            "repository_path": str(repo_path),
            "data": knowledge if result["success"] else result["data"],
            "error": result["error"]
        }