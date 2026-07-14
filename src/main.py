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

else:

    print("Usage:")
    print("python src/main.py analyze <github-url>")