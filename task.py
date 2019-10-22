from models import Database, TaskModel
from datetime import datetime

class Task:
    def __init__(self):
        self.db = Database()
    
    def new(self, description):
        new_task = TaskModel(
            description=description,
            date_start=datetime.now(),
            is_active=True
        )
        self.db.session.add(new_task)
        self.db.session.commit()

    def kill(self):
        pass

    def all(self):
        all_tasks = list(self.db.session.query(TaskModel).all())
        for task in all_tasks:
            print(task)
    
    def all_active(self):
        pass

    def all_inactive(self):
        pass
    
    def get_active_count(self):
        pass
