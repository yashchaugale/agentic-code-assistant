from pathlib import Path


def read_file(file_path):

    path = Path(file_path)

    if not path.exists():
        return None

    return path.read_text(encoding="utf-8")