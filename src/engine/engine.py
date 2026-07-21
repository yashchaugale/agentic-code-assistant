from services.repository_service import RepositoryService
from analysis.repository_chat import RepositoryChat
from analysis.code_review import CodeReview
from retrieval.chunker import CodeChunker
from retrieval.code_index import CodeIndex
from retrieval.retriever import Retriever
from pathlib import Path


class RepoMindEngine:

    def __init__(self):

        self.repository_service = RepositoryService()
        self.chat = RepositoryChat()
        self.code_review = CodeReview()
        self.chunker = CodeChunker()
        self.code_index = CodeIndex()
        self.retriever = Retriever(self.code_index)

        self.current_repository = None

    def analyze(self, github_url):

        result = self.repository_service.analyze_repository(
            github_url
        )

        if result["success"]:
            self.current_repository = result["data"]
            review = self.code_review.review(
            result["repository_path"],
            result["data"]
        )

        result["review"] = review

        repo_path = result["repository_path"]

        self.code_index.clear()

        for file in Path(repo_path).rglob("*"):

            if file.suffix not in [".py", ".js", ".ts", ".java", ".cpp", ".c", ".h"]:
                continue

            chunks = self.chunker.chunk_file(file)

            self.code_index.add_chunks(chunks)
        
        print(f"Total Chunks: {len(self.code_index.get_all_chunks())}")

        results = self.retriever.retrieve("main")

        print("\nRetrieved Chunks:\n")

        for chunk in results:
            print(chunk["file"])
            print(f"{chunk['start_line']} - {chunk['end_line']}")
            print("----------------------")

            

        return result

    def ask(self, question):

        if self.current_repository is None:

            return {
                "success": False,
                "error": "No repository analyzed."
            }

        retrieved_chunks = self.retriever.retrieve(
            question,
            top_k=3
        )
        print("=" * 60)
        print("RepoMind Retrieval")
        print(f"Question: {question}")
        print(f"Chunks Retrieved: {len(retrieved_chunks)}")
        print()

        for i, chunk in enumerate(retrieved_chunks, start=1):
            print(
                f"{i}. {chunk['file']} "
                f"({chunk['start_line']}-{chunk['end_line']})"
            )

        print("=" * 60)

        answer = self.chat.ask(
            self.current_repository,
            retrieved_chunks,
            question
        )

        return {
            "success": True,
            "answer": answer,
            "sources": [
                {
                    "file": chunk["file"],
                    "start_line": chunk["start_line"],
                    "end_line": chunk["end_line"]
                }
                for chunk in retrieved_chunks
            ]
        }