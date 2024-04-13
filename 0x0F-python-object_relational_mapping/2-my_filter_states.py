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
    cur.execute("""SELECT * FROM states
                    WHERE name LIKE BINARY '{}' ORDER BY id ASC""".format(sys.argv[4]).strip("'"))
    results = cur.fetchall()
    for row in results:
        print(row)
