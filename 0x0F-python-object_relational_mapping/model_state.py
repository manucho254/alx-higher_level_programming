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
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

args = sys.argv  # list of arguments
my_db = 'mysql+mysqldb://{}:{}@localhost/{}'.format(args[1], args[2], args[3])
engine = create_engine(my_db, pool_pre_ping=True)
Base = declarative_base()
Base.metadata.create_all(engine)
session = Session(engine)


class State(Base):
    """ class state that defines a state
        Attributes:
                  id: state id
                  name: state name
    """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, unique=True, primary_key=True)
    name = Column(String(128))


session.close()
