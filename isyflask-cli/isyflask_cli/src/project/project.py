from ...globals import Constants
from ..utils.template_gen import generate_flask_template
from ..utils.strings import get_random_string

import os
import json
import typer
from typing import cast
from click.types import Choice
from pathlib import Path

app = typer.Typer()

@app.command('init')
def init_project(pattern_version: str = typer.Option(help='Version del patron de flask.', default='latest')):
    """
    Genera un nuevo proyecto con template para flask
    """
    db_host = ""
    db_user = ""
    db_pass = ""
    db_name = ""
    docker_db_enable = False
    project_name = typer.prompt("Nombre del proyecto")
    
    dbChoices = Choice([
        Constants.SQLITE_ENGINE.value,
        Constants.SQLSERVER_ENGINE.value,
        Constants.MYSQL_ENGINE.value,
        Constants.POSTGRESQL_ENGINE.value
    ])
    dbDialect: Choice = typer.prompt("Elija su motor de base de datos", "sqlite", show_choices=True, type=dbChoices)
    
    if dbDialect != Constants.SQLITE_ENGINE.value:
        docker_db_enable = typer.confirm("¿Desea agregar configuracion de base de datos para desarrollo local en docker?")
        if docker_db_enable is False:
            db_host = typer.prompt("Host de la base de datos")
        else:
            db_host = Constants.LOCALHOST_DB_DOCKER.value
        db_name = typer.prompt("Nombre de la base de datos")
        
        if docker_db_enable is True and dbDialect == Constants.SQLSERVER_ENGINE.value:
            db_user = Constants.MSSQL_SA_USER.value
        else:
            db_user = typer.prompt("Usuario de la base de datos")
        
        autopassword = False
        if docker_db_enable is True:
            autopassword = typer.confirm("¿Desea autogenerar la contraseña?")
        if autopassword is True:
            db_pass = get_random_string()
        else:
            db_pass = typer.prompt("Contraseña de la base de datos")
    
    generate_flask_template(project_name, dbDialect, db_host, db_user, db_pass, db_name, docker_db_enable, pattern_version)

    local_project_dir = Path(os.getcwd()).joinpath(project_name).joinpath('.isy')
    if not local_project_dir.exists():
        os.mkdir(local_project_dir)
    
    with open(local_project_dir.joinpath('project.json'), 'w') as f:
        json.dump({
            "project_name": project_name,
            "dbDialect": dbDialect,
            "docker_db_enable": docker_db_enable,
            "pattern_version": pattern_version
        }, f)
    

@app.command('configure')
def read_config():
    local_project_dir = Path(os.getcwd()).joinpath('.isy')

    try:
        with open(local_project_dir.joinpath('project.json'), 'r') as f:
            project_config = cast(dict, json.load(f))
    except:
        typer.echo('No se puedo leer la configuracion del proyecto', color=typer.colors.RED)
        raise typer.Abort()
    
    output_str = ""
    for key in project_config.keys():
        output_str += f"{key} = {project_config[key]}\n"
    
    typer.echo(output_str)

