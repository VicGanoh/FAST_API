from sqlalchemy.orm import Session
import models, schemas




def get_blog(id: int, db: Session):
    return db.query(models.Blog).filter(models.Blog.id == id).first()


def get_blogs(db: Session):
    return db.query(models.Blog).all()

def create_blog(blog: schemas.Blog, db: Session):   
    new_blog  = models.Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog 




