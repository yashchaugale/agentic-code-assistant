from indexing.repository_indexer import RepositoryIndexer
from knowledge.knowledge_store import KnowledgeStore


class RepositoryService:

    def __init__(self):

        self.indexer = RepositoryIndexer()
        self.store = KnowledgeStore()

    def analyze_repository(self):

        print("📂 Scanning repository...")

        result = self.indexer.build()

        if not result["success"]:
            return result
        
        self.store.save(result["data"])

        print("✅ Repository indexed.")

        return result