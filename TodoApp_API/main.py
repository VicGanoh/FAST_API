from fastapi import FastAPI, HTTPException
from typing import Optional
from models import Todo

# Creating a todo app api sample

# create an instance of fastAPI
my_app = FastAPI()


    
# lets create a fake database for todo items
todos_db = [
    {"title": "Grocery",
     "description": "Buy foodstuffs at the grocery shop."},
    {"title": "Chores",
     "description":"Clean bathroom"}
]

# home 
@my_app.get('/')
async def index():
    return {"data": "Nothing to display"}

# get a specific todo
@my_app.get('/todos/{id}')
async def get_todo_by_id(id: int):  
    # loop through the db
    for item in todos_db:   
        if id == todos_db[id-1]:
            pass
    return {"todo_data": todos_db[id-1]}

# get all todos
@my_app.get('/todos')
async def get_todos():  
    return {"todos_data": todos_db}

# create a todo
@my_app.post('/todos')
async def create_todo(todo: Todo):
    # convert todo to a dictionary
    new_todo_dict = todo.dict()
    # add new todo to the todo_db
    todos_db.append(new_todo_dict)
    return {"Todo has been created successfully."}

# update a todo
@my_app.put('/todos/{id}')
async def update_todo(id: int, todo: Todo): 
    try:
        todos_db[id] = todo.dict()
        return {"Todo has been updated."}
    except:
        
        raise HTTPException(status_code=404, detail="Todo Not FOund.")

# delete a todo
@my_app.delete('/todos/{id}')
async def delete_todo(id: int):   
    try:
        todos_db.pop(id)
        return {"Todo has been deleted."}
    except:  
        
        raise HTTPException(status_code=404, detail="Todo Not Found.")