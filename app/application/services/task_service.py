from app.domain.task import Task, TaskCreate, Status

class TaskService:
    def __init__(self, repository):
        self.repository = repository

    def create_task(self, data: TaskCreate) -> Task:
        status = getattr(data, "status", Status.pending)
        task = Task(
            id=self.repository.next_id(),
            title=data.title,
            description=getattr(data, "description", ""),
            status=status
        )
        return self.repository.save(task)

    def list_tasks(self):
        return self.repository.list()
