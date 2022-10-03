from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String
)

from bottleplate.app.models import Base


class User(Base):
    """Model of a user."""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    dob = Column(String)
    

    def __init__(self):
        self.name = ''
