import os
from pathlib import Path
from cookiecutter.main import cookiecutter

import typer



app = typer.Typer()

@app.command('init')
def init_project():
    cookiecutter("https://github.com/DavidCuy/flask-pattern", directory="code", overwrite_if_exists=True)