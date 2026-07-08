from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)


def ask_llm(messages):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages
    )

    return response.choices[0].message.content


def summarize_file(file_content):

    prompt = f"""
You are an expert software engineer.

Summarize the following file.

File:

{file_content}
"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content