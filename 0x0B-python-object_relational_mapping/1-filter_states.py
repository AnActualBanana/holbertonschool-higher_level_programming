#!/usr/bin/python3
"""
lists all states with a nambe starting with N
"""

import MySQLdb


if __name__ == "__main__":
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states")
    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)

    cursor.close()
    db.close()
