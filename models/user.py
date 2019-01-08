#!/usr/bin/python3
"""This is the user class"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(string(128), nullable=False)
    first_name = Column(string(128), nullable=False)
    last_name = Column(string(128), nullable=False)
