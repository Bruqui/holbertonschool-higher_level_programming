#!/usr/bin/python3

"""
This module connects to a MySQL database and retrieves all states
whose names start with an uppercase 'N' from the specified database.
The results are sorted in ascending order by their IDs and displayed
in a specific format.
"""

import MySQLdb
import sys


def main():
    """
    The main function that executes the logic to connect to the MySQL
    database and retrieve states starting with 'N'. It takes three
    command-line arguments: MySQL username, password, and database name.
    It connects to the database, executes a SQL query, and prints all
    matching states sorted by their ID in ascending order.
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

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    results = cursor.fetchall()

    for row in results:
        if ('N' in row[1]):
            print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
