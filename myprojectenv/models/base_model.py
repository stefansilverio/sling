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

time = "%Y-%m-%dT%H:%M:%S.%f"

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
                if key is "password":
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

    def update(self, *args, **kwargs):
        """
        update obj values in db
        pass in cls, id, and attr key-values
        encrypt password and email
        """
        if kwargs:
            for k, v in kwargs.items():
                if k is 'password':
                    kwargs[k] = self.__set_password(v)
            models.storage.update(*args, **kwargs)

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

    def query(self, table):
        """
        view all borrowers or lenders in db
        """
        return models.storage.query(table)

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

    def to_dict(self):
        """creates dictionary of the class and returns
        Return:
            returns a dictionary of all the key values in __dict__
        """
        my_dict = dict(self.__dict__)
        print(my_dict)
        my_dict["created_at"] = my_dict["created_at"].strftime(time)
        if '_sa_instance_state' in my_dict.keys():
            del my_dict['_sa_instance_state']
        return my_dict
