import os
from decouple import config

path = config('MUSIC_FOLDER')

def checkMusicFolder():
    print('check music function')
    if not os.path.exists(path):
        os.makedirs(path)
    print('check music function - end')

def createUserFolderForMusic(username: str):
    new_path = path+'/'+username
    if not os.path.exists(new_path):
        os.makedirs(new_path)
        return new_path

def getPath():
    return path