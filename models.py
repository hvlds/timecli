from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATETIME, Boolean
from sqlalchemy.orm import sessionmaker
from datetime import timedelta, datetime


class Database:
    def __init__(self):
        db_uri = "sqlite:///db.sqlite"
        self.engine = create_engine(db_uri)
        self.connection = self.engine.connect()
        Session = sessionmaker(self.engine)
        self.session = Session()

db = Database()
Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    date_start = Column(DATETIME)
    date_stop = Column(DATETIME, nullable=True)
    is_active = Column(Boolean)

    def __str__(self):
        return "Task:{} | Start: {} |End: {}".format(
            self.description,
            self.date_start,
            self.date_stop
        )

    def get_duration(self) -> str:
        duration = str(self.date_stop - self.date_start)
        return duration

    @staticmethod
    def get_active_tasks() -> list:
        db = Database()
        query = db.session.query(Task).filter_by(is_active=True)
        query = query.order_by(Task.id.asc())
        active_tasks = list()
        ids = [task.id for task in query]
        for task in query:
            actual_time = datetime.now()
            duration = str(actual_time - task.date_start).split(".")[0]
            active_tasks.append(
                {
                    "id": task.id,
                    "relative_id": ids.index(task.id),
                    "description": task.description,
                    "duration": duration,
                }
            ) 
        return active_tasks
    
    @staticmethod
    def get_all_tasks() -> list:
        db = Database()
        query = db.session.query(Task).all()
        query = query.order_by(Task.id.asc())
        return list(query)
    
    @staticmethod
    def new(description):
        new_task = Task(
            description=description,
            date_start=datetime.now(),
            is_active=True
        )
        db = Database()
        db.session.add(new_task)
        db.session.commit()

    @staticmethod
    def kill(relative_id):
        db = Database()
        active_tasks = Task.get_active_tasks()
        relative_id = int(relative_id)
        if 0 <= relative_id < len(active_tasks):
            task = active_tasks[relative_id]
            task_id = int(task["id"])
            query = db.session.query(Task).filter_by(id=task_id)
            query.update({"is_active":False})         
            db.session.commit()
            print("Task {} terminated.".format(relative_id))
        else:
            print("Task out of range")

Base.metadata.create_all(db.engine)
