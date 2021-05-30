from fastapi import FastAPI, Depends, status,HTTPException
import schemas, models
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import List


# create database tables
models.Base.metadata.create_all(engine)

# create an instance 
app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a blog post
@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create_blog(blog: schemas.Blog, db: Session = Depends(get_db)):
    # Add new blog to database
    new_blog = models.Blog(title=blog.title, body=blog.body)
    
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return "New blog created."


# Get blog a id specification
@app.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog)
def get_blog(id: int, db: Session = Depends(get_db)):
    # get into the database and get the specified id if it exist 
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found.")
    return blog


# Get all blogs
@app.get('/blog/', status_code=200, response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db)):
    # Fetch all blogs from the database
    all_blogs = db.query(models.Blog).all()
    
    if not all_blogs:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail="No content for blog.")
    
    return all_blogs
    

# Delete a blog
@app.delete('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete_blog(id: int, db: Session = Depends(get_db)):
    # Delete a blog from database
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    # if blog is not available raise exception
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found.")
    blog.delete(synchronize_session=False)
    
    db.commit()
    return "Blog deleted."


# Update a blog
@app.put('/blog/{id}', status_code=200)
def update(id: int, blog: schemas.Blog, db: Session = Depends(get_db)):
    # Update a blog from database
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    
    # if blog is not available raise exception
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" Blog with id {id} not found.")
    blog.update({'title':blog.title, 'body':blog.body}, synchronize_session=False)
    
    db.commit()
    return "Blog updated"

# Create a user
@app.post('/user')
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(name=user.name, email=user.email, password=user.password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return "User created"

    
    

    