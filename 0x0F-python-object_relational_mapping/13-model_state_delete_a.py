#!/usr/bin/python3
"""
  script that deletes all State objects with a name
  containing the letter a from the database hbtn_0e_6_usa.

  - Script should take 3 arguments:
    mysql username, mysql password and database name
  - Import State and Base from model_state
    - from model_state import Base, State
"""

import sys

from sqlalchemy import create_engine, desc
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
              )

    # deletes all objects that contain a
    states.delete(synchronize_session=False)
    session.commit()

    session.close()
