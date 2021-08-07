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
    sql = """SELECT cities.name FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = %s ORDER BY cities.id ASC"""
    cursor.execute(sql, (argv[4],))
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()
