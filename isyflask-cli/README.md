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

## Instalacion
Para instalar el CLI ejecute el siguiente comando

```
python -m pip install --upgrade pip
```

````commandline
pip install isyflask-cli
````

Para iniciar un proyecto ejecute el siguiente comando y responda las preguntas que salgan en el prompt:

````commandline
isyflask-cli project init
cd <folder project name>
pip install -r requirements.txt
````

Cambie el directorio al generado en el paso anterior. Utilizando *Docker*, el proyecto se levanta utilizando el siguiente comando:

````commandline
docker-compose up
````

Si no utiliza docker, necesitará ejecutar lo siguiente:

_Windows_:
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

_Mac_ o _Linux_:
```
python -m venv venv
./venv/Scripts/activate

export FLASK_APP=api
export FLASK_RUN_HOST=0.0.0.0
export FLASK_ENV=development

flask db migrate
flask db upgrade
flask run --host=0.0.0.0
```
