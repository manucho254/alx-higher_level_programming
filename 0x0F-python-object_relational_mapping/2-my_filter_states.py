#!/usr/bin/python3

"""
  script that takes in an argument and displays,
  all values in the states table of hbtn_0e_0_usa
  where name matches the argument.
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
    query = "SELECT * FROM states WHERE BINARY name = '{}'\
             ORDER BY id ASC".format(args[4])
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
