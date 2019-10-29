from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATETIME, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
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
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    date_start = Column(DATETIME)
    date_stop = Column(DATETIME, nullable=True)
    is_running = Column(Boolean)
    project_id = Column(Integer, ForeignKey("projects.id"))

    def __str__(self):
        return "Task:{} | Start: {} | End: {}".format(
            self.description,
            self.date_start,
            self.date_stop,
        )

    def get_duration(self) -> str:
        duration = str(self.date_stop - self.date_start).split(".")[0]
        return duration

    @staticmethod
    def get_running() -> list:
        db = Database()
        query = db.session.query(Task).filter_by(is_running=True)
        query = query.order_by(Task.id.asc())
        running_tasks = list()
        ids = [task.id for task in query]
        for task in query:
            actual_time = datetime.now()
            duration = str(actual_time - task.date_start).split(".")[0]
            running_tasks.append({
                    "id": task.id,
                    "relative_id": ids.index(task.id),
                    "description": task.description,
                    "duration": duration
                }
            ) 
        return running_tasks
    
    @staticmethod
    def get_all() -> list:
        db = Database()
        query = db.session.query(Task).all()
        return query
    
    @staticmethod
    def new(description):
        new_task = Task(
            description=description,
            date_start=datetime.now(),
            is_running=True
        )
        db = Database()
        db.session.add(new_task)
        db.session.commit()

    @staticmethod
    def kill(relative_id):
        db = Database()
        running_tasks = Task.get_running()
        relative_id = int(relative_id)
        if 0 <= relative_id < len(running_tasks):
            task = running_tasks[relative_id]
            task_id = int(task["id"])
            query = db.session.query(Task).filter_by(id=task_id)
            query.update({
                "is_running": False,
                "date_stop": datetime.now()                
            })         
            db.session.commit()
            print("Task [{}] '{}' terminated.\nTotal time: {}".format(
                    relative_id,
                    task["description"],
                    task["duration"]
            ))
        else:
            print("Task out of range")
    
    @staticmethod
    def kill_last():
        db = Database()
        running_tasks = Task.get_running()
        if len(running_tasks) > 0:
            task = running_tasks[-1]
            task_id = int(task["id"])
            query = db.session.query(Task).filter_by(id=task_id)
            query.update({
                "is_running": False,
                "date_stop": datetime.now()
            })
            db.session.commit()
            print("Last Task '{}' terminated.\nTotal time: {}".format(
                task["description"],
                task["duration"]
            ))
        else:
            print("There is no running task!")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    tasks = relationship("Task")

    def __str__(self):
        return "Project: {}".format(
            self.name
        )

Base.metadata.create_all(db.engine)
