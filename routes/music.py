from fastapi import APIRouter, Depends, status, UploadFile, File, Form, HTTPException
from sqlalchemy.orm import Session
from typing import List

from schemas.users import UserBase
from schemas.music import ShowMusic, MusicInfo, MusicFile
from controller.music import \
    save_song, all_songs, all_songs_by_user, delete_song
from database.db import get_db
from authentication.oauth2 import get_current_user
from utitlities.util import create_file, createFoldersAndFilePaths

router = APIRouter(
    prefix='/music',
    tags=['Music']
)

@router.post('/add_info')
async def add_new_info( request: MusicInfo, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    print(request)
    return save_song(request, db)

# How to upload file in fastapi? 
@router.post("/addSong")
async def post_endpoint(file: UploadFile = File(), current_user: UserBase = Depends(get_current_user)):
    _, dest_path = createFoldersAndFilePaths(file.filename) 
    await create_file(dest_path, file)
    return f'Received {file.filename}'
    #return {'file size: ', len(file)}


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