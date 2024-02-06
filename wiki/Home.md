# Comandos

El arbol general del los comandos se muestra acontinuación.

```
.
└── isy
    ├── project
    │   └── init
    │   └── configure
    │   └── install
    │   └── migrate
    │   └── run
    └── model
    │   └── new
    │   └── fromJson
    └── endpoint
    │   └── new
    └── docker
    |   └── list
    |   └── up
    |   └── down
    |   └── up-db
    |   └── configure-remote
    |   └── build-app
    |   └── push-app
```

Para ver la lista de comandos de su version, puede ejecutar el comando:

```
isy --help
```

Para verificar la versión del cli, se utiliza el comando `isy --version`

## Resumen de comandos

El subcomando *project* es utilizado para realizar tareas y afectaciones generales para el proyecto.

```
.
└── isy
    ├── project
    │   └── init
    │   └── configure
    │   └── install
    │   └── migrate
    │   └── run
```

El subcomando *model* es utilizado el manejo de los modelos para la base de datos del proyecto.

```
.
└── isy
    └── model
    │   └── new
    │   └── fromJson

Arguments:
- name: Nombre del nuevo modelo.
- tablename: Nombre de la tabla. Default='same-model-name'
```

El subcomando *endpoint* es utilizado el manejo los endpoints que exponen en la API.

```
.
└── isy
    └── endpoint
        └── new

Arguments:
- method: Metodo de la peticion. Valores permitidos [GET, POST, PUT, PATCH, DELETE].
- path: Path del endpoint
- model_name: Nombre de un modelo existente. Si no existe, crea el service, controller y router correspondiente. Default=''
```

El subcomando *docker* es utilizado el manejo del projecto utilizando docker, así como la sincronización remota.

```
.
└── isy
    └── docker
    |   └── list
    |   └── up
    |   └── down
    |   └── up-db
    |   └── configure-remote
    |   └── build-app
    |   └── push-app
```

