from fastapi import status, HTTPException, UploadFile
from sqlalchemy.orm import Session

from utitlities.util import createUserFolderForMusic
from schemas.music import MusicUpload
from schemas.models import Music as MusicModel
from utitlities.logged_in import get_user
from utitlities.util import getPath

def save_song(request: MusicUpload, file: UploadFile, db: Session):
    user = get_user(db)
    dest_path = getPath() + '/' + user + '/' + file.filename

    song = db.query(MusicModel).filter(MusicModel.artitst == request.artist, MusicModel.title == request.title).first()
    if song:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                detail=f'Song {request.title} and Artist {request.artist} already exists')
    new_song = MusicModel(
        artist=request.artist,
        title=request.title,
        genre=request.genre,
        path=dest_path,
        uploadedBy=user
    )
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    file.write(dest_path)
    return new_song