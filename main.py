from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import users, music, login, messages, contacts
from database.db import engine
from schemas.models import Base

from utitlities.util import checkMusicFolder

checkMusicFolder()

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router)
app.include_router(users.router)
app.include_router(music.router)
app.include_router(messages.router)
app.include_router(contacts.router)

Base.metadata.create_all(engine)