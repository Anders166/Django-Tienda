# Sistema de productos

Aplicación web desarrollada con Django para registrar y listar productos
almacenados en una base de datos. Cada producto guarda nombre, categoría,
precio y cantidad disponible.

## Tecnologías

- Python
- Django
- SQLite
- HTML y CSS
- Git y GitHub

## Ejecución

1. Crear y activar el entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```
2. Instalar Django:
   ```bash
   pip install django
   ```
3. Ejecutar las migraciones:
   ```bash
   python manage.py migrate
   ```
4. Ejecutar el servidor:
   ```bash
   python manage.py runserver
   ```
5. Abrir http://127.0.0.1:8000/ en el navegador.

## Funcionalidades

### Productos
- Listado de productos en una tabla (`/`) con nombre, categoría, precio, cantidad y estado.
- Mensaje cuando no hay productos registrados.
- Formulario para registrar productos (`/productos/nuevo/`).
- Campo `estado` (booleano): activo / inactivo.
- Validación de datos (precio mayor que 0, cantidad no negativa).
- Cada producto pertenece a una categoría (clave foránea).

### Categorías (CRUD completo)
- Listar: `/categorias/`
- Registrar: `/categorias/nueva/`
- Detallar (incluye sus productos): `/categorias/<id>/`
- Editar: `/categorias/<id>/editar/`
- Eliminar (con confirmación): `/categorias/<id>/eliminar/`
- No se puede eliminar una categoría que tenga productos asociados.

### General
- Navegación entre productos y categorías.
- Modelos registrados en el panel de administración (`/admin/`).
