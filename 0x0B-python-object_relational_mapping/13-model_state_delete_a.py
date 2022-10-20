#!/usr/bin/python3
"""
deletes all states containing the letter 'a'
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                             .format(argv[1], argv[2], argv[3]),
                             pool_pre_ping=True)

    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    dbs = session()

    delm = dbs.query(State).filter(State.name.like('%a%'))
    for row in delm:
        dbs.delete(row)
    dbs.commit()

    session()