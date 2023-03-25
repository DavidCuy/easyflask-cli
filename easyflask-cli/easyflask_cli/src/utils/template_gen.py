from cookiecutter.main import cookiecutter
from ...constants import Constants

def generate_flask_template(project_name: str, db_dialect: str, db_host: str, db_user: str, db_pass: str, db_name: str, db_schema: str):
    config_override = {
        "directory_name": project_name,
        "develop_branch": "main",
        "dbDialect": db_dialect,
        "db_host": db_host,
        "db_user": db_user,
        "db_pass": db_pass,
        "db_name": db_name,
        "db_schema": db_schema
    }
    cookiecutter(
        Constants.FLASK_TEMPLATE.value,
        directory="code",
        overwrite_if_exists=True,
        no_input=True,
        extra_context=config_override
    )