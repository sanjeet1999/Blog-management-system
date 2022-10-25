from sqlalchemy.orm import Session
import schemas,database,models
from Hashing import Hash
from fastapi import HTTPException
def create_user(request:schemas.User,db:Session):
    new_users = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    return new_users

def get_users(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with the id {id} is not available")
    else:
         return user     