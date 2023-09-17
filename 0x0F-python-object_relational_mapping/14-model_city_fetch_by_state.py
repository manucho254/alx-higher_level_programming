#!/usr/bin/python3
"""
   Script that prints all City objects from the database hbtn_0e_14_usa:

   - Script should take 3 arguments:
     mysql username, mysql password and database name
   - Import State and Base from model_state
     - from model_state import Base, State.
   - Script should connect to a MySQL server
     running on localhost at port 3306
   - Results must be sorted in ascending order by cities.id
   - Results must be display as they are in
     the example below (<state name>: (<city id>) <city name>)
"""
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State
from model_city import City

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

    # get all states
    cities = session.query(City).order_by(City.id).all()

    # print all states
    for city in cities:
        # get state with state id in city
        state = session.query(State).filter(State.id == city.state_id).first()
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
