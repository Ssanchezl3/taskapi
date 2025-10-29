from typing import List, Optional
from datetime import datetime
from app.application.ports.task_repository import TaskRepositoryPort
from app.domain.task import Task

class MemoryTaskRepository(TaskRepositoryPort):
    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._counter = 0

    def next_id(self) -> int:
        self._counter += 1
        return self._counter

    def list(self) -> List[Task]:
        return [self._tasks[k] for k in sorted(self._tasks.keys())]

    def save(self, task: Task) -> Task:
        task.updated_at = datetime.utcnow()
        self._tasks[task.id] = task
        return task

    def get(self, task_id: int) -> Optional[Task]:
        return self._tasks.get(task_id)
