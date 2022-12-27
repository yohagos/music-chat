from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from schemas.models import Music as MusicModel
from controller.history import new_song_added
from utitlities.logged_in import get_user
from utitlities.util import getTimeStamp

def save_song(title: str, artist: str, genre: str, featuring: str, user: str, path: str, db: Session):
    if featuring is None: featuring=""
    request: MusicModel = MusicModel( title=title, genre=genre, path=path, uploaded_by=user, artist=artist, featuring=featuring, uploaded_at=getTimeStamp())
    song = db.query(MusicModel).filter(MusicModel.artist == request.artist , MusicModel.title == request.title, MusicModel.uploaded_by == user).first()
    if song:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail=f'Song {request.title} and Artist {request.artist} already exists')
    new_song = request
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    new_song_added(user, new_song.id, db)
    return new_song



def all_songs(db: Session):
    songs = db.query(MusicModel).all()
    print(songs)
    return songs

def all_songs_by_user(user: str, db: Session):
    return db.query(MusicModel).filter(MusicModel.uploaded_by == user).all()

def delete_song(id: int, db: Session):
    user = get_user()
    song = db.query(MusicModel).filter(MusicModel.id == id, MusicModel.uploaded_by == user).delete(synchronize_session="evaluate")
    if not song:
        raise HTTPException(status_code=status.HTTP_412_PRECONDITION_FAILED, detail=f'ID {id} or User {user} does not exist.')