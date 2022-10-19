#!/usr/bin/python3
"""
Lists all citires and states of database where name matches arguments
"""

import MySQLdb

if __name__ == "__main__":
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities JOIN states ON cities.state_id = states.id")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
