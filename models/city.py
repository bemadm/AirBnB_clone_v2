#!/usr/bin/python3
""" City Module for HBNB project """

from os import getenv
from models.base_model import Base, BaseModel
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship



class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        places = relationship("Place", backref="city",
                              cascade="all, delete-orphan")

