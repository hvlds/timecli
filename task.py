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

    def kill(self, id):
        pass

    def all(self, is_active=None):
        if is_active:
            tasks = list(self.db.session.query(TaskModel).filter_by(is_active=is_active))
        else:
            tasks = list(self.db.session.query(TaskModel).all())
        return tasks
    
    def get_active_count(self):
        pass
