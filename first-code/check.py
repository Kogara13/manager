#!/usr/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='ManagerProject',
        database='passwords'
)

dbcursor = mydb.cursor()

query1 ="SELECT COUNT(Account) FROM entries WHERE Account='python'"
dbcursor.execute(query1)
cnt=dbcursor.fetchone()

print(cnt)

for x in cnt:
    print(x) 

print(type(x))
