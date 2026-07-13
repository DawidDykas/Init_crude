import questionary
from initBackend.generator import generate_project


answers = {
    "database": questionary.select(
        "Database",
        choices=[
            "Async",
            "Sync",
        ],
    ).ask(),
}



def main() -> None: 
    generate_project(answers)