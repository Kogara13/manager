#!/usr/bin/python3  

from time import sleep
import mysql.connector
import getpass
import random
import string

"""
-------------------------------------------------------------
Edits to function to comply with unit testing:
1. inputs have been replaced with functions parameters
2. Password to database has been hardcoded into the function
3. Return value set to test that entry was added to database
-------------------------------------------------------------
"""

def addPassword(newName, newPassword, confirmPassword): 
    database = mysql.connector.connect(
            host ='localhost', 
            user = 'root', 
            password = 'ManagerProject',
            database = 'passwords'
    )
    
    dbcursor = database.cursor()    
    
    while(True):
        #newName = input("Enter the name of the new account: ")
        if newName == "":
            print("Empty String. Please enter a name")
            continue
        checkQuery ="""SELECT COUNT(Account) FROM entries WHERE Account='%s'""" % (newName) 
        dbcursor.execute(checkQuery)
        count = dbcursor.fetchone()
        for x in count:
            entries = x
        if entries == 1:
            print("Name already exists") 
            continue
        else:
            break
    
    #newPassword = getpass.getpass(prompt='Enter the password of the new account: ')
    errorCounter = 3
    while(True):
        #confirmPassword = getpass.getpass(prompt='Confirm new password: ')
        if newPassword != confirmPassword:
            errorCounter = errorCounter - 1
            if errorCounter > 0:
                print('Two different passwords entered. Please reconfirm password (Process will abort after ' + str(errorCounter) + ' more failed attempts)') 
            else:
                print("Too many failed attempts. ", end = ' ')
                break
        else:
            command = "INSERT INTO entries (Account, Password) VALUES (%s, %s)"
            entry = (newName, newPassword)
            dbcursor.execute(command, entry)
            database.commit()
            print("Password entered into database. ", end = ' ')
            break
    
    entryCommand = """SELECT * FROM entries WHERE Account='%s'""" % (newName)
    dbcursor.execute(entryCommand)
    output = dbcursor.fetchone()
    return output

    
"""
Edits to function to comply with unit testing:
1. User Inputted variables replaced with function parameters
2. Password to Database hardcoded into function
3. Return values set to test whether an entry has been deleted from the database or not
"""

def deleteSelectedPassword(selection, check):
    database = mysql.connector.connect(
            host ='localhost', 
            user = 'root', 
            password = 'ManagerProject',
            database = 'passwords'
   )
    dbcursor = database.cursor()
    print("Account |  Password")
    print("-------------------")
    dbcursor.execute("SELECT * FROM entries")
    for x in dbcursor:
        print (x)
    while(True):
        #selection = input("Enter the name of the account you would like to delete: ")
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

    #check = input("\nAre you sure you want to delete this account entry? [Y/n] ")
    if (check == 'Y' or check == 'y'):
        deleteCommand = """DELETE FROM entries WHERE Account = '%s'""" % (selection)
        dbcursor.execute(deleteCommand) 
        database.commit()
        print("Account deleted.", end = ' ')
    elif (check == 'N' or check == 'n'):
        print("Account deletion suspended.", end = ' ' )
    
    if (check == 'Y' or check == 'y'):
        checkDeletion ="""SELECT COUNT(Account) FROM entries WHERE Account='%s'""" % (selection) 
        dbcursor.execute(checkDeletion)
        noEntry = dbcursor.fetchone()
        return noEntry
    elif (check == 'N' or check == 'n'):
        checkDeletion ="""SELECT COUNT(Account) FROM entries WHERE Account='%s'""" % (selection) 
        dbcursor.execute(checkDeletion)
        remainingEntry = dbcursor.fetchone()
        return remainingEntry

        
