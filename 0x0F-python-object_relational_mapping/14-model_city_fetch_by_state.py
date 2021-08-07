#!/usr/bin/python3
""" this module selects and show the registers in tha table states
    of the given database using ORM
"""
from sys import argv
from model_state import Base, State
# tates2 = __import__('model_state').State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    # get the connection parameters
    db_user = argv[1]
    db_pass = argv[2]
    db_name = argv[3]
    db_address = "localhost"

    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
        db_user,
        db_pass,
        db_address,
        db_name),
        pool_pre_ping=True)

    # Create and instance the sesion
    Session = sessionmaker(bind=engine)
    session = Session()

    # Executes the query
    results = session.query(State.name, City.id, City.name) \
        .filter(State.id == City.state_id).order_by(City.id)

    # show the results
    for row in results:
        print('{}: ({}) {}'.format(row[0], row[1], row[2]))

    # Closes the sesion
    session.close_all()
