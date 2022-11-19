from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[int]
    login: str
    password: str

#class Staff(BaseModel):
#    id: Optional[int]
#    id_user: int
#    surname: str
#    name: str
#    id_post: int

#class Post(BaseModel):
#    id: Optional[int]
#    name: str
