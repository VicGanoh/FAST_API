from database import Base 
from sqlalchemy import Column, Integer, String

# create moodel and table for blog 
class Blog(Base):
    # declare a table name for blog db
    __tablename__ = "blog"
    # create fields for blog
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)

    