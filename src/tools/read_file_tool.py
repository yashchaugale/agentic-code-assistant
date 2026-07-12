from pathlib import Path

from tools.base_tool import BaseTool


class ReadFileTool(BaseTool):

    name = "read_file"

    description = "Reads the content of a file."

    def execute(self, file_path):

        path = Path(file_path)

        if not path.exists():

            return {
                "success": False,
                "data": None,
                "error": "File not found"
            }

        return {

            "success": True,

            "data": path.read_text(
                encoding="utf-8"
            ),

            "error": None
        }