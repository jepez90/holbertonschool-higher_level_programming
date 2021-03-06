#!/usr/bin/python3
""" definition of state class """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """ definition of state class """
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, autoincrement=True,
                primary_key=True)
    name = Column(String(128), nullable=False)
