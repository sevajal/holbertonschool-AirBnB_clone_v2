#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from models.place import place_amenity
from sqlalchemy.orm import relationship
from os import getenv

TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

class Amenity(BaseModel, Base if (TYPE_STORAGE == "db") else object):
    """Amenities class"""
    if TYPE_STORAGE == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary=place_amenity, viewonly=False, back_populates="amenities")

    else:                   
        name = ""
