#!/usr/bin/python3
"""
Contains the class definition of a City and an instance
Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class City(Base):
    """
    Defines City class
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
