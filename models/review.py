#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv

TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

class Review(BaseModel, Base if (TYPE_STORAGE == "db") else object):
    """ Review classto store review information """
    if TYPE_STORAGE == "db":
        __tablename__ = "reviews"
        text = Column(String(1024), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        place_id = Column(String(60), ForeignKey('places.id'), nullable=False)

    else:
        place_id = ""
        user_id = ""
        text = ""
