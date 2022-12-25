from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)

    music = relationship('Music', back_populates='creator')

class Music(Base):
    __tablename__ = "music"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    artist = Column(String)
    genre = Column(String)
    path = Column(String)
    uploaded_by = Column(String, ForeignKey('users.username'))

    creator = relationship('User', back_populates='music')

class History(Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    
    song_added = Column(Integer, ForeignKey('music.id'))
    added_by = Column(String, ForeignKey('users.username'))