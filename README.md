# 📘 Gestor de Tareas -- Proyecto Django

Aplicación web desarrollada con Django que permite a los usuarios
registrarse, iniciar sesión y gestionar sus tareas personales.\
Las tareas se almacenan en memoria, según los requisitos académicos del
proyecto.

## 📦 Características

-   Registro de usuarios\
-   Inicio y cierre de sesión\
-   Lista de tareas por usuario\
-   Crear, ver y eliminar tareas\
-   Interfaz responsiva con Bootstrap\
-   Tareas en memoria (no persisten al reiniciar)\
-   Vistas protegidas con login_required\
-   Separación estricta por usuario

## 🧩 Estructura del Proyecto

gestor_tareas/ │ manage.py │ ├── gestor_tareas/ │ ├── settings.py │ ├──
urls.py │ ├── wsgi.py │ └── asgi.py │ └── tareas/ ├── views.py ├──
urls.py ├── forms.py ├── templates/ │ ├── tareas/ │ └── registration/
└── apps.py

## 🚀 Instalación y Ejecución

### 1️⃣ Crear o ejecutar entorno virtual

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

-   Python 3.x\
-   Django 5.x\
-   HTML + Bootstrap 5\
-   Sistema de autenticación de Django\
-   Estructuras en memoria

## 📜 Licencia

Proyecto de libre uso con fines educativos.
