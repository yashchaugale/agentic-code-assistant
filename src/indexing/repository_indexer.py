from executors.tool_executor import ToolExecutor


class RepositoryIndexer:

    def __init__(self):

        self.executor = ToolExecutor()

        self.index = {}

    def build(self, path="."):

        result = self.executor.execute(
            "scan_repository",
            path
        )

        if not result["success"]:
            return result

        self.index = result["data"]

        return {
            "success": True,
            "data": self.index,
            "error": None
        }