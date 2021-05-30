from pydantic import BaseModel

# create a class type to inherit model
class Todo(BaseModel): 
    # a todo app will have a title and description 
    # title of todo which is optional  
    title : str
    # description of todo app  
    description: str
    

# class User(BaseModel):
#     first_name: str
#     last_name: str
#     email: str
#     password: str