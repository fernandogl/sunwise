# Introducción

**SunWise** 

El objetivo de este proyecto es tomar como entrada una o varias URL’s y generar nuevas URL’s acortadas haciendo uso de peticiones API REST. Todas las URL’s recibidas se guardan en una base de datos, esto permite posteriormente escribir una URL corta y redirigir hacia la URL larga u original.

Cuenta adicionalmente con una interfaz web para permitir la introducción mediante formularios de una URL o de multiples URL’s alojadas en un archivo JSON.

Este proyecto se realizó empleando Python 3.7, Django 2.1, DjangoRestFramework 3.3.1 y SQLite como base de datos.


# Procedimiento de instalación
Instalar [Python 3](https://www.python.org/downloads/)

Clonar este repositorio 
```
$ git clone https://github.com/fernandogl/sunwise.git
```

Crear y activar un ambiente virtual
```
$ cd sunwise
$ python3 -m venv venv
$ source venv/bin/activate
```

Instalar las dependencias de Python
```
$ cd src
$ pip install -r requirements.txt 
```

Ejecutar las migraciones de la base de datos
```
$ python manage.py migrate
```

Levantar un servidor local de desarrollo
```
$ python manage.py runserver
```

# Pruebas en ambiente local
Se debe acceder con un navegador a la ruta /urls/ en localhost
El puerto se indica al momento de levantar el servidor de prueba, por defecto será el 8000, quedando de la siguiente forma:

```
 http://localhost:8000/urls/
```

La interfaz web consiste en dos formularios en la parte superior, uno para introducir manualmente una URL y otro para introducir muchas URL’s mediante un archivo en formato JSON.

Debajo de los formularios se encuentran el listado de URL’s y el listado de Archivos, que nos permiten observar la información contenida en la base de datos.

En la ultima columna de cada listado, se cuenta con el botón “Borrar” que elimina un registro del listado de URL’s o un archivo y sus correspondientes URL’s que se encuentren asociadas a este.

Adicionalmente el listado de archivos permite también descargar en archivo JSON todas las URL’s con su correspondiente versión acortada de las rutas correspondientes a un archivos importado con anterioridad.

# Archivos JSON para pruebas
Dentro de la carpeta “json” se encuentran 2 archivos JSON que pueden ser utilizados para realizar pruebas de importar URL’s mediante la interfaz web y sirven de referencia si se quiere crear mas archivos de este tipo.

# Endpoints

**API**
```
/api/urls/
(GET, POST)

/api/urls/<url-id>/
(GET, DELETE)

/api/archivos/
(GET, POST)

/api/archivos/<archivo-id>/
(GET, DELETE)
```

**Interfaz Web**
```
  /urls/
	/<codigo>/
```
