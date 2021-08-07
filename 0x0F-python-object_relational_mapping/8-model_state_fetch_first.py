#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    printer = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(printer.format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = session.query(State).order_by(State.id).first()
    if (state_name is None):
        print("Nothing")
    else:
        print("{}: {}".format(state_name.id, state_name.name))
    session.close()
