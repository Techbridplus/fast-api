from fastapi import FastAPI
# from sqlalchemy.orm import Session
# from typing import List, Optional

from . import models
from .database import engine
from .routers import todo,user,auth
# Create database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todo.router)
app.include_router(user.router)
app.include_router(auth.router)

# default 
@app.get('/')
def say_hello():
    return {"message":"hello"}
