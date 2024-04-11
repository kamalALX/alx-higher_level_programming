#!/usr/bin/python3
"""  """
import sys
import MySQLdb

if __name__ == "__main__" : 
    args = sys.argv

    db = MySQLdb.connect(user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    states = cur.fetchall()
    for state in states:
        print("{}".format(state))
