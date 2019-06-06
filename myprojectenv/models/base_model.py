#!/usr/bin/python3
"""
base_model class to be inherited by all models
"""
import models
from uuid import uuid4
import hashlib
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime


Base = declarative_base()

class BaseModel:
    """
    BaseModel class for all other classes
    """
    id = Column(String(60), unique=True,
                primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())


    def __init__(self, *args, **kwargs):
        """
        Instantiation of base model class
        set user attributes for table
        Args:
          args - name of cls obj to create
          kwargs - assign user attributes
        """

        self.id = str(uuid4())
        self.created_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key is "password" or key is "email":
                    encrypted = self.__set_password(kwargs[key])
                    setattr(self, key, encrypted)
                else:
                    setattr(self, key, value)

    def __set_password(self, data):
        """
        encrypt user password w/ MD5
        """
        secure = hashlib.md5()
        secure.update(data.encode("utf-8"))
        encrypted = secure.hexdigest()
        return encrypted

    def all(self):
        """
        return dict of all objs in db
        currently printing dictionary
        """
        obj = models.storage.all()
        return obj

    def save(self):
        """
        adding obj to current db session
        """
        models.storage.new(self)
        models.storage.save()

    def delete(self, cls, u_id):
        """
        delete obj from db
        """
        cls = cls.__name__
        models.storage.delete(cls, str(u_id))

    def close(self):
        """
        close session, empty pool
        """
        models.storage.close()

    def drop_all(self):
        """
        drop all tables
        """
        models.storage.drop_all()
