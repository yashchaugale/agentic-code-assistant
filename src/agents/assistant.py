from chat import (
    add_user_message,
    add_ai_message,
    get_conversation
)

from llm import ask_llm, summarize_file
from tools.file_reader import read_file


class AssistantAgent:

    def chat(self, user_input):

        # ---------------- FILE TOOL ----------------

        if user_input.startswith("read "):

            filename = user_input.replace("read ", "").strip()

            file_content = read_file(filename)

            if file_content is None:
                return "❌ File not found."

            return summarize_file(file_content)

        # ---------------- NORMAL CHAT ----------------

        add_user_message(user_input)

        answer = ask_llm(get_conversation())

        add_ai_message(answer)

        return answer