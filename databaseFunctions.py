#!/usr/bin/python3  

import mysql.connector

dbcusor = database.cursor()

def passwordCheck(dbcusor, Username, UserPassword):
    try:
        database = mysql.connector.connect(
                host ="localhost", 
                user = Username, 
                password = UserPassword
                database="passwordDB"
        )
    except:
        print("Incorrect Entry")
   else:
       return True

def searchDatabase():
    
