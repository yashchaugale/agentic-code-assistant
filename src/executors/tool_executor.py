from tools.registry import TOOLS


class ToolExecutor:

    def execute(self, tool_name, tool_input):

        tool = TOOLS.get(tool_name)

        if tool is None:

            return {
                "success": False,
                "data": None,
                "error": f"Unknown tool: {tool_name}"
            }

        return tool(tool_input)