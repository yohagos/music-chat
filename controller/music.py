from fastapi import status, HTTPException, UploadFile
from sqlalchemy.orm import Session
import shutil

from utitlities.util import createUserFolderForMusic
from schemas.music import MusicUpload
from schemas.models import Music
from utitlities.logged_in import get_user
from utitlities.util import getPath

async def save_song(request: Music, file: UploadFile, db: Session):
    await create_song(file, request.path)    
    song = db.query(Music).filter(Music.artist == request.artist , Music.title == request.title).first()
    if song:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail=f'Song {request.title} and Artist {request.artist} already exists')
    new_song = request
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    
    return new_song

async def create_song(file: UploadFile, path: str):
    f = await file.read()
    dest_file = open(path, 'wb+')
    dest_file.write(f)
    dest_file.close()