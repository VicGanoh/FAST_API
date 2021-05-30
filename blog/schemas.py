from pydantic import BaseModel 
from typing import Optional

class Blog(BaseModel):
    title : str
    body: str
    
class ShowBlog(Blog):
    title : str
    body: str
    
    class Config():
        orm_mode = True
        
        
# User Class
class User(BaseModel):
    name : str
    email: str
    password: str