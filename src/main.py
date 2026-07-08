import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

conversation = []

print("=" * 50)
print("🤖 Agentic Code Assistant")
print("Type 'exit' to quit.")
print("=" * 50)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    # Save user message
    conversation.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation
    )

    ai_reply = response.choices[0].message.content

    print("\nAI:", ai_reply)

    # Save assistant reply
    conversation.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )