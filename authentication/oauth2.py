from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt

from . import token
from utitlities.logged_in import set_logged_in

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(data: str = Depends(oauth2_scheme)):
    print(oauth2_scheme)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Could not validate credentials',
        headers={'WWW-Authenticate': 'Bearer'}
    )
    set_logged_in(token.get_email_from_token(data))
    return token.verify_token(data, credentials_exception)