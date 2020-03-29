#!/usr/bin/python3
from model_state import State, Base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    session = Session(engine)
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()
    print(new_state.id)
