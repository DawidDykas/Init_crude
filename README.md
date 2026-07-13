# FastApiCrude_Init

FastAPI backend skeleton generator based on Jinja2 templates.

The project creates a `backend/` directory in the current working directory and renders a complete application structure with support for `Async` or `Sync` mode.

## What it generates

Depending on the selected mode, the generator creates, among others:

- FastAPI application with entry point `api/main.py`
- User routing
- Service and repository layers
- Models and schemas
- Security and JWT configuration
- Logging configuration
- Alembic migrations
- Tests for user endpoints

## Requirements

- Python `>= 3.13`
- `pip`

## Installation

```bash
pip install .
```

If you're working in a development environment, you can also install the project in editable mode:

```bash
pip install -e .
```

## Running the generator

After installation, the following command is available:

```bash
backend-gen
```

When executed, the program will ask for the database/execution layer type:

- `Async`
- `Sync`

Based on the selection, the generator filters the appropriate template files and creates the backend in the `backend/` directory.

## Project structure

```text
initBackend/
├── cli.py
├── generator.py
└── templates/
    └── backend/
        ├── api/
        ├── config/
        ├── log_config/
        └── migrations/
```

## How it works

1. `initBackend.cli` prompts the user for the mode of operation.
2. `initBackend.generator` loads files from the `templates/backend` directory.
3. `.jinja2` templates are rendered with context indicating whether the `Async` variant was selected.
4. The output is placed in the `backend/` directory.

## Usage example

```bash
backend-gen
```

Then select one of the options and run the generated backend in your new project.

## Notes

- The generator overwrites files in the target directory if they already exist.
- Some template names can be refined for a specific project, e.g., the application title in `api/main.py`.

## License

The project is distributed under the terms of the license included in the `LICENSE` file.
