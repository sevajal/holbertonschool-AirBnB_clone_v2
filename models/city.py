#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from os import getenv

TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

class City(BaseModel, Base if (TYPE_STORAGE == "db") else object):
    """ The city class, contains state ID and name """
    if TYPE_STORAGE == "db":
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        state_id = ""
        name = ""
