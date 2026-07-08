from llm import ask_llm, summarize_file
from chat import (
    add_user_message,
    add_ai_message,
    get_conversation
)
from tools.file_reader import read_file

print("=" * 50)
print("🤖 Agentic Code Assistant")
print("Type 'exit' to quit.")
print("Type 'read README.md' to summarize a file.")
print("=" * 50)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    # ---------- FILE TOOL ----------
    if user_input.startswith("read "):

        filename = user_input.replace("read ", "").strip()

        file_content = read_file(filename)

        if file_content is None:
            print("\n❌ File not found.")
            continue

        answer = summarize_file(file_content)

        print("\nAI:", answer)

        continue

    # ---------- NORMAL CHAT ----------

    add_user_message(user_input)

    answer = ask_llm(get_conversation())

    print("\nAI:", answer)

    add_ai_message(answer)