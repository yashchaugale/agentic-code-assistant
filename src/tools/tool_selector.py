from llm import ask_llm


def decide_tool(user_input):

    prompt = f"""
You are an AI routing assistant.

Your job is to decide whether a tool is needed.

Available tools:

1. read_file(filename)
Use this whenever the user wants to:
- read a file
- summarize a file
- explain a file
- inspect a file

Reply:
TOOL:read_file:<filename>

Examples:

User:
Summarize README.md

Assistant:
TOOL:read_file:README.md

User:
Read config.py

Assistant:
TOOL:read_file:config.py


2. scan_repository(path)

Use this whenever the user wants to:
- inspect a repository
- understand a project
- analyze a repository
- list files
- list folders
- show project structure
- explore the project
- what files are present
- what folders exist

Reply:

TOOL:scan_repository:.

Examples:

User:
Analyze this repository

Assistant:
TOOL:scan_repository:.

User:
Show me the project structure

Assistant:
TOOL:scan_repository:.

User:
List all files

Assistant:
TOOL:scan_repository:.


If NO tool is required, reply ONLY:

NONE


User Request:
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