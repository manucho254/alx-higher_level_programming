#!/usr/bin/python3
"""
  script that changes the name of a State
  object from the database hbtn_0e_6_usa.

  - Your script should take 3 arguments:
    mysql username, mysql password and database name.
  - Import State and Base from model_state
    - from model_state import Base, State
  - Script should connect to a MySQL server
    running on localhost at port 3306
  - Change the name of the State where id = 2 to New Mexico
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
    state = session.query(State).filter(State.id == 2).first()

    # update state name
    state.name = "New Mexico"
    session.commit()

    session.close()
