# Introducción

**SunWise** 

El objetivo de este proyecto es tomar como entrada una o varias URL’s y generar nuevas URL’s acortadas haciendo uso de peticiones API REST. Todas las URL’s recibidas se guardan en una base de datos, esto permite posteriormente escribir una URL corta y redirigir hacia la URL larga u original.

Cuenta adicionalmente con una interfaz web para permitir la introducción mediante formularios de una URL o de multiples URL’s alojadas en un archivo JSON.

Este proyecto se realizó empleando Python 3.7, Django 2.1, DjangoRestFramework 3.3.1 y SQLite como base de datos.


# Procedimiento de instalación
Instalar Python 3

Clonar este repositorio 
```
https://github.com/fernandogl/sunwise.git
```
Crear y activar un ambiente virtual
```
cd sunwise
python3 -m venv venv
source venv/bin/activate
```

Instalar las dependencias de Python
```
cd src
pip install -r requirements.txt 
```
Ejecutar las migraciones de la base de datos
```
python manage.py migrate
```
Levantar un servidor local de desarrollo
```
python manage.py runserver
```
