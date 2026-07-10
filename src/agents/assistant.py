from chat import (
    add_user_message,
    add_ai_message,
    get_conversation
)

from llm import ask_llm, summarize_file
from tools.registry import TOOLS
from tools.tool_selector import decide_tool


class AssistantAgent:

    def chat(self, user_input):

        # Ask the LLM if a tool is required
        decision = decide_tool(user_input)

        print(f"\n[Decision] {decision}")

        # Execute Tool
        if decision.startswith("TOOL:"):

            try:
                _, tool_name, filename = decision.split(":", 2)

            except ValueError:
                return "❌ Invalid tool response."

            tool = TOOLS.get(tool_name)

            if tool is None:
                return f"❌ Unknown tool: {tool_name}"
            
            tool_result = tool(filename)

            if not tool_result["success"]:
                return f"❌ {tool_result['error']}"

            return summarize_file(tool_result["data"])

        # No tool required -> Normal Chat
        add_user_message(user_input)

        answer = ask_llm(get_conversation())

        add_ai_message(answer)

        return answer