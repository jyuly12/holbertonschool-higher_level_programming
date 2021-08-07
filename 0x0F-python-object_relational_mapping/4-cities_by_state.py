#!/usr/bin/python3
"""
lists all states with a name starting with N (upper N) from the database.
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
    FROM cities, states WHERE cities.state_id = states.id
    ORDER BY cities.id ASC""")
    rows = cursor.fetchall()
    for item in rows:
        print(item)
    cursor.close()
    db.close()
