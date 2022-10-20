#!/usr/bin/python3
"""
script that lists all states
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    db = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'\
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(db)
    sesh = sessionmaker(bind=db)

    for row in dbsession().query(State).order_by(State.id):
        print("{}: {}".format(row.id, row.name))

    sesh().close
