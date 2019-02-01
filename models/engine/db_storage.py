#!/usr/bin/python3
"""SQLAlchemy storage module
"""

import json
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __engine = None
    __session = None

    def __init__(self):
        """the init method
        """
        user = os.getenv('HBNB_MYSQL_USER', "hbnb_dev")
        passwd = os.getenv('HBNB_MYSQL_PWD', "hbnb_dev_pwd")
        host = os.getenv('HBNB_MYSQL_HOST', "localhost")
        database = os.getenv('HBNB_MYSQL_DB', "hbnb_dev_db")

        db_str = 'mysql+mysqldb://{}:{}@{}/{}'.format(
            user,
            passwd,
            host,
            database)

        self.__engine = create_engine(db_str, pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            meta = MetaData(self.__engine)
            meta.drop_all()

    def all(self, cls=None):
        """returns a dictionary
        Keyword Args:
            cls: the class to filter
        Return:
            returns a dictionary of __object
        """
        ret_dict = {}
        if cls:
            query = self.__session.query(cls).all()
        else:
            query = []
            query += self.__session.query(City).all()
            query += self.__session.query(State).all()
            query += self.__session.query(User).all()
            query += self.__session.query(Amenity).all()
            query += self.__session.query(Place).all()
            query += self.__session.query(Review).all()

        for obj in query:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            ret_dict[key] = obj

        return ret_dict

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        self.__session.add(obj)

    def save(self):
        """save the file into the database
        """
        self.__session.commit()

    def reload(self):
        """serialize the file path to JSON file path
        """
        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = Session()

    def delete(self, obj=None):
        """deletes an object
        Keyword Args:
            obj: given object to be deleted
        """
        if obj is None:
            cls = type(obj)
            self.__session.query(cls).filter(id=obj.id).delete()

    def close(self):
        """ a method for deserializing the JSON file to objects
        """
        if self.__session:
            self.__session.remove()
