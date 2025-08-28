from fastapi import FastAPI
from .routers import todo,user,auth
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine)   if we use alembic, we don't need this line
# Base.metadata.create_all(bind=engine)  # Uncomment if you want to create tables directly

app = FastAPI()

origins = [
    "https://techbridplus.me",
    "http://localhost", # Add for local development if needed
    "http://localhost:8001", # Add for local development if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo.router)
app.include_router(user.router)
app.include_router(auth.router)

# default 
@app.get('/')
def say_hello():
    return {"message":"hello ok testing 1"}


