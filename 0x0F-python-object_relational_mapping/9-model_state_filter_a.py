#!/usr/bin/python3
"""
  script that lists all State objects that contain the
  letter a from the database hbtn_0e_6_usa
    - Your script should take 3 arguments:
      mysql username, mysql password and database name
    - You must import State and Base from model_state
      from model_state import Base, State
    - Your script should connect to a MySQL server
      running on localhost at port 3306
    - Results must be sorted in ascending order by states.id
"""

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":

    args = sys.argv  # list of arguments
    my_db = ('mysql+mysqldb://{}:{}@localhost:3306/{}'
             .format(args[1], args[2], args[3])
             )
    engine = create_engine(my_db, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    # create a session
    session = Session()

    # get all objects that contain a
    states = (session.query(State)
              .filter(State.name.ilike('%a%'))
              .order_by(State.id)
              )

    # print nothing if state not found else print first
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
