from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from schemas.users import UserBase
from schemas.models import User as UserModel, Music as MusicModel
from hashing.hash import get_password_hashed
from utitlities.logged_in import get_user

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

def all_users(db: Session):
    print('test')
    return db.query(UserModel).all()

def remove_user(db: Session):
    user = get_user()
    db.query(UserModel).filter(UserModel.username == user).delete(synchronize_session="evaluate")
    db.commit()
    return user
    
def remove_all(db: Session):
    user = get_user()
    db.query(MusicModel).filter(MusicModel.uploaded_by == user).delete()
    db.commit()
    remove_user(db)