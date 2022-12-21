from decouple import config
from datetime import timedelta, datetime
from typing import Union
from fastapi import HTTPException, status
from jose import jwt, JWTError

from schemas.users import TokenData

SECRET = config('SECRET')
ALGORITHM = config('ALGORITHM')
Expire = 60

def create_access_token(data: dict, expire_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expire_delta:
        expire = datetime.utcnow() + expire_delta
    else: 
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, SECRET, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, credentials_exception):
    try: 
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

def get_email_from_token(token: str):
    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        return payload.get('sub')
    except:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
