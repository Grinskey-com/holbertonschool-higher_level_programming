#!/usr/bin/python3
"""lists all states matching the name given as an argument"""
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
    cur.execute(
        "SELECT cities.id, cities.name, state.name"
        "FROM cities JOIN states ON cities.state._id = states.id"
        "ORDER BY cities.id ASC"
    
    )
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
