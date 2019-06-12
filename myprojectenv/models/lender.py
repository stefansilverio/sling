#!/usr/bin/python3
"""This is the borrower class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

class Lender(BaseModel, Base):
    """This is the class for Lender
    Attributes:
    loan_size: amount looking to loan
    loan_duration: length of loan
    l_m_r_t: lowest interest rate WTA
    """
    __tablename__ = 'lenders'
    loan_size = Column(Integer, nullable=True)
    loan_duration = Column(Integer, nullable=True)
    interest = Column(Integer, nullable=False)
    email = Column(String(60), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    user = relationship("User", back_populates="lender")
