#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
import os

TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')
"""if "db" == TYPE_STORAGE:
    storage = 
else:"""
    storage = FileStorage()
storage.reload()


