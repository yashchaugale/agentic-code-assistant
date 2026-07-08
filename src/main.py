from chat import (
    add_user_message,
    add_ai_message,
    get_conversation
)

from llm import ask_llm

print("=" * 50)
print("🤖 Agentic Code Assistant")
print("Type 'exit' to quit.")
print("=" * 50)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    add_user_message(user_input)

    answer = ask_llm(get_conversation())

    print("\nAI:", answer)

    add_ai_message(answer)