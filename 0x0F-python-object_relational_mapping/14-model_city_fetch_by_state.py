#!/usr/bin/python3
"""Start link class to table in database
"""
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    printer = 'mysql+mysqldb://{}:{}@localhost/{}'
    engine = create_engine(printer.format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State, City).filter(City.state_id ==
                                              State.id).order_by(City.id).all()
    for state, city in query:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
