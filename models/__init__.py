#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.file_storage import FileStorage

TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
if 'db' == TYPE_STORAGE:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
