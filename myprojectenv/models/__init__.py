#!/usr/bin/python3
from models.base_model import BaseModel
from models.engine.db_storage import DBstorage

storage = DBstorage()

storage.reload()
