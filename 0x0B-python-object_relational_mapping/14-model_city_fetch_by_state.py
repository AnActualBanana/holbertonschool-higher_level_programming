#!/usr/bin/python3
"""
Lists all cities
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                             .format(argv[1], argv[2], argv[3]),
                             pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    dbs = session()

    city_search = dbs.query(State, City).filter(
        State.id == City.state_id).all()
    for state_item, city_item in city_search:
        print("{}: ({}) {}".format(state_item.name,
              city_item.id, city_item.name))

    session().close
