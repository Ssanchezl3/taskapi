from abc import ABC, abstractmethod
from typing import List, Optional
from app.domain.task import Task

class TaskRepositoryPort(ABC):
    @abstractmethod
    def list(self) -> List[Task]:
        raise NotImplementedError

    @abstractmethod
    def save(self, task: Task) -> Task:
        raise NotImplementedError

    @abstractmethod
    def get(self, task_id: int) -> Optional[Task]:
        raise NotImplementedError

    @abstractmethod
    def next_id(self) -> int:
        raise NotImplementedError
