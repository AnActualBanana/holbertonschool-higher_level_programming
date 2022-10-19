#!/usr/bin/python3
"""
script that lists all cities of the state given as argument
"""

import MySQLdb

if __name__ == "__main__":
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=argv[1], passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.name FROM cities JOIN states ON cities.state_id\
= states.id WHERE states.name LIKE %s ORDER BY cities.id", (argv[4],))
    print(", ".join(rows[0] for rows in cursor.fetchall()))

    cursor.close()
    db.close()
