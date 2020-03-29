#!/usr/bin/python3
from model_state import State, Base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    session = Session(engine)
    update_state = session.query(State).filter_by(id=2).first()
    update_state.name = "New Mexico"
    session.commit()
