#!/usr/bin/python3
"""
Lists the first state.
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    db = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                             .format(argv[1], argv[2], argv[3]),
                             pool_pre_ping=True)

    Base.metadata.create_all(db)
    sesh = sessionmaker(bind=db)

    try:
        print("{}: {}".format(sesh().query(State).first().id,
                              sesh().query(State).first().name))

    except Exception:
        print("Nothing")

    sesh().close