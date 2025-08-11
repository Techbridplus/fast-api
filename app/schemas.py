from pydantic import BaseModel,EmailStr
from datetime import datetime
from typing import Optional

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class Todo(TodoBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True 

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username:EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[str] = None


