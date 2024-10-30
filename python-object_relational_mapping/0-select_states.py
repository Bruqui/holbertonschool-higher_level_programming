#!/usr/bin/python3

"""
This module connects to a MySQL database and retrieves all states
from the specified database. The states are sorted in ascending order
by their IDs and displayed in a specific format.
"""

import MySQLdb
import sys


def main():
    """
    The main function that executes the logic to connect to the MySQL
    database and retrieve states. It takes three command-line arguments:
    MySQL username, password, and database name. It connects to the
    database and executes a SQL query to select and print all states
    sorted by their ID in ascending order.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    results = cursor.fetchall()

    for row in results:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
