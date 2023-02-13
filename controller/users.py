from fastapi import status, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from schemas.users import UserBase
from schemas.models import User as UserModel, Music as MusicModel
from hashing.hash import get_password_hashed
from utitlities.logged_in import get_user
from utitlities.util import deleteUserFolder, getTimeStamp

def create_user(request: UserBase, db: Session):
    user = db.query(UserModel).filter(UserModel.username == request.username).first()
    if user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f'User with username {request.username} already exists')
    new_user = UserModel(firstname=request.firstname, lastname=request.lastname, username=request.username, password=get_password_hashed(request.password), profile_photo="", created_at=getTimeStamp())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user 

def get_user_info(db: Session):
    username = get_user()
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with ID {id} not found')
    return user

def all_users(db: Session):
    return db.query(UserModel).all()

def upload_photo(user: str, file_path: str, db: Session):
    user = db.query(UserModel).filter(UserModel.username == user).update({"profile_photo": file_path}, synchronize_session="evaluate")
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User {user} not found')
    db.commit()
    return user

def get_profile_photo(db: Session):
    username = get_user()
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if not user.profile_photo: 
        raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY)
    fname = user.profile_photo.split('\\')
    return FileResponse(path=user.profile_photo, filename=fname[len(fname)-1], media_type='image/jpg')
    
def remove_user(db: Session):
    user = get_user()
    db.query(UserModel).filter(UserModel.username == user).delete(synchronize_session="evaluate")
    db.commit()
    
def remove_all(db: Session):
    user = get_user()
    db.query(MusicModel).filter(MusicModel.uploaded_by == user).delete()
    db.commit()
    remove_user(db)
    deleteUserFolder(user)
