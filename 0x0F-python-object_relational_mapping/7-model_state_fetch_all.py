#!/usr/bin/python3
""" Script that lists all State objects from the database hbtn_0e_6_usa.
    - script takes 3 arguments: mysql username, mysql password and database name
    - Import State and Base from model_state - from model_state import Base, State
    - Your script should connect to a MySQL server running on localhost at port 3306
    - Results must be sorted in ascending order by states.id
"""

import sys

from sqlalchemy import create_engine, Column, Integer, String, asc
from sqlalchemy.orm import Session

from model_state import Base, State

if __name__ == "__main__":
    args = sys.argv  # list of arguments
    my_db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(args[1], args[2], args[3])
    engine = create_engine(my_db, pool_pre_ping=True)
    session = Session(engine)
    Base.metadata.create_all(engine)

    query = session.query(State).order_by(asc(State.id))
    for row in query.all():
        print("{}: {}".format(row.id, row.name))
    session.close()
