from fastapi import status, HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session

from schemas.messages import SendMessage, LoadMessageFor
from schemas.models import Messages as MessageModel, User as UserModel
from utitlities.logged_in import get_user
from utitlities.util import getTimeStamp

def create_message(request: SendMessage, db: Session):
    user = get_user()
    receiver = db.query(UserModel).filter(UserModel.username == request.receiver).first()
    if not receiver:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail=f'Receiver not found')
    if user == request.receiver:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'Users cannot send messages to themself')
    new_msg = MessageModel(receiver=request.receiver, text=request.text, send_date=getTimeStamp(), sender=user, group_id="")
    db.add(new_msg)
    db.commit()
    db.refresh(new_msg)
    return 'added new msg'

### WebSocket

async def websocket_data_processing(data: dict, db: Session):
    msg = MessageModel(
        receiver=data.get('receiver'),
        sender=data.get('sender'),
        text=data.get('text'),
        send_date=getTimeStamp(),
    )
    db.add(msg)
    db.commit()
    db.refresh(msg)
    return data

async def load_messages(receiver: str, db: Session):
    user = get_user()
    receiver_list = db.query(MessageModel).filter(MessageModel.sender == user, MessageModel.receiver == receiver).all()
    sender_list = db.query(MessageModel).filter(MessageModel.receiver == user, MessageModel.sender == receiver).all()
    receiver_list += sender_list
    for rec in receiver_list:
        print(rec.sender, rec.text)
    return receiver_list