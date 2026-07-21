from pathlib import Path


class CodeChunker:

    def __init__(self, chunk_size=40):
        self.chunk_size = chunk_size

    def chunk_file(self, file_path):
        path = Path(file_path)

        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception:
            return []

        chunks = []

        for start in range(0, len(lines), self.chunk_size):

            end = min(start + self.chunk_size, len(lines))

            chunk = {
                "file": str(path),
                "start_line": start + 1,
                "end_line": end,
                "content": "".join(lines[start:end])
            }

            chunks.append(chunk)

        return chunks