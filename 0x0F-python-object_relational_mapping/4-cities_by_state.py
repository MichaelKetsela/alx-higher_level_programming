#!/usr/bin/python3
"""
lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3], charset="utf8")
    db_cur = db_connect.cursor()
    db_cur.execute("SELECT  cities.id, cities.name, states.name FROM cities \
    JOIN  states ON cities.state_id = states.id ORDER BY cities.id")
    [print(row) for row in db_cur.fetchall()]
    db_cur.close()
    db_connect.close()
