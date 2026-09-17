from sqlalchemy import Columns, Integer, String, Float, DateTime, ForiegnKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
import enum

class TaskStatus(str,enum.Enum):
    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"

class TaskPriority(str, enum.Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class User(Base):
    __tablename__="USERS"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)  
    email = Column(String(50), unique=True, index=True)
    hashed_password = Column(String(255))
    tasks = relationship("Task", back_populates="user")

class Task(Base):
    __tablename__="TASKS"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(String(255))
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING)
    priority = Column(Enum(TaskPriority), default=TaskPriority.MEDIUM)
    due_date = Column(DateTime)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    user_id = Column(Integer, ForeignKey("USERS.id"))
    user = relationship("User", back_populates="tasks")


    