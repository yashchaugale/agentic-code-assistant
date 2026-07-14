import sys

from services.repository_service import RepositoryService
from ui.dashboard import show_dashboard


service = RepositoryService()


if len(sys.argv) == 3 and sys.argv[1] == "analyze":

    result = service.analyze_repository(sys.argv[2])

    if not result["success"]:
        print(result["error"])
        exit()

    data = result["data"]
    repo_path = result["repository_path"]

    repo_name = sys.argv[2].split("/")[-1]

    show_dashboard(data, repo_name)
    from analysis.repository_chat import RepositoryChat

    chat = RepositoryChat()

    print("\nAsk RepoMind anything about the repository.")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("Question: ")

        if question.lower() == "exit":
            break

        answer = chat.ask(
            repo_path,
            data,
            question
        )

        print("\nRepoMind:\n")
        print(answer)
        print()

else:

    print("Usage:")
    print("python src/main.py analyze <github-url>")