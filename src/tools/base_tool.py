class BaseTool:

    name = ""

    description = ""

    def execute(self, tool_input):

        raise NotImplementedError(
            "Each tool must implement execute()."
        )