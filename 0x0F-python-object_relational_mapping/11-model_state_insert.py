#!/usr/bin/python3
"""
   script that adds the State object “Louisiana”
   to the database hbtn_0e_6_usa.

   - Script takes 3 arguments:
     mysql username, mysql password and database name
   - Import State and Base from model_state
     - from model_state import Base, State
   - The script should connect to a MySQL server
     running on localhost at port 3306
   - Print the new states.id after creation
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
    state = State(name="Louisiana")

    # add new state
    new = session.add(state)
    session.commit()
    last = session.query(State).order_by(desc(State.id)).first()

    # print state id
    print(last.id)

    session.close()
