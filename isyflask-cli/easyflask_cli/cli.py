from importlib.metadata import version as v

import typer
from dotenv import load_dotenv

from .src.project import project
from .src.model import model

load_dotenv()

app = typer.Typer()
app.add_typer(project.app, name='project')
app.add_typer(model.app, name='model')


@app.callback(invoke_without_command=True)
def callback_version(version: bool = False):
    """
    Imprime la versión del CLI.
    """
    if version:
        typer.echo(f'version: {v("isyflask-cli")}')
