#!/usr/bin/python3

import mysql.connector

mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='ManagerProject'
)

dbcursor = mydb.cursor()

try:
    dbcursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME='test'")
    for x in dbcursor:
        entries = x
    if len(entries) == 1:
        print("database exists")
except:
    print("doen't exist. creating now")
    dbcursor.execute("CREATE DATABASE test")
    mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='ManagerProject',
            database='test'
    )
    dbcursor = mydb.cursor()
    dbcursor.execute("CREATE TABLE testTable (Account varchar(255), password varchar(255))")
    print("Database created")

name="testName"


