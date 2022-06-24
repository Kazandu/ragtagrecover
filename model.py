from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text
from database import Base
class ToDo(Base):
    __tablename__ = "todo"
    id = Column(Integer, primary_key=True, unique=True)
    videoid = Column(String(11))
    state = Column(String(50))
    uploader = Column(String(100))
    received = Column(String(20))