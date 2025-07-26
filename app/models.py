
from sqlalchemy import Column, Integer, String, Text, DateTime,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True,nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(),nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now()) 

    owner_id = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)

    owner = relationship("User")


class User(Base):
    __tablename__ = "users"
    id= Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))