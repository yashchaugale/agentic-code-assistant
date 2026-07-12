from indexing.repository_indexer import RepositoryIndexer


class RepositoryService:

    def __init__(self):

        self.indexer = RepositoryIndexer()

    def analyze_repository(self):

        print("📂 Scanning repository...")

        result = self.indexer.build()

        if not result["success"]:
            return result

        print("✅ Repository indexed.")

        return result