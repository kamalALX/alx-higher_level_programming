#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
But this time, it is safe from MySQL injections!
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states""")
    result = cur.fetchall()
    for state in result:
        if state[1] == sys.argv[4]:
            print(state)
