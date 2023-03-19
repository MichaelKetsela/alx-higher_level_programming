#!/usr/bin/python3
"""
takes in the name of a state as an argument and
lists all cities of that state, using the database
hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db_connect = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3], charset="utf8")
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELEECT cities.name FROM cities \
    JOIN states ON citites.state_id = states.id WHERE states.name LIKE %s\
    ORDER BY cities.id", (argv[4]))
    [print(", ".join(row[0] for row in db_cursor.fetchall()))]
    db_cursor.close()
    db_connect.close()
