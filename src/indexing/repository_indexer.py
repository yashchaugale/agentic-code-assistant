from executors.tool_executor import ToolExecutor


class RepositoryIndexer:

    def __init__(self):

        self.executor = ToolExecutor()

        self.index = {}

    def build(self):

        result = self.executor.execute(
            "scan_repository",
            "."
        )

        if not result["success"]:
            return result

        self.index = result["data"]

        return {
            "success": True,
            "data": self.index,
            "error": None
        }