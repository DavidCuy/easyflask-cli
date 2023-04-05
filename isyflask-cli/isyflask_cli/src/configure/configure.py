import os
import typer
from pathlib import Path
from configparser import ConfigParser

from ..utils.folders import validate_path_exist

app = typer.Typer()

@app.command('aws')
def configure_aws_credentials(profile: str = typer.Option("default", help='Perfil de aws.', prompt=False)):
    """
    Configura credenciales de aws para utilizar

    Args:
        profile (str, optional): Perfil local de aws. Defaults to typer.Option(..., help='Perfil de aws.', prompt=False, default='default').
    """
    home_path = os.path.expanduser('~')
    aws_cred_path = Path(os.path.join(home_path, '.aws', 'credentials'))
    try:
        validate_path_exist(path=aws_cred_path, custom_error_message=f'No existe configuracion local para aws')
    except Exception as e:
        typer.echo(f'No existe configuracion local para aws')
        exit(1)
    
    config = ConfigParser()
    config.read_string(aws_cred_path.read_text())
    aws_access_key_id = config.get(profile, 'aws_access_key_id')
    aws_secret_access_key = config.get(profile, 'aws_secret_access_key')
    
    confirm_credentials = typer.confirm(f"""Se ha detectado las siguientes contraseñas.
[{aws_access_key_id}]={''.rjust(10, '*')}{aws_secret_access_key[-4:]}
Desea continuar?""")
    if not confirm_credentials:
        aws_access_key_id = typer.prompt("AWS ACCESS KEY ID")
        aws_secret_access_key = typer.prompt("AWS SECRET ACCESS KEY")
        profile = typer.prompt("Nombre de perfil", default='default')
        
        if not config.has_section(profile):
            config.add_section(profile)
        config.set(profile, 'aws_access_key_id', aws_access_key_id)
        config.set(profile, 'aws_secret_access_key', aws_secret_access_key)
        
        with open(str(aws_cred_path), 'w') as configFile:
            config.write(configFile)
