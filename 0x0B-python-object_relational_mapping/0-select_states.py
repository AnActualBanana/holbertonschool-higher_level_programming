#!/usr/bin/python3
"""
Script that will list all states
"""

import MySQLdb


if __name__ == "__main__":
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states")
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
