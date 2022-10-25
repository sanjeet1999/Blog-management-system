from sqlalchemy.orm import Session
import database,models,schemas
from fastapi import HTTPException,status
def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request:schemas.Blog,db:Session):
    new_blog = models.Blog(title=request.title, body=request.body,user_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy_blog(id:int,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} not found")
    else:
        blog.delete(synchronize_session = False)
    db.commit()
    return "done"

def update(id:int,request:schemas.Blog,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    print("printing",blog)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"blog with id {id} not found")
    else:
        blog.update(request.dict(),synchronize_session=False)
    db.commit()
    return request

def show(id:int,db:Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blogs:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id: {id} is not available")
 
    return blogs