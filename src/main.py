from llm import summarize_file
from agents.assistant import AssistantAgent
from tools.file_reader import read_file

agent = AssistantAgent()

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

    

    answer = agent.chat(user_input)

    print("\nAI:", answer)

    