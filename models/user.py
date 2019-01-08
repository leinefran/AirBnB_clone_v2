#!/usr/bin/python3
"""This is the user class"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'
    email = Column('email', String(128), nullable=False)
    password = Column('password', String(128), nullable=False)
    first_name = Column('first_name', String(128), nullable=False)
    last_name = Column('last_name', String(128), nullable=False)
