#!/usr/bin/python3
"""
   script that prints the State object with the name passed,
   as argument from the database hbtn_0e_6_usa
    - Script should take 4 arguments: mysql username,
      mysql password,
      database name and state name to search (SQL injection free).
    - Import State and Base from model_state -
      from model_state import Base, State
    - Script should connect to a MySQL server running on localhost at port 3306
    - You can assume you have one record with the state name to search
    - Results must display the states.id
    - If no state has the name you searched for, display Not found
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

    # get object with name in args
    state = session.query(State).filter(State.name == "%s" % args[4]).first()

    # if no state is found
    if not state:
        print("Not found")
    else:
        # print state id
        print(state.id)

    session.close()
