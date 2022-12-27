from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List
import os

from schemas.users import UserBase
from schemas.music import ShowMusic
from controller.music import \
    save_song, all_songs, all_songs_by_user, delete_song
from database.db import get_db
from authentication.oauth2 import get_current_user
from utitlities.logged_in import get_user
from utitlities.util import getPath, createUserFolderForMusic

router = APIRouter(
    prefix='/music',
    tags=['Music']
)

@router.post('/add_song')
async def add_new_song( new_title: str = Form(...), new_artist: str = Form(...), new_genre: str = Form(...), new_featuring: str = Form(None),
                        file: UploadFile = File(...), db: Session = Depends(get_db), 
                        current_user: UserBase = Depends(get_current_user)):
    user = get_user()
    createUserFolderForMusic(user)
    dest_path = os.path.join(getPath(), user, file.filename)
    return save_song(new_title, new_artist, new_genre, new_featuring, user, dest_path, db)

@router.get('/all', response_model=List[ShowMusic])
def get_all_songs(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return all_songs(db)

@router.get('/all/{user}', response_model=List[ShowMusic])
def get_all_songs_by_user(user: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return all_songs_by_user(user, db)

@router.delete('/{id}')
def delete_song_by_id(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    delete_song(id, db)
    return 'done'