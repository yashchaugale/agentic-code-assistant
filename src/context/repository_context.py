def build_repository_context(scan_result):

    data = scan_result["data"]

    context = f"""
Repository Summary

Language:
{data["language"]}

Framework:
{data["framework"]}

Entry Point:
{data["entry_point"]}

Important Files:
{", ".join(data["important_files"])}

Top Level Directories:
{", ".join(data["directories"])}
"""

    return context.strip()