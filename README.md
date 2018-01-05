# Users API 

Este es un test para la creación, migración y exposición de usuarios a través de servicios API y con una validación mínima de un Token.

De momento muestra el listado completo de usuarios registrados en la base de datos.

Se recomienda el uso de PostgreSQL como motor de Base de Datos.


# Desarrollado con

* Django==2.0.1
* django-import-export==0.6.1
* djangorestframework==3.7.7
* psycopg2==2.7.3.2


# Como Probar

Debes crear un usuario administrador y mediante un CSV desde el modulo de User (definido por Django), cargar tu CSV desde el boton import.

Para visualizar los usuarios desde el endpoint debes crear token para el usuario administrador con el cual podrás visualizar todos los usuarios disponibles en la Base de Datos.


# Servidor TEST

Para iniciar el servidor es necesario configurar los datos en el archivo users.settings.development como lo son USER, NAME, PASSWORD, HOST, PORT

Una vez configurados correras el servidor con el comando python manage.py runserver --settings=user.settings.development 

La URL de lectura del endpoint será http://127.0.0.1:8000/users/API/V1/list_all

# Usando CURL

Para usar Curl lo harías así

curl -X GET http://127.0.0.1:8000/users/API/V1/list_all -H 'Authorization: Token XXXXXXXXXXXXXXXXXXXXXX' 

donde las X serán el token que creaste