from jinja2 import Environment, FileSystemLoader
from pathlib import Path


# ======================================================
# PATHS
# ======================================================

workpath = Path(__file__).resolve().parent

template_path = workpath / "templates"

env = Environment(
    loader=FileSystemLoader(str(template_path))
)



# ======================================================
# FILTER FILES
# ======================================================

def filter_files(files, config):

    api = config["api"].lower()
    database = config["database"]

    print(api)


    # -----------------------------
    # API FILTER
    # -----------------------------
    if api == "flask":
        files = [
            file for file in files
            if "fastapi" not in str(file).lower()
        ]


    elif api == "fastapi":
        files = [
            file for file in files
            if "flask" not in str(file).lower()
        ]

    # -----------------------------
    # DATABASE FILTER
    # -----------------------------

    if database == "Async":
        files_ = [] 

        for file in files:
            if "async" in str(file).lower():
                files_.append(file)
                

        files = [
            file for file in files
            if "sync" not in str(file).lower()
        ]
        
        files = files + files_

    elif database == "Sync":

        files = [
            file for file in files
            if "async" not in str(file).lower()
        ]


    return files





# ======================================================
# GENERATOR
# ======================================================

def generate_project(config: dict):


    context = {
        "api": config["api"].lower(),

        "database": {
            "async": config["database"] == "Async"
        }
    }



    source_dir = template_path / "backend"

    output_dir = Path("backend")



    # ==================================================
    # 1. LOAD ALL FILES
    # ==================================================

    files = [
        file
        for file in source_dir.rglob("*")
        if file.is_file()
    ]


    print(
        f"Found files: {len(files)}"
    )



    # ==================================================
    # 2. FILTER
    # ==================================================

    files = filter_files(
        files,
        config
    )


    print(
        f"Selected files: {len(files)}"
    )



    # ==================================================
    # 3. RENDER
    # ==================================================

    for file_path in files:


        relative_path = file_path.relative_to(
            source_dir
        )



        # ----------------------------------------------
        # Remove .jinja2 extension
        # ----------------------------------------------

        if relative_path.suffix == ".jinja2":

            output_file = (
                output_dir /
                relative_path.with_suffix("")
            )

        else:

            output_file = (
                output_dir /
                relative_path
            )



        output_file.parent.mkdir(
            parents=True,
            exist_ok=True
        )



        # ----------------------------------------------
        # Load template
        # ----------------------------------------------

        template_name = str(
            file_path.relative_to(template_path)
        )


        template = env.get_template(
            template_name
        )



        # ----------------------------------------------
        # Render
        # ----------------------------------------------

        output = template.render(
            **context
        )



        # ----------------------------------------------
        # Write
        # ----------------------------------------------

        with open(
            output_file,
            "w",
            encoding="utf-8"
        ) as f:

            f.write(output)



        print(
            f"Generated: {output_file}"
        )