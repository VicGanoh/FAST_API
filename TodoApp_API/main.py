from fastapi import FastAPI, HTTPException, Depends, status 
from typing import Optional
from models import Todo
import models_db
from database import engine, SessionLocal
from sqlalchemy.orm import Session


# Creating a todo app api sample
models_db.Base.metadata.create_all(engine)

# create an instance of fastAPI
my_app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    
    try:
        yield db
    except:
        db.close()



# home 
@my_app.get('/')
async def index():
    return {"data": "Nothing to display"}

# get a specific todo
@my_app.get('/todos/{id}', status_code=status.HTTP_202_ACCEPTED)
async def get_todo(id: int, db: Session = Depends(get_db)):  
    todo = db.query(models_db.Todo).filter(models_db.Todo.id == id).first()
    if not todo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {id} not found")
    return todo
    

# get all todos
@my_app.get('/todos', status_code=status.HTTP_200_OK)
async def get_todos(db: Session = Depends(get_db)):
    all_todos = db.query(models_db.Todo).all()  
    if not all_todos:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No content available")
    return all_todos

# create a todo
@my_app.post('/todos', status_code=status.HTTP_201_CREATED)
async def create_todo(todo: Todo, db: Session = Depends(get_db)):
    
    new_todo = models_db.Todo(title = todo.title, description = todo.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return "Todo has been created successfully."

# update a todo
@my_app.put('/todos/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update_todo(id: int, todo: Todo, db: Session = Depends(get_db)):
    update_ = db.query(models_db.Todo).filter(models_db.Todo.id == id)
    if not update_.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {id} not found.")
    update_.update({'title':todo.title,'description':todo.description}, synchronize_session=False)
    db.commit() 
    return "Todo has been updated."

# # delete a todo
@my_app.delete('/todos/{id}', status_code=status.HTTP_200_OK)
async def delete_todo(id: int, db: Session = Depends(get_db)):
    deleted_todo = db.query(models_db.Todo).filter(models_db.Todo.id == id)
    if not deleted_todo.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with id {id} not found.")
    deleted_todo.delete(synchronize_session=False)
    db.commit()
    return "Todo has been deleted." 


# @my_app.post('/user')
# async def create_user(user: User, db: Session = Depends(get_db)):
#     new_user = models_db.Todo(first_name=user.first_name, last_name=user.last_name,
#                               email=user.email, password=user.password) 
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return "user has been created successfully."
   