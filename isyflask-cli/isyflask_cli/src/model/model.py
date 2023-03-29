from ...globals import load_config
from ..utils.folders import validate_path_not_exist
from ..utils.strings import camel_case
from ..utils.template_gen import add_code_to_module, add_file_to_module

import typer
from pathlib import Path

app = typer.Typer()

@app.command('new')
def new_model(name: str = typer.Option(..., help='Nombre del nuevo modelo.', prompt=True)):
    config = load_config()
    name = camel_case(name)
    models_folder_path = Path(config.project.folders.models)
    validate_path_not_exist(path=models_folder_path.joinpath(name), custom_error_message=f'Ya existe un modelo con nombre: {name}')

    template_model_path = Path(config.template.files.model)
    add_code_to_module(template_model_path, models_folder_path, name, {'model_name': name, 'model_name_lower': name.lower()})
    add_file_to_module(models_folder_path, name)
    
    service_template_path = Path(config.template.files.service)
    service_folder_path = Path(config.project.folders.services)
    add_code_to_module(service_template_path, service_folder_path, f"{name}Service", {'model_name': name})
    add_file_to_module(service_folder_path, f"{name}Service")
    
    controller_template_path = Path(config.template.files.controller)
    controller_folder_path = Path(config.project.folders.controllers)
    add_code_to_module(controller_template_path, controller_folder_path, f"{name}Controller", {})
    
    routes_template_path = Path(config.template.files.endpoint)
    routes_folder_path = Path(config.project.folders.endpoints)
    add_code_to_module(routes_template_path, routes_folder_path, f"{name}Router", {'model_name': name, 'model_name_lower': name.lower()})
    add_file_to_module(routes_folder_path, f"{name}Router", f"{name.lower()}_router")
    
    index_code = Path(config.project.folders.root).joinpath('__init__.py').read_text()
    index_code = index_code.replace("#replace this for add routes <-- NOT REMOVE THE COMMENT",
                       f"from .routes import {name.lower()}_router\n    #replace this for add routes <-- NOT REMOVE THE COMMENT")
    index_code = index_code.replace("#replace this for add blueprint <-- NOT REMOVE THE COMMENT",
                       f"app.register_blueprint({name.lower()}_router, url_prefix='/{name.lower()}')\n    #replace this for add blueprint <-- NOT REMOVE THE COMMENT")
    Path(config.project.folders.root).joinpath('__init__.py').write_text(index_code)

    typer.echo(f'{name} se agrego correctamente!', color=typer.colors.GREEN)

