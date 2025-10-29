from fastapi import FastAPI, HTTPException
from app.application.services.task_service import TaskService
from app.adapters.persistence.memory_task_repository import MemoryTaskRepository
from app.domain.task import TaskCreate

app = FastAPI(title="Task API", version="1.0")


repo = MemoryTaskRepository()
service = TaskService(repo)


@app.get("/health")
def health_check():
    """
    Devuelve el estado del servicio.
    """
    return {"status": "ok", "message": "Task API is running!"}


@app.post("/tasks")
def create_task(task: TaskCreate):
    try:
        return service.create_task(task)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/tasks")
def list_tasks():
    """
    Retorna la lista de tareas almacenadas.
    """
    return service.list_tasks()
