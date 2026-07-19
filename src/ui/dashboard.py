from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from analysis.repository_score import RepositoryScore
from analysis.repository_insights import RepositoryInsights
from analysis.reading_order import ReadingOrder
from analysis.architecture_summary import ArchitectureSummary


console = Console()


def show_dashboard(data, repo_name,review=None):

    score = RepositoryScore().calculate(data)
    insights = RepositoryInsights().analyze(data)

    table = Table(show_header=False)

    table.add_row("Repository", repo_name)
    table.add_row("Language", data["language"])
    table.add_row("Framework", data["framework"])
    table.add_row("Entry Point", str(data["entry_point"]))
    table.add_row("Repository Score", f"{score}/100")
    table.add_row("Files", str(len(data["files"])))
    table.add_row("Directories", str(len(data["directories"])))
    

    console.print()

    console.print(
        Panel.fit(
            table,
            title="🧠 RepoMind Analysis",
            border_style="cyan"
        )
    )

    console.print()
    stars = "★" * (score // 20)
    stars += "☆" * (5 - len(stars))

    console.print()
    console.print(f"[bold yellow]{stars}[/bold yellow]")
    

    console.print("[bold green]Important Files[/bold green]")

    for file in data["important_files"]:
        console.print(f" • {file}")
    
    console.print()

    console.print("[bold green]Strengths[/bold green]")

    for item in insights["strengths"]:
        console.print(f"✅ {item}")

    console.print()

    console.print("[bold yellow]Suggested Improvements[/bold yellow]")

    for item in insights["improvements"]:
        console.print(f"⚠ {item}")

    

    reading_order = ReadingOrder().generate(data)

    console.print()
    console.print("[bold cyan]📚 Recommended Reading Order[/bold cyan]")

    for i, item in enumerate(reading_order, start=1):

        console.print(
            f"{i}. [green]{item['file']}[/green]"
        )

        console.print(
            f"   {item['reason']}"
        )
    
    summary = ArchitectureSummary().generate(data)

    console.print()
    console.print("[bold magenta]🏗 Architecture Summary[/bold magenta]")

    console.print(f"Entry Point : {summary['entry_point']}")
    console.print(f"Python Files: {summary['python_files']}")
    console.print(f"Functions   : {summary['functions']}")
    console.print(f"Classes     : {len(summary['classes'])}")

    console.print("\nLayers:")

    for layer in summary["layers"]:
        console.print(f"  • {layer}")

    if review:

        console.print()
        console.print("[bold red]⚠ Code Review[/bold red]")

        for finding in review:

            severity = finding["severity"]

            if severity == "HIGH":
                color = "red"
            elif severity == "MEDIUM":
                color = "yellow"
            else:
                color = "cyan"

            console.print(
                f"[{color}][{severity}][/{color}] {finding['title']}"
            )

            console.print(
                f"    {finding['description']}"
            )

            console.print()
        


    