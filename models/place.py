#!/usr/bin/python3
""" Place Module for HBNB project """
import modules
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.reviews import Review
from sqlalchemy import Column, Float, Integer, String, ForeignKey
from os import getenv

TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

class Place(BaseModel, Base if (TYPE_STORAGE == "db") else object):
    """ A place to stay """
    if TYPE_STORAGE == "db":
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place")

    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """returns the list of City instances with state_id equals to the current State.id"""
            reviews = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews
