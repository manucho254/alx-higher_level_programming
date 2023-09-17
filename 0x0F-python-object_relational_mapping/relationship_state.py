#!/usr/bin/python3
"""
   python file that contains the class definition of a,
   State and an instance Base = declarative_base():

   State class:
      - inherits from Base Tips
      - links to the MySQL table states
      - class attribute id that represents a,
        column of an auto-generated, unique integer,
        Can’t be null and is a primary key
      - class attribute name that represents a column,
       of a string with maximum 128 characters and can’t be null
"""

import sys
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

args = sys.argv  # list of arguments
Base = declarative_base()


class State(Base):
    """ class State that defines a state
        Attributes:
                  id: state id
                  name: state name
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True, primary_key=True)
    name = Column(String(128))
    cities = relationship('City', backref='state', cascade='all, delete')
