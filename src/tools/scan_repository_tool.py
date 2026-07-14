from pathlib import Path

from tools.base_tool import BaseTool

class ScanRepositoryTool(BaseTool):

    name = "scan_repository"

    description = "Scans the repository."

    def execute(self, path="."):
        root = Path(path)

        files = []
        directories = []

        ignore = {
            ".git",
            "venv",
            "__pycache__",
            ".idea",
            ".vscode",
            ".DS_Store"
        }

        for item in root.rglob("*"):

            if any(part in ignore for part in item.parts):
                continue

            if item.is_file():
                files.append(str(item.relative_to(root)))

            elif item.is_dir():
                directories.append(str(item.relative_to(root)))

    # ------------------------
    # Detect Language
    # ------------------------

        python_count = sum(1 for f in files if f.endswith(".py"))
        cpp_count = sum(1 for f in files if f.endswith(".cpp"))
        c_count = sum(1 for f in files if f.endswith(".c"))
        js_count = sum(1 for f in files if f.endswith(".js"))
        ts_count = sum(1 for f in files if f.endswith(".ts"))
        go_count = sum(1 for f in files if f.endswith(".go"))
        java_count = sum(1 for f in files if f.endswith(".java"))

        counts = {
            "Python": python_count,
            "C++": cpp_count,
            "C": c_count,
            "JavaScript": js_count,
            "TypeScript": ts_count,
            "Go": go_count,
            "Java": java_count,
        }

        language = max(counts, key=counts.get)

        if counts[language] == 0:
            language = "Unknown"

    # ------------------------
    # Detect Framework
    # ------------------------

        framework = "Unknown"

        if "CMakeLists.txt" in files:
            framework = "CMake"

        elif "package.json" in files:
            framework = "Node.js"

        elif "requirements.txt" in files:
            framework = "Python"

        elif "manage.py" in files:
            framework = "Django"

        elif "Cargo.toml" in files:
            framework = "Rust"

        elif "go.mod" in files:
            framework = "Go Modules"

        elif "pom.xml" in files:
            framework = "Maven"

    # ------------------------
    # Important Files
    # ------------------------

        important = []

        important_candidates = [
            "README.md",
         "requirements.txt",
            "package.json",
            "Dockerfile",
            ".env.example",
            "main.py",
            "src/main.py"
        ]

        for file in important_candidates:
            if file in files:
                important.append(file)

    # ------------------------
    # Entry Point
    # ------------------------

        entry = None

        entry_candidates = [
            "src/main.cpp",
            "main.cpp",
            "src/main.c",
            "main.c",
            "src/main.py",
            "main.py",
            "app.py",
            "manage.py",
            "server.py",
            "src/main.go",
            "main.go"
        ]

        for candidate in entry_candidates:

            if candidate in files:
                entry = candidate
                break

        return {

            "success": True,

            "data": {

                "language": language,

                "framework": framework,

                "entry_point": entry,

                "important_files": important,

                "files": sorted(files),

                "directories": sorted(directories)

            },

            "error": None
        }
