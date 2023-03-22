import os
from pathlib import Path
from cookiecutter.main import cookiecutter

import typer
from click.types import Choice

import random
import string

app = typer.Typer()

@app.command('init')
def init_project():
    project_name = typer.prompt("Nombre del proyecto")
    dbChoices = Choice(["sqlite", "mssql", "mysql", "postgresql"])
    dbDialect: Choice = typer.prompt("Elija su motor de base de datos", "sqlite", show_choices=True, type=dbChoices)
    
    config_override = {
        "directory_name": project_name,
        "develop_branch": "main",
        "dbDialect": dbDialect,
        "db_host": "",
        "db_user": "",
        "db_pass": "",
        "db_name": "",
        "db_schema": ""
    }
    
    if dbDialect != 'sqlite':
        config_override['db_host'] = typer.prompt("Host de la base de datos")
        config_override['db_name'] = typer.prompt("Nombre de la base de datos")
        config_override['db_user'] = typer.prompt("Usuario de la base de datos")
        autopassword = typer.confirm("Desea autogenerar la contraseña?")
        if autopassword is True:
            config_override['db_pass'] = get_random_string()
        else:
            config_override['db_pass'] = typer.prompt("Contraseña de la base de datos")
    if dbDialect == "postgresql":
        config_override['db_schema'] = typer.prompt("Nombre del esquema de base de datos")
    cookiecutter("https://github.com/DavidCuy/flask-pattern", directory="code", overwrite_if_exists=True, no_input=True, extra_context=config_override)

def get_random_string(length = 16):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))
    

