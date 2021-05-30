from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "sqlite:///./blog.db"

# create engine
engine = create_engine(DATABASE_URL,connect_args={"check_same_thread": False})

# create session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# create Base
Base = declarative_base()