from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from typing import List

from database.db import get_db
from authentication.oauth2 import get_current_user

from controller.messages import *
from schemas.users import UserBase
from schemas.messages import *

router = APIRouter(
    prefix='/msg',
    tags=['Messages']
)

@router.get('/{contact}', response_model=List[ShowMessages])
def get_messages(contact: str, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return get_user_messages(contact, db)

@router.post('')
def post_message(request: SendMessage, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return create_message(request, db)
    
@router.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        try:
            data = await websocket.receive_json()
            message_processed = await websocket_data_processing(data)
            await websocket.send_json(
                {
                    "sender": message_processed.get('sender'),
                    "send_time": datetime.now().strftime("%H:%M:%S"),
                    "receiver": message_processed.get('receiver'),
                    "text": message_processed.get('text')
                }
            )
        except WebSocketDisconnect:
            print('Connection to Websocket closed')
            break

