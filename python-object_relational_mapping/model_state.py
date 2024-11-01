#!/usr/bin/python3
"""
Defines the State class and a Base instance to map to the states table in a MySQL database.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class definition to map to the states table in the MySQL database.

    Attributes:
        id (int): Auto-generated, unique integer, primary key, non-null.
        name (str): String column with max 128 characters, non-null.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
