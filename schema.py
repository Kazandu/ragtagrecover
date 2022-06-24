from datetime import date
from pydantic import BaseModel
class ToDo(BaseModel):
    id = int
    videoid = str
    state = str
    uploader = str
    received = str

    class Config:
        orm_mode = True