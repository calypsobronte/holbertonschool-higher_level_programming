#!/usr/bin/python3
from model_state import State, Base
from model_city import City
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)
    state_result = session.query(City, State)\
                          .filter(City.state_id == State.id)\
                          .order_by(City.id.asc())
    for city, state in state_result:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
