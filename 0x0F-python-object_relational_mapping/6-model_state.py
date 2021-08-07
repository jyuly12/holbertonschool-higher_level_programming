#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    printer = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(printer.format(sys.argv[1],
                                          sys.argv[2],
                                          sys.argv[3]))
    Base.metadata.create_all(engine)
