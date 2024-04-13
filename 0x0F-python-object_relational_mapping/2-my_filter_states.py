#!/usr/bin/python3
""" a script that takes in an argument and displays all
values in the states table of hbtn_0e_0_usa where
name matches the argument. """

import MySQLdb
import sys

if __name__ == "__name__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    state_name = sys.argv[4]
    cur.execute(query, (state_name,))
    results = cur.fetchall()
    for row in results:
        print(row)
