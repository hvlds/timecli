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

class TaskModel(Base):
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
        query = db.session.query(TaskModel).filter_by(is_active=True)
        query = query.order_by(TaskModel.id.asc())
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
        query = db.session.query(TaskModel).all()
        query = query.order_by(TaskModel.id.asc())
        return list(query)

Base.metadata.create_all(db.engine)
