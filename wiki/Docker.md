# Sub-Comando Docker

Este subcomando es utilizado para realizar tareas y afectaciones utilizando el comando de docker (debe estar instalado en el equipo).

```
.
└── isy
    └── docker
        └── list
        └── up
        └── down
        └── up-db
        └── configure-remote
        └── build-app
        └── push-app
```

## Docker commands

```isy docker list```
```
.
└── isy
    └── docker
        └── list
Arguments:
- docker-compose-file: Ruta al archivo de docker-compose.yml. Default=docker-compose.yml
```
Enlista todos los servicios que se encuentren configurados en el archivo docker-compose.yml

```isy docker up```
```
.
└── isy
    └── docker
        └── up

Arguments:
- service-name: Nombre del servicio a levantar con docker declarado en el archivo compose
- docker-compose-file: Ruta al archivo de docker-compose.yml. Default=docker-compose.yml
- detached: Indica si la imagen se ejecutará en background
```
Levanta un servicio en específico del archivo docker-compose.yml

```isy docker down```
```
.
└── isy
    └── docker
        └── down
Arguments:
- docker-compose-file: Ruta al archivo de docker-compose.yml. Default=docker-compose.yml
```
Finaliza todos los servicios que se encuentren en ejecución

```isy docker up-db```
```
.
└── isy
    └── docker
        └── up-db
Arguments:
- docker-compose-file: Ruta al archivo de docker-compose.yml. Default=docker-compose.yml
- detached: Indica si la imagen se ejecutará en background
```
Levanta el servicio de base de datos en el archivo especificado de docker-compose.yml

```isy docker configure-remote```
```
.
└── isy
    └── docker
        └── configure-remote
Arguments:
- pass-from-file: Indica si la contraseña viene desde un archivo docker-pass.secret
```
Configura las credenciales necesarias para poder realizar un inicio de sesión para un repositorio de contenedores remoto

```isy docker build-app```
```
.
└── isy
    └── docker
        └── build-app
```
Construye de manera local una imagen del contenedor de la aplicación de la api de docker.

```isy docker push-app```
```
.
└── isy
    └── docker
        └── push-app
Arguments:
- pass-from-file: Indica si la contraseña viene desde un archivo docker-pass.secret
```
Realiza la publicación de la imagen construida de docker de la api. En caso de no haber realizado la configuración de credenciales, las consultará, así como tambien contruirá la imagen
