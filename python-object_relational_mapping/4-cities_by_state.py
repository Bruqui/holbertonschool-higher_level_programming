#!/usr/bin/python3

"""
This module connects to a MySQL database and retrieves all cities
along with their corresponding states from the specified database.
The results are sorted in ascending order by the city ID and displayed
in a specific format.
"""

import MySQLdb
import sys


def main():
    """
    The main function that executes the logic to connect to the MySQL
    database and retrieve cities along with their associated state names.
    It takes three command-line arguments: MySQL username, password,
    and database name. The function connects to the database, executes
    a SQL query to retrieve city and state data, and prints each city
    with its ID, name, and state name, sorted by city ID in ascending order.
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

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    cursor.execute(query)

    results = cursor.fetchall()

    for row in results:
        print(row)
    
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
