from fastapi import APIRouter, Depends, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List

from schemas.users import UserBase
from schemas.music import ShowMusic, MusicUpload
from controller.music import save_song
from database.db import get_db
from authentication.oauth2 import get_current_user

router = APIRouter(
    prefix='/music',
    tags=['Music']
)

@router.post('/add_song')
async def add_new_song(_artist: str = Form(...), _title: str = Form(...), _genre: str = Form(...), 
                        file: bytes = File(...), db: Session = Depends(get_db), 
                        current_user: UserBase = Depends(get_current_user)):
    print('testing.....')
    request: MusicUpload = MusicUpload(artist = _artist, title = _title, genre = _genre)
    return save_song(request, file, db)

# @router.get('', response_model=ShowMusic)
# def get_song_by_id(id: int, db: Session = Depends(get_db)):
#     pass

