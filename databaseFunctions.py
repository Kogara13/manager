#!/usr/bin/python3  

import mysql.connector





UserPassword = input("enter the password: ")

def passwordCheck(UserPassword):
    try:
        mydb = mysql.connector.connect(
                host ='localhost', 
                user = 'root', 
                password = "ManagerProject",
        )
        dbcursor = mydb.cursor()
        dbcursor.execute("SHOW DATABASES")

        for x in dbcursor:
            print(x)
    except:
        print("Incorrect Entry")


passwordCheck(UserPassword)
