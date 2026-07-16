from pathlib import Path


class SourceCodeIndexer:

    SUPPORTED_EXTENSIONS = {
        ".py": "Python",
        ".cpp": "C++",
        ".c": "C",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".java": "Java",
        ".go": "Go"
    }

    def build(self, repository_path):

        indexed_files = []

        root = Path(repository_path)

        for file in root.rglob("*"):

            if not file.is_file():
                continue

            extension = file.suffix

            if extension not in self.SUPPORTED_EXTENSIONS:
                continue

            indexed_files.append({

                "path": str(file.relative_to(root)),

                "language": self.SUPPORTED_EXTENSIONS[extension],

                "size": file.stat().st_size
            })

        return indexed_files