from pathlib import Path


def scan_repository(path="."):

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

    language = "Unknown"

    if any(f.endswith(".py") for f in files):
        language = "Python"

    elif any(f.endswith(".js") for f in files):
        language = "JavaScript"

    elif any(f.endswith(".ts") for f in files):
        language = "TypeScript"

    # ------------------------
    # Detect Framework
    # ------------------------

    framework = "Unknown"

    if "requirements.txt" in files:
        framework = "Python"

    if "package.json" in files:
        framework = "Node.js"

    if "manage.py" in files:
        framework = "Django"

    if "app.py" in files:
        framework = "Flask"

    if "main.py" in files or "src/main.py" in files:
        framework = "Python Application"

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

    for candidate in [
        "src/main.py",
        "main.py",
        "app.py",
        "manage.py"
    ]:

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