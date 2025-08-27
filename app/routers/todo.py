from fastapi import  Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session

from typing import List 

from .. import models, schemas,oauth2
from ..database import get_db


router = APIRouter(
    prefix="/todos",
    tags=['Todos']
)


@router.get("/",response_model=List[schemas.Todo])
def get_todos(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0):
    
    todos = db.query(models.Todo).offset(skip).limit(limit).all()

    return todos


@router.post("/",status_code=status.HTTP_201_CREATED, response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate,db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    new_todo = models.Todo( **todo.dict(), owner_id=current_user.id)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return new_todo


@router.get("/{id}", response_model=schemas.Todo)
def get_post(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    todo = db.query(models.Todo).filter(models.Todo.id == id).first()

    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Todo with id: {id} was not found")

    return todo

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(id: int, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    todo_query = db.query(models.Todo).filter(models.Todo.id == id)

    todo = todo_query.first()

    if todo == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"todo with id: {id} does not exist")

    if todo.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    todo_query.delete(synchronize_session=False)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model=schemas.Todo)
def update_todo(id: int, updated_todo: schemas.TodoUpdate, db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):

    todo_query = db.query(models.Todo).filter(models.Todo.id == id)

    todo = todo_query.first()

    if todo == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"todo with id: {id} does not exist")

    if todo.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="Not authorized to perform requested action")

    todo_query.update(updated_todo.dict(), synchronize_session=False)

    db.commit()

    return todo_query.first()