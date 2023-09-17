#!/usr/bin/python3
"""
  Script that creates the State “California” with
  the City “San Francisco” from the database
  hbtn_0e_100_usa: (100-relationship_states_cities.py)

  - Script should take 3 arguments:
    mysql username, mysql password and database name
  - Script should connect to a MySQL server
    running on localhost at port 3306
  - Use the cities relationship for all State objects
"""

import sys

from relationship_state import State, Base
from relationship_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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

    # Get list of states
    states = session.query(State).all()

    # print states and all cities connected
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
