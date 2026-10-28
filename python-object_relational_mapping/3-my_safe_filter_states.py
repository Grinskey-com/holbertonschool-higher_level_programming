#!/usr/bin/python3
"""lists all states matching the name given as an argument, safely"""
import sys
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER by id ASC",
                (sys.argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
