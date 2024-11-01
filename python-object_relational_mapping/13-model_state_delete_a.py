#!/usr/bin/python3
"""
Deletes all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Connects to the MySQL database, finds State objects with 
    names containing 'a', deletes them, and commits the changes.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password,
                                                    database),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states_to_delete = session.query(State).filter(State.name.like(
        '%a%')).all()
    
    for state in states_to_delete:
        session.delete(state)

    session.commit()

    session.close()


if __name__ == "__main__":
    main()
