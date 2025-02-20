# Setup

Para crear el entorno virtual e instalar los requerimientos:

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

### Variables de entorno

Remover '.example' de `.env.example`.

### Para levantar la aplicación

```bash
flask run
```

### Endpoints

- `http://127.0.0.1:5000/housing` (GET): Para obtener todos los registros
- `http://127.0.0.1:5000/housing/<id>` (GET): Para obtener el registro que coincida con el id
- `http://127.0.0.1:5000/housing` (POST): Para crear un nuevo registro. Es necesario pasar un body con la forma:
  ```json
  {
    "rooms": 8
  }
  ```
