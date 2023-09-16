#!/usr/bin/python3

"""
  script that takes in the name of a state as an argument,
  and lists all cities of that state, using the database hbtn_0e_4_usa.
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
    cities = set()  # a set to hold all the city names
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=f"{args[1]}", passwd=f"{args[2]}",
                           db=f"{args[3]}", charset="utf8")
    cur = conn.cursor()
    # list all cities in my database
    cur.execute('SELECT cities.name FROM cities INNER JOIN states\
                ON\
                cities.state_id\
                = ( SELECT id FROM states WHERE states.name = %s )\
                ORDER BY cities.id ASC', (args[4], ))
    query_rows = cur.fetchall()
    # add city names to set
    [cities.add(city[0]) for city in query_rows]
    length = len(cities) - 1  # length of cities set
    # print the city names
    for idx, city in enumerate(cities):
        if idx < length:
            print(city + ', ', end="")
        else:
            print(city)
    cur.close()
    conn.close()
