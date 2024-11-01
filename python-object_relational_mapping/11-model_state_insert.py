#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa and
prints the id of the new state after insertion.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """
    Connects to the MySQL database, adds a new State object with the
    name "Louisiana", commits the transaction, and prints the new state's id.
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

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()


if __name__ == "__main__":
    main()
