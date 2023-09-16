#!/usr/bin/python3

"""
   script that lists all states with a name starting with N (upper N),
   from the database hbtn_0e_0_usa:
    - Script takes 3 arguments: mysql username, mysql password and
      database name.
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server running,
      on localhost at port 3306
    - Results must be sorted in ascending order by states.id
"""

import sys
import MySQLdb


if __name__ == "__main__":
    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=f"{args[1]}", passwd=f"{args[2]}",
                           db=f"{args[3]}", charset="utf8")
    cur = conn.cursor()
    # list all states in my database
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
