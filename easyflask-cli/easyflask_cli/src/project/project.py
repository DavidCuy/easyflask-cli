from ...constants import Constants
from ..utils.template_gen import generate_flask_template

import typer
from click.types import Choice

import random
import string

app = typer.Typer()

@app.command('init')
def init_project():
    """
    Genera un nuevo proyecto con template para flask
    """
    db_host = ""
    db_user = ""
    db_pass = ""
    db_name = ""
    db_schema = ""
    project_name = typer.prompt("Nombre del proyecto")
    dbChoices = Choice([
        Constants.SQLITE_ENGINE.value,
        Constants.SQLSERVER_ENGINE.value,
        Constants.MYSQL_ENGINE.value,
        Constants.POSTGRESQL_ENGINE.value
    ])
    dbDialect: Choice = typer.prompt("Elija su motor de base de datos", "sqlite", show_choices=True, type=dbChoices)
    
    if dbDialect != Constants.SQLITE_ENGINE.value:
        db_host = typer.prompt("Host de la base de datos")
        db_name = typer.prompt("Nombre de la base de datos")
        db_user = typer.prompt("Usuario de la base de datos")
        autopassword = typer.confirm("Desea autogenerar la contraseña?")
        if autopassword is True:
            db_pass = get_random_string()
        else:
            db_pass = typer.prompt("Contraseña de la base de datos")
    if dbDialect == "postgresql":
        db_schema = typer.prompt("Nombre del esquema de base de datos")
    generate_flask_template(project_name, dbDialect, db_host, db_user, db_pass, db_name, db_schema)

def get_random_string(length = 16):
    """
    Genera una cadena random de longitud variable

    Args:
        length (int, optional): Longitudd de la cadena. Defaults to 16.

    Returns:
        str: Cadena autogenerada
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))
    

