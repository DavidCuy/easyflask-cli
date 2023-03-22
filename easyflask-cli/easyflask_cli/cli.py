from importlib.metadata import version as v

import typer
from dotenv import load_dotenv

from .src.project import project

load_dotenv()

app = typer.Typer()
app.add_typer(project.app, name='project')


@app.callback(invoke_without_command=True)
def callback_version(version: bool = False):
    """
    Prints the version of the CLI.
    """
    if version:
        typer.echo(f'version: {v("easyflask-cli")}')
