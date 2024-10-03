# Proyecto CRUD API en Django

- Este repositorio contiene una API CRUD desarrollada con el framework Django (utiliza SQLite como Base de Datos), similar al Repositorio Prueba Técnica Laravel Ejercicio 1. A continuación, se explican los pasos para clonar y ejecutar este proyecto localmente.
- Para poder visualizar la base de datos SQLite se recomienda instalar la extensión SQLite Viewer en Visual Studio Code

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

- python manage.py makemigrations
- python manage.py makemigrations products
- python manage.py migrate

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
- Datos de ejemplo: {
  "name": "Laptop Lenovo",
  "description": "Laptop de baja gama",
  "price": 700.50,
  "stock_quantity": 10
}

Actualizar un producto existente: 
- PUT /api/products/{id}
- URL: http://127.0.0.1:8000/api/products/{id}
- Datos de ejemplo: {
  "name": "Laptop Lenovo",
  "description": "Laptop de alta gama",
  "price": 1500,
  "stock_quantity": 70
}

Eliminar un producto: 
- DELETE /api/products/{id}
- URL: http://127.0.0.1:8000/api/products/{id}

## Resumen de como aprendí a usar el framework Django

- Primero, revisé la documentación oficial del framework en su página oficial.
- Luego, aprendí a utilizar el archivo settings.py para inicializar las apps creadas con los comandos de Django, en este caso, la app products.
- Hice uso de la clase ModelViewSet para tener las funciones CRUD inicializadas.
- Modifique las funciones para que muestren mensajes personalizados en cada request.
- Use la clase ModelSerializer para añadir las validaciones a la clase Product.
- Finalmente, añadí la urls correspondientes a urls.py para completar la API.

## Recursos utilizados

- Documentación oficial: https://www.djangoproject.com/
- Consultas específicas: https://stackoverflow.com/questions/tagged/django

## Desafíos presentados y su solución

- El desarrollo del proyecto no tuvo complicación alguna, solo tuve que aprender que era el concepto de "baterías incluidas" en Django. Que, en resumen, es la filosofía del framework de proporcionar un conjunto completo de herramientas y características listas para usar desde el inicio del desarrollo. Es decir, que ya viene con muchas librerías de uso común para todo tipo de proyectos, siendo una buena opción frente a frameworks más complejos como .NET, por ejemplo.
