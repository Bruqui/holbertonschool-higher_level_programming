#!/usr/bin/python3

"""
This module connects to a MySQL database and retrieves all cities
for a given state from the specified database. The results are
sorted in ascending order by city ID and displayed as a comma-separated
list of city names.
"""

import MySQLdb
import sys

def main():
    """
    The main function that executes the logic to connect to the MySQL
    database and retrieve cities for a given state. It takes four command-line
    arguments: MySQL username, password, database name, and state name.
    The function connects to the database, executes a SQL query to
    retrieve city data, and prints each city name in a comma-separated format.
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

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))

    results = cursor.fetchall()

    city_names = [row[0] for row in results]
    print(", ".join(city_names))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
