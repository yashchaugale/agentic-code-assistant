from chat import (
    add_user_message,
    add_ai_message,
    get_conversation
)

from llm import ask_llm


class AssistantAgent:

    def chat(self, user_input):

        add_user_message(user_input)

        answer = ask_llm(get_conversation())

        add_ai_message(answer)

        return answer