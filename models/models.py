from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column
from pydantic import BaseModel, Field
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    