#!/usr/bin/python3
""" sefinition of City class """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.schema import ForeignKey
from model_state import Base, State


class City(Base):
    """ sefinition of City class"""
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement="auto")
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'), nullable=False)
