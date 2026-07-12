from agents.assistant import AssistantAgent
from services.repository_service import RepositoryService

agent = AssistantAgent()

print("=" * 50)
print("🤖 Agentic Code Assistant")
print("Type 'exit' to quit.")
print("=" * 50)
service = RepositoryService()

service.analyze_repository()

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    answer = agent.chat(user_input)

    print("\nAI:", answer)