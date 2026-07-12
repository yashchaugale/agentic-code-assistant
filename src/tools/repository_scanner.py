from pathlib import Path


def scan_repository(path="."):

    root = Path(path)

    files = []
    directories = []

    # Ignore unnecessary folders
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

    return {
        "success": True,
        "data": {
            "files": sorted(files),
            "directories": sorted(directories)
        },
        "error": None
    }