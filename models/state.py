#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from os import getenv

TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

class State(BaseModel, Base if (TYPE_STORAGE == "db") else object):
    """ State class """
    if TYPE_STORAGE == "db":
        __tablename__ = "states"

        name = Column(String(128), nullable=False)
    else:
        name = ""
