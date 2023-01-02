#!/usr/bin/python3
"""
create DBStorage
"""

from requests import delete
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os
from models.base_model import Base

class DBStorage:
    __engine: None
    __session: None

    def __init__(self):
        """Returns a dictionary of models currently in storage"""
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine(
            f"mysql+mysqldb://{user}:{password}@{host}/{db}", pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls != None:
            objects = self.__session.query(cls).all()
        else:
            c = [City, Amenity, User, State, Place, Review]
            objects = []
            for k in c:
                objects += self.__session.query(k)
        return {"{}.{}".format(type(obj).__name__, obj.id): obj for obj in
                objects}

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """save new object to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """remove new object from session"""
        if obj != None:
            self.__session.delete(obj)

    def reload(self):
        """Create the table"""
        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()

    def close(self):
        """close the SQLAlchemy session"""
        self.__session.close()
