#!/usr/bin/python3
from sys import argv
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session2 = session()
    new_state = State(name="California")
    session2.add(new_state)
    session2.commit()
    new_city = City(name="San Francisco", state_id=new_state.id)
    session2.add(new_city)
    session2.commit()
    session2.close()
