from fastapi import APIRouter, Depends, UploadFile, File, Form
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session
from typing import List
import os

from schemas.users import UserBase
from schemas.music import Music, ShowMusic
from controller.music import \
    save_song, all_songs, all_songs_by_user, delete_song, song_to_play
from database.db import get_db
from authentication.oauth2 import get_current_user
from utitlities.util import create_file, createFoldersAndFilePaths

router = APIRouter(
    prefix='/music',
    tags=['Music']
)

@router.post('/add_song')
async def new_song(artist: str = Form(), title: str = Form(), genre: str = Form(), featuring: str = Form(), file: UploadFile = File(), db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    _, dest_path = createFoldersAndFilePaths(file.filename)
    await create_file(dest_path, file)
    return save_song(artist=artist, title=title, genre=genre, featuring=featuring, path=dest_path, db=db)

@router.get('/all', response_model=List[Music])
def get_all_songs(db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return all_songs(db)

@router.get('/all/{user}', response_model=List[ShowMusic])
def get_all_songs_by_user(user: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return all_songs_by_user(user, db)

@router.get('/song/{id}')
def get_song_by_id(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    file = song_to_play(id, db)
    if os.path.exists(file.path):
        return FileResponse(path=file.path)
    return {'error', 'file not found'}

@router.delete('/{id}')
def delete_song_by_id(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    delete_song(id, db)
    return 'done'
