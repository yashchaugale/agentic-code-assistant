from llm import ask_llm


def decide_tool(user_input):

    prompt = f"""
You are an AI agent.

Available tools:

1. read_file(filename)
   Use this whenever the user wants to:
   - summarize a file
   - read a file
   - explain a file
   - inspect a file

If a tool is needed reply ONLY like:

TOOL:read_file:<filename>

Examples:

User:
Summarize README.md

Answer:
TOOL:read_file:README.md

User:
Read config.py

Answer:
TOOL:read_file:config.py

If no tool is required reply:

NONE

User:
{user_input}
"""

    return ask_llm(
        [
            {
                "role": "user",
                "content": prompt
            }
        ]
    ).strip()