from indexing.repository_indexer import RepositoryIndexer
from knowledge.knowledge_store import KnowledgeStore
from services.github_service import GitHubService


class RepositoryService:

    def __init__(self):

        self.github = GitHubService()
        self.indexer = RepositoryIndexer()
        self.store = KnowledgeStore()

    def analyze_repository(self, repo_url):

        repo_path = self.github.clone_repository(repo_url)

        result = self.indexer.build(repo_path)

        if result["success"]:
            self.store.save(result["data"])

        return result