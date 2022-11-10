#!/usr/bin/python3  

from time import sleep
import mysql.connector
import getpass

#usernameEntry = ""
#passwordEntry = ""

def passwordCheck():
    check = False
    while(check == False):
        global usernameEntry 
        usernameEntry = input("Enter your Username: ") 
        global passwordEntry
        passwordEntry = getpass.getpass(prompt='Enter Password: ')
        try:
            mydb = mysql.connector.connect(
                    host ='localhost', 
                    user = usernameEntry, 
                    password = passwordEntry
            )
            #dbcursor = mydb.cursor()
            #dbcursor.execute("SHOW DATABASES")

            #for x in dbcursor:
            #    print(x)
        except:
            print("Incorrect Entry")
        else: 
            check = True
    return True

def checkDatabase():
        database = mysql.connector.connect(
                host ='localhost', 
                user = usernameEntry, 
                password = passwordEntry,
        )
        dbcursor = database.cursor()
        try:
            dbcursor.execute("SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME='passwords'")
            for x in dbcursor:
                entries = x
            if len(entries) == 1:
                print("Database Found")
        except:
            print("Password Manager database not found. creating now...")
            dbcursor.execute("CREATE DATABASE passwords") 
            database = mysql.connector.connect(
                    host ='localhost', 
                    user = usernameEntry, 
                    password = passwordEntry,
                    database = 'passwords'
            )
            dbcursor = database.cursor()
            dbcursor.execute("CREATE TABLE entries (Account varchar(255), password varchar(255))")
            print("Database Created")
        finally:
            sleep(2)

def addPassword():
    newName = input("Enter the name of the new account: ")
    newPassword = getpass.getpass(prompt='Enter the password of the new account: ')
    confirmPassword = getpass.getpass(prompt='Confirm new password: ')
    while(newPassword != confirmPassword):
        confirm = getpass.getpass(prompt='Two different passwords entered. Please reconfirm password: ') 
    command = "INSERT INTO entries (Account, Password) VALUES (%s, %s)"
    entry = (newName, newPassword)
    database = mysql.connector.connect(
            host ='localhost', 
            user = usernameEntry, 
            password = passwordEntry,
            database = 'passwords'
    )
    dbcursor = database.cursor()    
    dbcursor.execute(command, entry)
    database.commit()
    
def deleteSelectedPassword():
    database = mysql.connector.connect(
            host ='localhost', 
            user = usernameEntry, 
            password = passwordEntry,
            database = 'passwords'
   )
    dbcursor = database.cursor()
    print("Account |  Password")
    print("-------------------")
    dbcursor.execute("SELECT * FROM entries")
    for x in dbcursor:
        print (x)
    while(True):
        selection = input("Enter the name of the account you would like to delete: ")
        try:
            selectionCommand = """SELECT * FROM entries where Account = '%s'""" % (selection)
            dbcursor.execute(selectionCommand)
            showSelection = dbcursor.fetchone()
            print("Selected: ", end=' ')
            for n in showSelection:
                print(n + " |", end=' ')
            break
        except:
            print("Selection not found in database. Please enter again: ")

    check = input("\nAre you sure you want to delete this account entry? [Y/n] ")
    if (check == 'Y' or check == 'y'):
        deleteCommand = """DELETE FROM entries WHERE Account = '%s'""" % (selection)
        dbcursor.execute(deleteCommand) 
        database.commit()
        print("Account deleted.", end = ' ')
    elif (check == 'N' or check == 'n'):
        print("Account deletion suspended.", end = ' ' )


