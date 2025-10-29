# TaskAPI (minimal) — API REST de tareas (en memoria) con Docker

## Objetivo
API REST simple para gestionar tareas. Buena separación por capas (domain, application, adapters), uso de patrones Service + Repository, y validaciones mínimas. Corre en Docker.

## Endpoints mínimos
- `GET /health` → `{ "status": "ok" }`
- `GET /tasks` → lista de tareas
- `POST /tasks` → crear tarea
  - Body JSON: `{ "title": "mi tarea", "status": "pending" }`
  - `status` debe ser `pending` o `done`
  - `title` obligatorio y no vacío

Opcional:
- `GET /tasks/{id}` → obtener tarea por id

## Requisitos
- Python 3.10+
- Docker 


## Instalar dependencias:

pip install -r requirements.txt

uvicorn main:app --reload


## Ejecutar localmente (sin Docker)
1. Crear y activar virtualenv:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   # source .venv/bin/activate  # macOS / Linux

## Ejecutar con Docker
docker build -t taskapi:latest .
docker run -p 8000:8000 taskapi:latest
http://localhost:8000/tasks



## IF YOU GET A RECURSIVE GUARD ERROR IT IS DUE TO MY PYTHON BEING OUTDATED AS SUCH I HAVE TO DOWNGRADE MY FASTAPI TO IT RUNS WITH MY PYTHON

