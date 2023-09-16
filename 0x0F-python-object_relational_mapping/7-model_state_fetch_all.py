#!/usr/bin/python3
""" A script that lists all State objects from the database hbtn_0e_6_usa.
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    args = sys.argv  # list of arguments
    my_db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(args[1], args[2], args[3])
    engine = create_engine(my_db, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # create a session
    session = Session()

    # get all states
    states = session.query(State).order_by(State.id).all()

    # print all states
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
