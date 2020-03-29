#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database_name = argv[3]

    connect_db = MySQLdb.connect(host="localhost",
                                 port=3306,
                                 user=username,
                                 passwd=password,
                                 db=database_name)

    cursor = connect_db.cursor()
    cursor.execute("SELECT * FROM states WHERE BINARY name=%s\
                   ORDER BY id ASC", (argv[4],))
    return_list = cursor.fetchall()
    for row in return_list:
        print(row)
    cursor.close()
    connect_db.close()
