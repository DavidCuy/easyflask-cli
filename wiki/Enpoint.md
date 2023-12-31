# Sub-Comando Endpoint

Este subcomando es utilizado el manejo los endpoints que exponen en la API.

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

```isy endpoint new```

Con este comando se creará un nuevo endpoint para el proyecto siguiendo el ruteo de blueprint, donde el el primer separador será tomado como el modelo del endpoint, si este modelo no existe en los archivos Router se creará el servicio, el controlador y el ruteo correspondiente.

Se creará los archivos correspondientes con el siguiente formato en las ubicaciones:

* api/app/Data/Services/_ModelName_ Service.py
* api/app/Controllers/_ModelName_ Controller.py
* api/routes/_ModelName_ Router.py

Así como moficar los siguientes archivos para el import y ruteo correspondiente:

* api/app/Data/Services/__ init__.py
* api/app/Controllers/__ init__.py
* api/routes/__ init__.py
* api/__ init__.py

Si el modelo ya existe, sólo se verán afectado los siguientes archivos.

* api/app/Controllers/_ModelName_ Controller.py
* api/routes/_ModelName_ Router.py

Teniendo encuenta lo anterior, la estructura de un endpoint quedaría como se muestra acontinuación:

``` [METHOD] <model>/<resto del ruteo> ```

## Ejemplos y afectaciones

```isy endpoint new --method=POST --path=car/verify-id```

El modelo para el ejemplo anterior sería *Car*. En caso de que no exista se generaría los siguientes archivos

```
.
├── /api/
│   ├── /app/
│   │   ├── /Controllers/
│   │   │   ├── __init__.py
│   │   │   └── CarController.py
│   │   ├── /Services/
│   │   │   ├── __init__.py
│   │   │   └── CarService.py
│   ├── /routes/
│   │   ├── __init__.py
│   │   └── CarRouter.py
```

En el archivo `api/app/Controllers/CarController.py` se agregaría la siguiente función:

```python
def post_car_verify-id(service: CarService):
    return build_response(HTTPStatusCode.OK.value, {"text": "Hello World!"})
```

Y en el archivo `api/routes/CarRouter.py`, se agregaría la siguiente línea:

```python
car_router.route('/verify-id', methods=['POST'], defaults={{'service': car_service}}) ({post_car_verify-id})
```

El usuario al final es libre de cambiar el nombre del controlador, y actualizarlo en el ruteo.
