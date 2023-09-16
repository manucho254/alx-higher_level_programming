#!/usr/bin/python3
""" Script that prints the first State object from the database hbtn_0e_6_usa

    - script takes 3 arguments: mysql username, mysql password and database name
    - Import State and Base from model_state - from model_state import Base, State
    - Your script should connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by states.id
    - If the table states is empty, print Nothing followed by a new line
"""

import sys
from sqlalchemy import create_engine, Column, Integer, String, asc
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    args = sys.argv  # list of arguments
    my_db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(args[1], args[2], args[3])
    engine = create_engine(my_db, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    query = session.query(State).order_by(State.id)
    first = query.first()
    if not first:
        print("Nothing")
    else:
        print("{}: {}".format(first.id, first.name))
    session.close()
