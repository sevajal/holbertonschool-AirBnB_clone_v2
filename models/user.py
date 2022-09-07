#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy.orm import relationship
from models.reviews import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv

TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

class User(BaseModel, Base if (TYPE_STORAGE == "db") else object):
    """This class defines a user by various attributes"""
    if TYPE_STORAGE == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        reviews = relationship("Review", backref=backref("user", cascade="all, delete-orphan"))

    
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
