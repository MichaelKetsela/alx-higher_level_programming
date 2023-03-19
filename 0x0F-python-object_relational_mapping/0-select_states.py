#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    Access to the database and get the states from
    the database.
    """
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                passwd=argv[2], db=argv[3], charset="utf8")
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states ORDER BY id ASC")
    [print(row) for row in db_cursor.fetchall()]
    db_cursor.close()
    db_connect.close()
