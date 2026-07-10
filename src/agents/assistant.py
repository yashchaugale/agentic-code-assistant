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
            
            file_content = tool(filename)

            if file_content is None:
                return f"❌ File '{filename}' not found."

            return summarize_file(file_content)

        # No tool required -> Normal Chat
        add_user_message(user_input)

        answer = ask_llm(get_conversation())

        add_ai_message(answer)

        return answer