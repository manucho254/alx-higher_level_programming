#!/usr/bin/python3
"""
   script that lists all City objects from the database hbtn_0e_101_usa

    - Your script should take 3 arguments:
      mysql username, mysql password and database name
    - Script should connect to a MySQL server
      running on localhost at port 3306
    - Must use the state relationship to access
      to the State object linked to the City object
    - Results must be sorted in ascending order by cities.id
"""

import sys

from relationship_state import Base
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
    cities = session.query(City).all()

    # print states and all cities connected
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    session.close()
