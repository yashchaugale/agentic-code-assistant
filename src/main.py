import sys

from services.repository_service import RepositoryService


service = RepositoryService()


if len(sys.argv) == 3 and sys.argv[1] == "analyze":

    result = service.analyze_repository(sys.argv[2])

    if not result["success"]:
        print(result["error"])
        exit()

    data = result["data"]

    print("\n🧠 RepoMind Analysis\n")

    print(f"Language: {data['language']}")
    print(f"Framework: {data['framework']}")
    print(f"Entry Point: {data['entry_point']}")

    print("\nImportant Files:")

    for file in data["important_files"]:
        print("-", file)

else:

    print("Usage:")
    print("python src/main.py analyze <github-url>")