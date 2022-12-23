from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List
import os

from schemas.users import UserBase
from schemas.models import Music
from controller.music import save_song
from database.db import get_db
from authentication.oauth2 import get_current_user
from utitlities.logged_in import get_user
from utitlities.util import getPath, createUserFolderForMusic

router = APIRouter(
    prefix='/music',
    tags=['Music']
)

@router.post('/add_song')
async def add_new_song( new_title: str = Form(...), new_artist: str = Form(...), new_genre: str = Form(...), 
                        file: UploadFile = File(...), db: Session = Depends(get_db), 
                        current_user: UserBase = Depends(get_current_user)):
    user = get_user()
    createUserFolderForMusic(user)
    dest_path = os.path.join(getPath(), user, file.filename)
    return save_song(new_title, new_artist, new_genre, user, dest_path, file, db)
