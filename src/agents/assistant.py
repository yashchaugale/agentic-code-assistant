from chat import (
    add_user_message,
    add_ai_message,
    get_conversation
)

from llm import ask_llm, summarize_file
from tools.tool_selector import decide_tool
from executors.tool_executor import ToolExecutor
from context.repository_context import build_repository_context

executor = ToolExecutor()


class AssistantAgent:

    def chat(self, user_input):

        # ------------------------------
        # Ask the LLM if a tool is needed
        # ------------------------------
        decision = decide_tool(user_input)

        print(f"\n[Decision] {decision}")

        # ------------------------------
        # Execute Tool
        # ------------------------------
        if decision.startswith("TOOL:"):

            try:
                _, tool_name, tool_input = decision.split(":", 2)

            except ValueError:
                return "❌ Invalid tool response."

            tool_result = executor.execute(
                tool_name,
                tool_input
            )

            if not tool_result["success"]:
                return f"❌ {tool_result['error']}"

            # ------------------------------
            # Handle read_file Tool
            # ------------------------------
            if tool_name == "read_file":

                return summarize_file(tool_result["data"])

            # ------------------------------
            # Handle scan_repository Tool
            # ------------------------------
            elif tool_name == "scan_repository":

                context = build_repository_context(tool_result)

                messages = [
                    {
                        "role": "system",
                        "content": f"""
You are RepoMind.

You are an expert software architect.

Use ONLY the repository context below to answer the user's question.

Repository Context:

{context}
"""
                    },
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]

                return ask_llm(messages)

            # ------------------------------
            # Unknown Tool
            # ------------------------------
            else:

                return f"❌ Tool '{tool_name}' is not supported."

        # ------------------------------
        # Normal Conversation
        # ------------------------------

        add_user_message(user_input)

        answer = ask_llm(get_conversation())

        add_ai_message(answer)

        return answer