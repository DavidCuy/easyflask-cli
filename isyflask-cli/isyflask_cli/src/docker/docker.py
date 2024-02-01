from ...globals import Constants
from ..utils.template_gen import generate_flask_template, read_project_config
from ..utils.strings import get_random_string
from ..utils.docker import save_compose_file, load_compose_file, clean_just_app_service, clean_entrypoint, delete_compose_file

import os
import sys
import json
import typer
from typing import cast
from click.types import Choice
from pathlib import Path
from shutil import which

app = typer.Typer()

@app.command('list')
def list_images(docker_compose_file: str = typer.Option(help='Ruta al archivo de docker-compose.yml', default='docker-compose.yml')):
    docker_file = load_compose_file(docker_compose_file)
    for service in cast(dict, docker_file['services']).keys():
        typer.echo(f'* {service}')
    return cast(dict, docker_file['services']).keys()

@app.command('up')
def up_container(
    service_name: str = typer.Option(..., help='Nombre del servicio a levantar con docker declarado en el archivo compose'),
    docker_compose_file: str = typer.Option(help='Ruta al archivo de docker-compose.yml', default='docker-compose.yml'),
    detached: bool = typer.Option(help='Indica si la imagen se ejecutará en background', default=True)):
    extra_params = ''
    if not service_name:
        raise Exception('service_name not valid')
    
    if service_name not in list_images(docker_compose_file=docker_compose_file):
        raise Exception('service not found in docker-compose file')

    if detached:
        extra_params += ' -d'
    os.system(f'docker-compose -f {docker_compose_file} up {service_name}{extra_params}')


@app.command('down')
def down_container(docker_compose_file: str = typer.Option(help='Ruta al archivo de docker-compose.yml', default='docker-compose.yml')):
    os.system(f'docker-compose -f {docker_compose_file} down')

@app.command('up-db')
def up_db_container(
    docker_compose_file: str = typer.Option(help='Ruta al archivo de docker-compose.yml', default='docker-compose.yml'),
    detached: bool = typer.Option(help='Indica si la imagen se ejecutará en background', default=True)):
    try:
        project_config = read_project_config()
    except:
        typer.echo('No se puedo leer la configuracion del proyecto', color=typer.colors.RED)
        raise typer.Abort()
    db_dialect = project_config['dbDialect']
    found_db = False
    service_db_name = ''
    for image in list_images(docker_compose_file=docker_compose_file):
        if str(db_dialect).lower() in str(image).lower():
            found_db = True
            service_db_name = image
            break
    if not found_db:
        raise Exception('Base de datos no encontrada en archivo docker-compose')
    
    up_container(service_name = service_db_name, docker_compose_file = docker_compose_file, detached = detached)


@app.command('doctor')    
def verify_docker():
    # Verify if docker and docker-compose installed and docker is up
    pass

@app.command('configure-remote')
def configure_remote():
    # Save config of docker remote repository
    pass

@app.command('build-app')
def docker_build():
    pass

@app.command('push-app')
def docker_push():
    pass
