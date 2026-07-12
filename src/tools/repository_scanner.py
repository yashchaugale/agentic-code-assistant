from pathlib import Path


def scan_repository(path="."):

    root = Path(path)

    files = []
    directories = []

    for item in root.iterdir():

        if item.is_file():
            files.append(item.name)

        elif item.is_dir():
            directories.append(item.name)

    return {
        "success": True,
        "data": {
            "files": sorted(files),
            "directories": sorted(directories)
        },
        "error": None
    }