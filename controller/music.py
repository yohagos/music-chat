from fastapi import status, HTTPException
from sqlalchemy.orm import Session

from schemas.models import Music
from controller.history import new_song_added

def save_song(title: str, artist: str, genre: str, user: str, path: str, db: Session):
    request: Music = Music( title=title, genre=genre, path=path, uploaded_by=user, artist=artist)
    song = db.query(Music).filter(Music.artist == request.artist , Music.title == request.title, Music.uploaded_by == user).first()
    if song:
        raise HTTPException(status_code=status.HTTP_405_METHOD_NOT_ALLOWED, detail=f'Song {request.title} and Artist {request.artist} already exists')
    new_song = request
    db.add(new_song)
    db.commit()
    db.refresh(new_song)
    create_song(request.uploaded_by, request.path)
    print(new_song)
    new_song_added(user)
    return new_song

def create_song(user: str, path: str):
    with open(path, 'wb+') as buffer:
        print(f'{user} added a new song')
    buffer.close()

def all_songs(db: Session):
    return db.query(Music).all()
