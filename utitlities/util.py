import os, shutil
from decouple import config
from datetime import datetime

path = config('MUSIC_FOLDER')

def checkMusicFolder():
    if not os.path.exists(path):
        os.makedirs(path)

def createUserFolderForMusic(username: str):
    new_path = path+'/'+username
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        return new_path

def getPath():
    return path

def deleteUserFolder(user: str):
    user_path = os.path.join(path, user)
    shutil.rmtree(user_path)

def getTimeStamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")