#!/usr/bin/python3
"""
list all states with a name starting with N(upper N)
from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3], charset="utf8")
    cursor = db_connect.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    [print(row) for row in cursor.fetchall() if row[1][0] == "N"]
    cursor.close()
    db_connect.close()
