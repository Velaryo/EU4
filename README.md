# Examen proyecto de la UNIDAD #04

## ¿Qué es Django?
Es un framework de alto nivel escrito en python y que permite el desarrollo de sitios web seguros y mantenibles.

## Patrón MVC
Django se basa en el patrón Modelo-Vista-Controlador (MVC).
- El modelo se encarga de gestionar la información y los datos de la aplicación.
- La vista se encarga de generar la interfaz de usuario y de mostrar la información al usuario.
- El controlador se encarga de gestionar las interacciones entre el usuario y la aplicación, así como de realizar las operaciones necesarias para responder a las solicitudes del usuario.

## Pasos iniciales

- Descarga del repositorio
```bash
git clone https://github.com/Velaryo/EU4.git nombre_carpeta
```

- Crear un entorno virtual en la carpeta con el repositorio descargado

```bash
virtualenv env
```

- Activar el entorno virtual

Windows

```bash
env\Scripts\activate
```

MacOS/Linux

```bash
source env/bin/activate
```

- Instalación de Django, módulos y/o librerías necesarias

```bash
pip install -r requirements.txt
```

## |-*settings.py*

```python
DATABASES = {
    'default': {
        'ENGINE': 'MOTOR de base de datos',
        'NAME': 'nombre de la DB',
        'PORT': 'puerto',
        'HOST': 'host {localhost} por defecto',
        'USER': 'usuario {root} por defecto',
        'PASSWORD': 'contraseña'
    }
}

```
#
## Autor:
- Huarca Gamero, Alvaro
#
