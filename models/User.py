from pydantic import BaseModel

class User(BaseModel):
    UserName: str
    FirstName: str
    LastName: str
    ContactNumber: str