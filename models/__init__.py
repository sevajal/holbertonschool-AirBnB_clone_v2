#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os

TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
if 'db' == TYPE_STORAGE:
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()


