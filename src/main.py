from agents.assistant import AssistantAgent

agent = AssistantAgent()

print("=" * 50)
print("🤖 Agentic Code Assistant")
print("Type 'exit' to quit.")
print("=" * 50)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    answer = agent.chat(user_input)

    print("\nAI:", answer)