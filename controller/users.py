from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from schemas.users import UserBase
from schemas.models import User as UserModel
from hashing.hash import get_password_hashed

def create_user(request: UserBase, db: Session):
    user = db.query(UserModel).filter(UserModel.username == request.username).first()
    if user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f'User with username {request.username} already exists')
    new_user = UserModel(username=request.username, password=get_password_hashed(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 

def get_user_by_id(id: int, db: Session):
    user = db.query(UserModel).filter(UserModel.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with ID {id} not found')
    return user
