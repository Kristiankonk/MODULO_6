# 📘 Gestor de Tareas -- Proyecto Django

Aplicación web desarrollada con Django que permite a los usuarios
registrarse, iniciar sesión y gestionar sus tareas personales.\
Las tareas se almacenan en memoria, según los requisitos académicos del
proyecto.

## 📦 Características

-   Registro de usuarios
-   Inicio y cierre de sesión
-   Lista de tareas por usuario
-   Crear, ver y eliminar tareas
-   Interfaz responsiva con Bootstrap
-   Tareas en memoria (no persisten al reiniciar)
-   Vistas protegidas con login_required
-   Separación estricta por usuario

## 🧩 Estructura del Proyecto

gestor_tareas/
│   manage.py
│
├── gestor_tareas/          # Configuración global del proyecto
│   ├── settings.py         # Configuración general (apps, BD, seguridad, etc.)
│   ├── urls.py             # Enrutamiento principal
│   ├── wsgi.py
│   └── asgi.py
│
└── tareas/                 # Aplicación principal del sistema
    ├── views.py            # Lógica de vistas (CRUD en memoria y autenticación)
    ├── urls.py             # Rutas específicas de tareas
    ├── forms.py            # Formularios (registro y creación de tareas)
    ├── templates/          # Plantillas HTML con Bootstrap
    │     ├── tareas/       # Plantillas del módulo de tareas
    │     └── registrar/    # Plantillas de autenticación
    └── apps.py



## 🚀 Instalación y Ejecución

### 1️⃣ Crear entorno virtual

Windows:

    python -m venv proyectovenv
    proyectovenv\Scripts\activate

macOS / Linux:

    python3 -m venv venv
    source venv/bin/activate

### 2️⃣ Instalar dependencias

    pip install django

### 3️⃣ Ejecutar migraciones

    python manage.py makemigrations
    python manage.py migrate

### 4️⃣ Ejecutar el servidor

    python manage.py runserver

## 🛠 Tecnologías utilizadas

-   Python 3.13.5\
-   Django 5.2.8\
-   HTML + Bootstrap 5\
-   Sistema de autenticación de Django\
-   Estructuras en memoria

## 🚀  Ejecutar en modo producción (opcional)

En settings.py:

DEBUG = False
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


## Recolectar archivos estáticos:

python manage.py collectstatic


## 📜 Licencia

Proyecto de libre uso con fines educativos.
