from fastapi import FastAPI

from routes import users, music, login
from database.db import engine
from schemas.models import Base

from utitlities.util import checkMusicFolder

checkMusicFolder()

app = FastAPI()

app.include_router(login.router)
app.include_router(users.router)
app.include_router(music.router)

Base.metadata.create_all(engine)