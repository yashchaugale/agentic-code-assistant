import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Create the Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

print("=" * 50)
print("🤖 Agentic Code Assistant")
print("Type 'exit' to quit.")
print("=" * 50)

while True:

    # Take user input
    user_input = input("\nYou: ")

    # Exit condition
    if user_input.lower() == "exit":
        print("\n👋 Goodbye!")
        break

    # Send request to Groq
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    # Print AI response
    print("\nAI:", response.choices[0].message.content)