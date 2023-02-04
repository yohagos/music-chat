from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List

from schemas.users import UserBase, ShowUser
from authentication.oauth2 import get_current_user
from database.db import get_db
from controller.users import get_user_by_id, all_users, create_user, upload_photo, remove_user, remove_all
from utitlities.util import create_file, createFoldersAndFilePaths

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.get('', response_model=ShowUser)
def get_user(id: int, db: Session = Depends(get_db)):
    return get_user_by_id(id, db)

@router.get('s', response_model=List[ShowUser])
def get_all_users(db: Session = Depends(get_db)):
    return all_users(db)

@router.post('', response_model=ShowUser)
def create_new_user(request: UserBase, db: Session = Depends(get_db)):
    return create_user(request, db)

@router.post('/upload_photo')
async def post_uploaad_photo(file: UploadFile = File(...), db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    user, dest_path = createFoldersAndFilePaths(file.filename)
    await create_file(dest_path, file)
    return upload_photo(user, dest_path, db)

@router.delete('/delete')
def delete_account(db: Session = Depends(get_db),current_user: UserBase = Depends(get_current_user)):
    remove_user(db)
    return 'done'

@router.delete('/delete/all')
def delete_account_and_songs(db: Session = Depends(get_db),current_user: UserBase = Depends(get_current_user)):
    remove_all(db)
    return 'done'