from pydantic import BaseModel

class ContactsBase(BaseModel):
    user: str
    contact: str

class ShowContacts(ContactsBase):
    class Config():
        orm_mode = True

class ContactRequestBase(BaseModel):
    user: str
    requested: str

class ShowContactRequest(ContactRequestBase):    
    class Config():
        orm_mode = True