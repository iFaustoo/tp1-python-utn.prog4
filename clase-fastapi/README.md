# API de usuarios y libros

API sencilla hecha con FastAPI para practicar ABM/CRUD. Los datos se guardan
en memoria: al reiniciar la aplicación se pierden. Los usuarios de ejemplo
se cargan al iniciar; los libros comienzan vacíos.

## Instalar y ejecutar

Desde esta carpeta (`clase-fastapi`), crear y activar un entorno virtual.
En PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m fastapi dev main.py
```

En macOS o Linux, usar:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows, si PowerShell no permite activar el entorno, también se puede
usar el Símbolo del sistema:

```bat
.venv\Scripts\activate.bat
```

En macOS o Linux, luego de activar el entorno:

```bash
pip install -r requirements.txt
python -m fastapi dev main.py
```

La API queda disponible en `http://127.0.0.1:8000`. Abrir
`http://127.0.0.1:8000/docs` para probar los endpoints en Swagger.

## Endpoints de usuarios

- `POST /user`: crear usuario. El cuerpo incluye `id`, `name` y, de forma
  opcional, `is_active` (por defecto `true`).
- `GET /user`: listar todos los usuarios.
- `GET /user?is_active=true` o `GET /user?is_active=false`: filtrar por
  estado.
- `PUT /user/{user_id}`: reemplazar nombre y estado de un usuario existente.
  El cuerpo requiere `name` e `is_active`.
- `DELETE /user/{id}`: eliminar un usuario.

## Endpoints de libros

Un libro tiene cinco campos: `id`, `title`, `author`, `genre` y
`publication_year`.

- `POST /books`: crear un libro; el cuerpo incluye los cinco campos.
- `GET /books`: listar libros.
- `GET /books?genre=novela`: listar libros filtrando por género (sin
  distinguir mayúsculas y minúsculas).
- `GET /books/{book_id}`: obtener un libro por id.
- `PUT /books/{book_id}`: reemplazar título, autor, género y año de
  publicación. El id se toma de la URL.
- `DELETE /books/{book_id}`: eliminar un libro.

Para ambos ABM, las rutas de modificación y eliminación responden con error
404 si el registro no existe. No se permiten ids repetidos al crear un
registro.
