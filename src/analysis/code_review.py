from pathlib import Path

MAX_FILE_LINES = 300
MAX_METHODS = 10
MAX_FUNCTION_LINES = 50


class CodeReview:

    def review(self, repository_path, knowledge):

        findings = []

        findings.extend(
            self.check_tests(repository_path)
        )
        findings.extend(
            self.check_large_files(
                repository_path,
                knowledge
            )
        )
        findings.extend(
            self.check_todos(
                repository_path,
                knowledge
            )
        )
        findings.extend(
            self.check_large_classes(knowledge)
        )

        findings.extend(
            self.check_long_functions(knowledge)
        )

        return findings

    def check_tests(self, repository_path):

        test_dirs = [
            "tests",
            "test"
        ]

        for folder in test_dirs:

            if (Path(repository_path) / folder).exists():

                return []

        return [
            {
                "severity": "HIGH",
                "title": "No Tests Found",
                "description": "Repository does not contain a test directory."
            }
        ]

    def check_large_files(
        self,
        repository_path,
        knowledge
    ):

        findings = []

        for file in knowledge.get("source_files", []):

            path = Path(repository_path) / file["path"]

            if not path.exists():
                continue

            try:

                line_count = len(
                    path.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    ).splitlines()
                )

            except Exception:
                continue

            if line_count > MAX_FILE_LINES:

                findings.append(
                    {
                        "severity": "MEDIUM",
                        "title": "Large File",
                        "description":
                            f"{file['path']} has {line_count} lines."
                    }
                )

        return findings
    
    def check_todos(
        self,
        repository_path,
        knowledge
    ):

        findings = []

        keywords = [
            "TODO",
            "FIXME",
            "HACK"
        ]

        for file in knowledge.get("source_files", []):

            path = Path(repository_path) / file["path"]

            if not path.exists():
                continue

            try:

                lines = path.read_text(
                    encoding="utf-8",
                    errors="ignore"
                ).splitlines()

            except Exception:
                continue

            for line_number, line in enumerate(lines, start=1):

                if any(keyword in line.upper() for keyword in keywords):

                    findings.append(
                        {
                            "severity": "LOW",
                            "title": "TODO / FIXME Found",
                            "description":
                                f"{file['path']}:{line_number} → {line.strip()}"
                        }
                    )

        return findings
    
    def check_large_classes(self, knowledge):

        findings = []

        for file in knowledge.get("source_files", []):

            for cls in file.get("classes", []):

                if len(cls["methods"]) > MAX_METHODS:

                    findings.append({
                        "severity": "MEDIUM",
                        "title": "Large Class",
                        "description": (
                            f'{cls["name"]} in {file["path"]} '
                            f'has {len(cls["methods"])} methods.'
                        )
                    })

        return findings
    
    def check_long_functions(self, knowledge):

        findings = []

        for file in knowledge.get("source_files", []):

            for function in file.get("functions", []):

                length = (
                    function["end_line"]
                    - function["start_line"]
                    + 1
                )

                if length > MAX_FUNCTION_LINES:

                    findings.append({
                        "severity": "MEDIUM",
                        "title": "Long Function",
                        "description": (
                            f'{function["name"]} in {file["path"]} '
                            f'is {length} lines long.'
                        )
                    })

        return findings