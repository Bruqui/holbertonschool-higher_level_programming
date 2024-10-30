#!/usr/bin/python3

"""
This module connects to a MySQL database and retrieves all states
from the specified database where the state name matches the user input.
The results are sorted in ascending order by their IDs and displayed
in a specific format.
"""


import MySQLdb
import sys


def main():
    """
    The main function that executes the logic to connect to the MySQL
    database and retrieve states matching the given name. It takes four
    command-line arguments: MySQL username, password, database name,
    and state name to search. It connects to the database, executes a
    SQL query, and prints all matching states sorted by their ID in
    ascending order.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    results = cursor.fetchall()

    for row in results:
        print(row)
    
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
