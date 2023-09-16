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
    # # a list to hold all the city names
    cities = []
    for city in query_rows:
        if city[0] not in cities:
            cities.append(city[0])

    if len(cities) == 0:
        print()
        sys.exit()
    length = len(cities) - 1  # length of cities list
    # print the city names
    for idx, city in enumerate(cities):
        if idx < length:
            print(city + ', ', end="")
        else:
            print(city)
    cur.close()
    conn.close()
