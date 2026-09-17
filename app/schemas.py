from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

    @field_validator('username')
    @classmethod
    def validate_username(cls, value):
        if len(value) < 3:
            raise ValueError('Username must be at least 3 characters long')
        return value

    @field_validator('email')
    @classmethod
    def validate_email(cls, value):
        if '@' not in value:
            raise ValueError('Invalid email address')
        return value

class UserResponse(BaseModel):
    id: int
    username: str
    email:str
    created_at: datetime

    class Config:
        from_attribute= True

class Token(BaseModel):
    access_token: str
    token_type: str

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    priority: Optional[str] = "MEDIUM"
    due_date: Optional[datetime] = None

    @feild_validator('title')
    @classmethod
    def validate_title(cls, value):
        if len(value) < 3:
            raise ValueError('Title must be at least 3 characters long')
        return value

    @feild_valiadtor('priority')
    @classmethod
    def validate_priority(cls, value):
        valid=["LOW", "MEDIUM", "HIGH"]
        if value.upper() not in valid:
            raise ValueError('Priority must be one of LOW, MEDIUM, HIGH')
        return value.upper()

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime]= None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    status: str
    priority: str
    due_date: Optional[datetime] = None
    created_at: datetime
    user_id: int

    class Config:
        orm_mode = True