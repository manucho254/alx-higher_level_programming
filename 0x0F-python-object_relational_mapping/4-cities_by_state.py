#!/usr/bin/python3

"""
  Script that lists all cities from the database hbtn_0e_0_usa:
    - Script takes 3 arguments: mysql username, mysql password and
      database name.
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server running,
      on localhost at port 3306
    - Results must be sorted in ascending order by cities.id
"""

import sys
import MySQLdb


if __name__ == "__main__":
    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=f"{args[1]}", passwd=f"{args[2]}",
                           db=f"{args[3]}", charset="utf8")
    cur = conn.cursor()
    # list all cities in my database
    cur.execute("SELECT cities.id, cities.name,\
                states.name FROM cities INNER JOIN states ON\
                states.id=cities.state_id ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
