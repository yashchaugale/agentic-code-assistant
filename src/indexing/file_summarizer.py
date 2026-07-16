from pathlib import Path

from llm import summarize_file


class FileSummarizer:

    def summarize(self, file_path):

        path = Path(file_path)

        try:

            text = path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

        except Exception:

            return None

        # Skip huge files
        if len(text) > 12000:
            text = text[:12000]

        return summarize_file(text)