from typing import List 
from sqlalchemy.orm import Session
from fastapi import APIRouter,Depends,status,HTTPException
import schemas, database,models,oauth2
from repository import blog


get_db = database.get_db
router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

@router.get('/{id}',status_code=200,response_model=schemas.Showblog)
def show(id,db:Session=Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.show(id, db)
    

@router.get('/',status_code=200,response_model=List[schemas.Showblog])
def all(db:Session=Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.get_all(db)

@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog, db:Session=Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)
    

@router.post("/",status_code=201)
def create(request:schemas.Blog,db:Session=Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request, db)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(get_db),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.destroy_blog(id, db)

