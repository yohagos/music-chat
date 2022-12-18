from sqlalchemy.orm import Session

from schemas.models import User

logged_in: str

def set_logged_in(user: str):
    logged_in = user

def get_user(db: Session):
    return db.query(User).filter(User.email == logged_in).first()