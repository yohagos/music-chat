from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)

    music = relationship('Music', back_populates='music')

class Music(Base):
    __tablename__ = "music"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    artitst = Column(String)
    genre = Column(String)
    path = Column(String)
    uploadedBy = Column(String, ForeignKey('user.username'))

    creator = relationship('User', back_populates='music')
