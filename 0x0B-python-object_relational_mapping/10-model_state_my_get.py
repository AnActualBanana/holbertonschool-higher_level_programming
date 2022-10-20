#!/usr/bin/python3
"""
Lists state as argument.
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
        print(sesh().query(State).filter(
            State.name == argv[4])[0].id)

    except Exception:
        print("Not found")

    sesh().close