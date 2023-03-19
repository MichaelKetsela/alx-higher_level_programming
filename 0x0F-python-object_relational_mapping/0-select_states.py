#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_connect = MySQLdb.connect(host="localhost", user=argv[1],
                                 passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    row = db_cursor.fetchall()
    for r in row:
        print(r)
    db_cursor.close()
    db_connect.close()
