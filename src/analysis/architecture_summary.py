from collections import Counter
from pathlib import Path


class ArchitectureSummary:

    def generate(self, knowledge):

        source_files = knowledge.get("source_files", [])

        folders = Counter()

        classes = []

        functions = 0

        for file in source_files:

            folder = Path(file["path"]).parent.name

            if folder:
                folders[folder] += 1

            classes.extend(file.get("classes", []))

            functions += len(file.get("functions", []))

        return {
            "entry_point": knowledge.get("entry_point"),
            "layers": sorted(folders.keys()),
            "python_files": len(source_files),
            "classes": classes,
            "functions": functions
        }