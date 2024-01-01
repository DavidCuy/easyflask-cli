import pkg_resources
from cookiecutter.main import cookiecutter
from pathlib import Path
from ...globals import Constants, DRIVERS, SQL_PORTS_DEFAULT

def generate_flask_template(project_name: str, db_dialect: str, db_host: str, db_user: str, db_pass: str, db_name: str, docker_db: bool = False, repository_provider: str = None, pattern_version = 'latest'):
    """Descarga y configura el template de patron para flask

    Args:
        project_name (str): Nombre del proyecto
        db_dialect (str): Motor de base de datos
        db_host (str): Host de base de datos
        db_user (str): Usuario de base de datos
        db_pass (str): Contraseña de base de datos
        db_name (str): Nombre de base de datos
        docker_db (bool, optional): Crea la configuracion de docker para uso local. Defaults to False.
        repository_provider (str, optional): Genera los flujos de github actions para despliegue en un registro de contenedor. Defaults to None.
    """
    config_override = {
        "directory_name": project_name,
        "develop_branch": "main",
        "dbDialect": db_dialect,
        "db_host": db_host,
        "db_user": db_user,
        "db_pass": db_pass,
        "db_name": db_name,
        "_dbDriver": DRIVERS[db_dialect],
        "_db_port": SQL_PORTS_DEFAULT[db_dialect],
        "docker_local_db_enable": docker_db,
        "repostory_provider": repository_provider,
        "_db_extra_params": "?driver=FreeTDS" if db_dialect == Constants.SQLSERVER_ENGINE.value else ""
    }
    cookiecutter_kwargs = {
        "directory": "code",
        "overwrite_if_exists": True,
        "no_input": True,
        "extra_context": config_override
    }
    if pattern_version != 'latest':
        cookiecutter_kwargs.update({"checkout": pattern_version})
    cookiecutter(Constants.FLASK_TEMPLATE.value, **cookiecutter_kwargs)

def add_code_to_module(template_path: Path, module_path: Path, modelName: str, code_format_override: dict):
    module_code = template_path.read_text().format(**code_format_override)
    module_path.joinpath(f'{modelName}.py').write_text(module_code)

def add_file_to_module(module_path: Path, modelName: str, replace_import: str = None):
    module_text = module_path.joinpath('__init__.py').read_text()
    module_text += f"\nfrom .{modelName} import {modelName}" if replace_import is None else f"\nfrom .{modelName} import {replace_import}"
    module_path.joinpath('__init__.py').write_text(module_text)

