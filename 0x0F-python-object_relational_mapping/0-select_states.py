#!/usr/bin/python3
"""
This this will display all the states in the database.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    This is used to access the database and look for the states.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
