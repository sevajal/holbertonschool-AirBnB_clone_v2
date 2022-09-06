#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session

class DBStorage:
    """Class DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates a new database"""
        USER = os.getenv('HBNB_MYSQL_USER')
        PASS = os.getenv('HBNB_MYSQL_PWD')
        HOST = os.getenv('HBNB_MYSQL_HOST')
        DB = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(USER, PASS, HOST, DB), pool_pre_ping=True)
        metadata = MetaData()
        if os.getenv('HBNB_ENV') == "test":
            metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return a dictionary all cls in DB o all obj un DB"""
        self.__session = Session(self.__engine)
        dict_return = {}
        if cls:
            for obj in self.__session.query(cls).all():
                dict_return[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        else:
            from models.user import User
            from models.place import Place
            from models.state import State
            from models.city import City
            from models.amenity import Amenity
            from models.review import Review

            list_class = [State, Place, User, City, Review, Amenity]
            for query_cls in list_class:
                for obj in self.__session.query(cls).all():
                    dict_return[obj.to_dict()['__class__'] + '.' + obj.id] = obj
        return dict_return

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    del delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        from models.base_model import BaseModel, Base
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        from sqlalchemy.orm import sessionmaker, scoped_session
        Base.metadata.created_all(self.__engine)
        maker_sessions = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(maker_sessions)
        self.__session = Session()