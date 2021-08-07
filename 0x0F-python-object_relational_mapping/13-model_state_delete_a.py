#!/usr/bin/python3
""" this module selects and show the registers in tha table states
    of the given database using ORM
"""
from sys import argv
from model_state import Base, State
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

    # get the instance and edit it
    states_to_remove = session.query(State) \
        .filter(State.name.like("%a%")) \
        .delete(synchronize_session=False)

    # Executes the query
    session.commit()

    # Closes the sesion
    session.close_all()
