import questionary
from initBackend.generator import generate_project


answers = {
    "api": questionary.select(
        "API",
        choices=[
            "FastAPI",
            "Flask",
        ],
    ).ask(),

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