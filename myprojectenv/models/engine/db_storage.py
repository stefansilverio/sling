#!/usr/bin/python3
"""
database engine
"""
import models
from models.user import User
from models.base_model import Base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session

class DBstorage:
    """
    handles storge of user information
    """

    all_classes = {'User': User}

    def __init__(self):
        """
        happens when a new instance of DBStorage is created
        """
        self.__engine = create_engine('mysql+mysqldb://sling:s@localhost/sling', pool_pre_ping=True)


    def all(self):
        """
        return dictionary with all objs
        """
        dict_all = {}
        for table in DBstorage.all_classes.values():
            type_obj = self.__session.query(table)
            for one_obj in type_obj:
                cls_name = one_obj.__class__.__name__
                k = cls_name + '.' + one_obj.id
                dict_all[k] = one_obj
        print(dict_all)

    def reload(self):
        """creates all tables in database"""
        Base.metadata.create_all(self.__engine)
        reloaded_sesh = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(reloaded_sesh)
        self.__session = Session()

    def new(self, obj):
        """adds an object to the current datatabase session
        """
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, cls, code):
        """
        deletes obj from the current database session
        """
        if cls.__name__ in DBstorage.all_classes.keys():
            obj = DBstorage.all_classes[cls.__name__]

        else:
            return 1

        user = self.__session.query(obj).filter(obj.id == str(code)).one()
        self.__session.delete(user)
        self.__session.commit()

    def close(self):
        """
        close self.__session Session object
        """
        self.__session.close()

    def drop_all(self):
        """
        drop all tables
        """
        Base.metadata.drop_all(self.__engine)

    def update(self):
        """
        update User, Lender, and Borrower information
        """
        pass
