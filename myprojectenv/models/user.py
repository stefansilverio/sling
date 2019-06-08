#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from models.borrower import Borrower
from models.lender import Lender
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """This is the class for user
    Attributes:
    email: email address
    password: password for you login
    first_name: first name
    last_name: last name
    amount_borrowed: money borrowed
    amount_lent: money_lent
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    amount_borrowed = Column(Integer, nullable=False)
    amount_lent = Column(Integer, nullable=False)
