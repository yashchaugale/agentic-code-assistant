from pathlib import Path

from llm import summarize_file
from indexing.source_code_indexer import SourceCodeIndexer
from parsers.python_parser import PythonParser
from analysis.symbol_index import SymbolIndex


class KnowledgeBuilder:

    def __init__(self):

        self.indexer = SourceCodeIndexer()

        self.python_parser = PythonParser()
        self.symbol_index = SymbolIndex()

    def build(
        self,
        repository_path,
        metadata
    ):

        # Copy metadata
        knowledge = metadata.copy()

        # Store LLM summaries
        summaries = {}

        for file in metadata["important_files"]:

            file_path = Path(repository_path) / file

            if not file_path.exists():
                continue

            try:

                content = file_path.read_text(
                    encoding="utf-8",
                    errors="ignore"
                )

            except Exception:
                continue

            summary = summarize_file(content)

            if summary:
                summaries[file] = summary

        knowledge["summaries"] = summaries

        # Build source code index
        source_files = self.indexer.build(
            repository_path
        )

        parsed_files = []

        for file in source_files:

            if file["language"] == "Python":

                parsed = self.python_parser.parse(
                    Path(repository_path) / file["path"]
                )

                if parsed:

                    file["imports"] = parsed["imports"]

                    file["classes"] = parsed["classes"]

                    file["functions"] = parsed["functions"]

            parsed_files.append(file)

        knowledge["source_files"] = parsed_files

        knowledge["symbol_index"] = self.symbol_index.build(
            knowledge
        )

        return knowledge