from sqlalchemy.orm import Session

from schemas.models import User
from . import logged_in

log_in: str

def set_logged_in(user: str):
    logged_in.log_in = user

def get_user():
    return log_in