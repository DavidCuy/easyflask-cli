# isyflask-cli

Un cli para manejar proyectos de API con flask.

> Se recomienda la instalación de docker para tener las últimas mejoras y actualizaciones. Algunas características sólo están con docker

Se recomienda utilizar el módulo *virtualenv* para los proyectos generados

Para _windows_:
````commandline
python -m venv venv
./venv/Scripts/activate
````

Para _macOS_ o _linux_:
````commandline
python -m venv venv
source ./venv/Scripts/activate
````

Posteriormente instale el cli

````commandline
pip install isyflask-cli
````

Para iniciar un proyecto ejecute el siguiente comando y responda las preguntas que salgan en el prompt:

````commandline
isyflask-cli project init
pip install -r requirements.txt
````

Cambie el directorio al generado en el paso anterior. Utilizando *Docker*, el proyecto se levanta utilizando el siguiente comando:

````commandline
docker-compose up
````

Si no utiliza docker, necesitará ejecutar lo siguiente:

_Windows CMD_:
```
python -m venv venv
source ./venv/Scripts/activate

set FLASK_APP=api
set FLASK_RUN_HOST=0.0.0.0
set FLASK_ENV=development 

flask db migrate
flask db upgrade
flask run --host=0.0.0.0
```

_Windows Powershell_:
```
python -m venv venv
source ./venv/Scripts/activate

$Env:FLASK_APP="api"
$Env:FLASK_RUN_HOST="0.0.0.0"
$Env:FLASK_ENV="development"

flask db migrate
flask db upgrade
flask run --host=0.0.0.0
```

_Mac_ o _Linux_:
```
python -m venv venv
source ./venv/bin/activate

export FLASK_APP=api
export FLASK_RUN_HOST=0.0.0.0
export FLASK_ENV=development

flask db migrate
flask db upgrade
flask run --host=0.0.0.0
```

## SQLAlchemy, Alembic y Blueprint

En esta herramienta, se mezcló el uso principal de estas librerías, por lo que están a su disposición todos los comandos y estructuras de datos para el desarrollo de nuevas features.

* [SQLAlchemy](https://www.sqlalchemy.org/)
* [Alembic](https://alembic.sqlalchemy.org/en/latest/)
* [Blueprint](https://flask.palletsprojects.com/en/1.1.x/blueprints/)

## Nota para los desarrolladores

Para el desarrollo local con poetry, solo hay que agregar las siguientes líneas a tu archivo `isyflask_project.toml`:

```
...
...
...
[tool.poetry.dependencies]
isyflask = { path = "<relative_path_to_project>/isyflask_cli", develop = true }
```

## Comandos
Para más información de los comandos, revisa la [Wiki](https://github.com/DavidCuy/easyflask-cli/wiki/)

