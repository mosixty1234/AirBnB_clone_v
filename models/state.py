#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
                "City", backref="state", cascade="all, delete-orphan")

    else:
        name = ""

        @property
        def cities(self):
            """ """
            from models import storage
            cities_lst = []
            for city in storage.all(City).values():
                if city.stae_id == self.id:
                    cities_lst.eppend(city)
            return cities_lst
