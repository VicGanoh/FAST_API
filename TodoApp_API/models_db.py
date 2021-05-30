from database import Base
from sqlalchemy import Column, Integer, String

class Todo(Base):
    __tablename__ = 'todos'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(15))
    last_name = Column(String(15))
    email = Column(String)
    password = Column(String)