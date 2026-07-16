import sys

from services.repository_service import RepositoryService
from ui.dashboard import show_dashboard
from analysis.repository_chat import RepositoryChat
from engine.engine import RepoMindEngine


engine = RepoMindEngine()


if len(sys.argv) == 3 and sys.argv[1] == "analyze":

    result = engine.analyze(
        sys.argv[2]
    )

    if not result["success"]:
        print(result["error"])
        exit()

    data = result["data"]

    repo_name = sys.argv[2].split("/")[-1]

    show_dashboard(data, repo_name)

    print("\nAsk RepoMind anything about the repository.")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("Question: ")

        if question.lower() == "exit":
            break

        response = engine.ask(question)

        if not response["success"]:
            print(response["error"])
            continue

        answer = response["answer"]

        print("\n🧠 RepoMind:\n")
        print(answer)
        print()

else:

    print("Usage:")
    print("python src/main.py analyze <github-url>")