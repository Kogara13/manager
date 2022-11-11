#!/usr/bin/python3

import mysql.connector

name = input("Enter test: ")
mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='ManagerProject',
        database='test'
)

dbcursor = mydb.cursor()

try:
    command = """SELECT * FROM testTable WHERE Account='%s'""" % (name)

    dbcursor.execute(command)   
    for x in dbcursor:
        entries = x
    if len(entries) == 2:
        print("name already exists")
except:
    print("doen't exist.")



