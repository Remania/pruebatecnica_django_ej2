# Proyecto CRUD API en Django

Este repositorio contiene una API CRUD desarrollada con el framework Django (utiliza SQLite como Base de Datos), similar al Repositorio Prueba Técnica Laravel Ejercicio 1. A continuación, se explican los pasos para clonar y ejecutar este proyecto localmente.

## Requisitos previos

Antes de ejecutar este proyecto, asegúrate de tener instalado lo siguiente en tu máquina:

- Python (versión 3.8 o superior)
- pip (gestor de paquetes de Python)
- Git

## Instrucciones para clonar y ejecutar el proyecto

### 1. Clonar el repositorio

Abre una terminal y ejecuta el siguiente comando para clonar el repositorio:

git clone https://github.com/Remania/pruebatecnica_django_ej2.git

### 2. Instalar dependencias

Una vez activado el entorno virtual, instala las dependencias del proyecto desde el archivo requirements.txt:

pip install -r requirements.txt

### 3. Configurar la Base de Datos
Este proyecto utiliza SQLite como base de datos predeterminada. Para crear la base de datos y las tablas necesarias, ejecuta las migraciones:

python manage.py migrate

### 4. Iniciar el servidor de desarrollo
Inicia el servidor de desarrollo de Django con el siguiente comando:

python manage.py runserver

### 5. Pruebas de la API
Puedes probar los endpoints de la API utilizando herramientas como Postman o la extensión ThunderClient de Visual Studio Code. A continuación, algunos ejemplos de los endpoints disponibles:

Obtener todos los productos: 
- GET /api/products
- URL: http://127.0.0.1:8000/api/products/

Obtener un producto por ID: 
- GET /api/products/{id}
- URL: http://127.0.0.1:8000/api/products/{id}

Crear un nuevo producto: 
- POST /api/products
- URL: http://127.0.0.1:8000/api/products/

Actualizar un producto existente: 
- PUT /api/products/{id}
- URL: http://127.0.0.1:8000/api/products/{id}

Eliminar un producto: 
- DELETE /api/products/{id}
- URL: http://127.0.0.1:8000/api/products/{id}