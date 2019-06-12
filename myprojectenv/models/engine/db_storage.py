#!/usr/bin/python3
"""
database engine
"""
import models
import MySQLdb
import json
from sqlalchemy import inspect
from models.user import User
from models.borrower import Borrower
from models.lender import Lender
from models.base_model import Base
from sqlalchemy import table, update
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from collections import defaultdict

class DBstorage:
    """
    handles storge of user information
    """

    all_classes = {'User': User, 'Borrower': Borrower, 'Lender': Lender}

    def __init__(self):
        """
        happens when a new instance of DBStorage is created
        """
        self.__engine = create_engine('mysql+mysqldb://sling:s@localhost/sling', pool_pre_ping=True)


    def all(self, obj=None):
        """
        return dictionary with all objs
        """
        dict_all = {}

        if obj is None:
            for table in DBstorage.all_classes.values():
                type_obj = self.__session.query(table)
                for each_obj in type_obj:
                    k = each_obj.email
                    dict_all[k] = each_obj
        else:
            one_obj = DBstorage.all_classes[obj]
            type_obj = self.__session.query(one_obj)
            for obj in type_obj:
                k = obj.email
                dict_all[k] = obj
        return(dict_all)

    def reload(self):
        """creates all tables in database"""
        Base.metadata.create_all(self.__engine)
        reloaded_sesh = sessionmaker(
            bind=self.__engine, expire_on_commit=True)
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

    def delete(self, cls, obj_id):
        """
        deletes obj from the current database session
        """
        if cls in DBstorage.all_classes.keys():
            obj = DBstorage.all_classes[cls]
            user = self.__session.query(obj).filter(obj.id == obj_id).one()
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

    def update(self, *args, **kwargs):
        """
        update User, Lender, and Borrower information
        """
        class_name = args[0]
        obj = DBstorage.all_classes[class_name]
        if class_name is "User":
            user = self.__session.query(obj).filter(obj.id == args[1]).\
                   update({obj.last_name: kwargs.get('last_name'),
                           obj.first_name: kwargs.get('first_name'),
                           obj.amount_borrowed: kwargs.get('amount_borrowed'),
                           obj.amount_lent: kwargs.get('amount_lent'),
                           obj.password: kwargs.get('password'),
                           obj.email: kwargs.get('email')}, synchronize_session = False)
        elif class_name is "Borrower":
            borrower = self.__session.query(obj).filter(obj.id == args[1]).\
                       update({obj.loan_size: kwargs.get('loan_size'),
                               obj.loan_duration: kwargs.get('loan_duration'),
                               obj.interest: kwargs.get('interest'),
                               obj.email: kwargs.get('email')}, synchronize_session = False)
        else:
            lender = self.__session.query(obj).filter(obj.id == args[1]).\
                     update({obj.loan_size: kwargs.get('loan_size'),
                             obj.loan_duration: kwargs.get('loan_duration'),
                             obj.interest: kwargs.get('interest'),
                             obj.email: kwargs.get('email')}, synchronize_session = False)
        self.__session.commit()

    def query(self, cls, interest=None):
        """
        view all borrowers or lenders in db
        option to sort by interest rate
        """
        table = DBstorage.all_classes[cls]
        if interest is None:
            all_objs = self.__session.query(table).all()
            return all_objs
        else:
            matches = self.__session.query(table).filter(table.interest==interest).all()
            return matches

    def rollback(self):
        """
        issue Session.rollback()
        """
        self.__session.rollback()

    def clean(self):
        """
        delete everything from db
        """
        conn = MySQLdb.connect(host="localhost", user="sling", passwd="s", db="sling")
        cur = conn.cursor()
        cur.execute("DELETE FROM users;")
        conn.commit()
