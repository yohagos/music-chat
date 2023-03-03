from fastapi import status, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from schemas.models import Music as MusicModel
from utitlities.logged_in import get_user
from utitlities.util import getTimeStamp

def save_song(artist: str, title: str, genre: str, featuring: str, path: str, db: Session):
    user = get_user()
    if featuring is None: featuring=""
    request: MusicModel = MusicModel( title=title, genre=genre, uploaded_by=user, artist=artist, featuring=featuring, path=path, uploaded_at=getTimeStamp())
    song = db.query(MusicModel).filter(MusicModel.artist == artist , MusicModel.title == title, MusicModel.uploaded_by == user).first()
    if song:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail=f'Song {request.title} and Artist {request.artist} already exists')
    new_song = request
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    return new_song

def all_songs(db: Session):
    return db.query(MusicModel).all()

def all_songs_by_user(user: str, db: Session):
    return db.query(MusicModel).filter(MusicModel.uploaded_by == user).all()

def song_to_play(id: int, db: Session):
    song = db.query(MusicModel).filter(MusicModel.id == id).first()
    if not song:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    fname = song.path.split('\\')
    return FileResponse(path=song.path, filename=fname[len(fname)-1], media_type='audio/mpeg')

def delete_song(id: int, db: Session):
    user = get_user()
    song = db.query(MusicModel).filter(MusicModel.id == id, MusicModel.uploaded_by == user).delete(synchronize_session="evaluate")
    if not song:
        raise HTTPException(status_code=status.HTTP_412_PRECONDITION_FAILED, detail=f'ID {id} or User {user} does not exist.')


