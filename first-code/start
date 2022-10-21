#!/usr/bin/pyton3

import mysql.connector
import os
import time
import string

#Determine "clear terminal" command based on operating system
if os.name == 'nt':
    terminal_clear = 'cls'
else:
    terminal_clear = 'clear'

#User Enters their username and password
Username = input("Enter your username: ")
userPassword =  input("Enter your password: ")

#Initial connection to MySQL
database = mysql.connector.connect(
        host="localhost"
        user = Username
        password = userPassword
)


dbcusor = database.cursor()

#Check to see if database already exists
databaseCheck()

#Updated MySQL connection
database = mysql.connector.connect(
        host="localhost"
        user=Username
        password=userPassword
        database="passwordDB"
)

#Opens Main Menu (Other functions stem from this one)
mainMenu(terminalClear)

#Function to check if database already exists and create one if it does not
def databaseCheck():
        dbcursor.execute("SHOWDATABASES")
        if len(dbcursor) == 0: 
            echo("Database does not exist. Creating now")
            dbcursor.execute("CREATE DATABASE passwordDB")
            dbcursor.execute("CREATE TABLE passwords (Account VARCHAR(255) PRIMARY KEY, Password VARCHAR(255))")
        else: 
            echo("Database found")

#Function to display main menu
def mainMenu(termnial_clear):
    while(True): 
             echo(" 1. Add Password")
             echo(" 2. Delete Password")
             echo(" 3. Edit Password")
             echo(" 4. Generate Password")
             selection = input("Enter selection from above")
             if selection == 1: 
                 addPassword(terminalClear)
            elif selection == 2: 
                deletePassword(terminalClear)
            elif selection == 3: 
                editPassword(terminalClear)
            elif selection == 4: 
                generatePassword(terminalClear)
            else: 
                echo("Invalid Entry")

#Function to add new password to database
def addPassword(terminalClear):
        os.system(terminalClear)
        name = input("Account of new password: ")
        password = input("Enter new password: ")
        command = "INSERT INTO passwords (Account, Password) VALUES (%s, %s)"
        entry = (name, password)
        dbcursor.execute(command, entry)

        database.commit()
        echo("New Password Entered. Returning to Main Menu...")
        time.sleep(3)
        os.system(terminalClear) 

#Function to delete password in database
def deletePassword(terminalClear):
    os.system(terminalClear)
    dbcursor.execute("SELECT Account FROM passwords")
    name = input("Which password should be deleted?: ")
    command = "DELETE FROM passwords WHERE Account = %s"
    dbcursor.execute(command, name)

    database.commit()
    echo("Password Deleted. Returning to Main Menu...")
    time.sleep(3)
    os.system(terminalClear)

#Function to edit existing password in database
def editPassword(terinalClear): 
    os.system(terminalClear)
    dbcursor.execute("SELECT Account FROM passwords")
    name = input("Which password should be edited?: ")
    newPassword = input("Enter new password: ")
    command = "UPDATE passwords SET Password = %s WHERE Account = %s"
    values = (name, newPassword)
    dbcursor.execute(command, values)

    database.commit()
    echo("Password changed. Returning to Main Menu...")
    time.sleep(3)
    os.system(terminalClear)

#Function to generate a random string of ascii characters based on inputed length
def generatePassword(terminalClear):
    os.system(terminalClear)
    length = input("Enter the character length of the password: ")
    availableChars = string.ascii_letters + string.punctuation
    
    newPassword = ''
    for x in range(length)
       newPassword += random.choice(availableChars)
    echo("New password is: " + newPassword)





