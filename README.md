```markdown
# 🚀 FastAPI Crude Init

FastAPI backend skeleton generator based on Jinja2 templates.

The project creates a `backend/` directory in the current working directory and generates a complete application structure with support for `Async` or `Sync` mode.

---

## 📋 What it generates

Depending on the selected mode, the generator creates, among others:

- FastAPI application with entry point `api/main.py`
- User routing
- Service and repository layers
- Models and schemas (Pydantic)
- Security and JWT configuration
- Logging configuration
- Alembic migrations
- Tests for user endpoints

---

## 📦 Requirements

- Python `>= 3.13`
- `pip`

---

## 🔧 Installation

```bash
pip install .
```

If you're working in a development environment, you can also install the project in editable mode:

```bash
pip install -e .
```

---

## 🏃 Running the generator

After installation, the following command is available:

```bash
backend-gen
```

When executed, the program will ask for the database/execution layer type:

- `Async`
- `Sync`

Based on the selection, the generator filters the appropriate template files and creates the backend in the `backend/` directory.

---

## 📁 Project structure

```text
initBackend/
├── cli.py                 # Command line interface
├── generator.py           # Main generator logic
└── templates/
    └── backend/           # Jinja2 templates
        ├── apiAsync/      # Async version
        ├── apiSync/       # Sync version
        ├── config/        # Configuration
        ├── databases/     # Databases
        ├── log_config/    # Logging configuration
        └── migrations/    # Alembic migrations
            └── versions/
```

---

## ⚙️ How it works

1. `initBackend.cli` prompts the user for the mode of operation (`Async` or `Sync`).
2. `initBackend.generator` loads files from the `templates/backend` directory.
3. `.jinja2` templates are rendered with context indicating whether the `Async` variant was selected.
4. The output is placed in the `backend/` directory.

---

## 💻 Usage example

```bash
backend-gen
```

Then select one of the options:

```
Select mode (Async/Sync): Async
```

After generation, run the backend in your new project:

```bash
cd backend
pip install -r requirements.txt
uvicorn api.main:app --reload
```

---

## ⚠️ Notes

- The generator overwrites files in the target directory if they already exist.
- Some template names can be refined for a specific project, e.g., the application title in `api/main.py`.
- The generated project requires installing dependencies from the `requirements.txt` file.

---

## 📄 License

The project is distributed under the terms of the license included in the `LICENSE` file.

---
