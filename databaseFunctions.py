#!/usr/bin/python3  

#import dependencies
from time import sleep
import mysql.connector
import getpass
import random
import string

#Called in main() to have the user enter the master password of the database
def passwordCheck():
    check = False
    passwordCheck = 2
    while(check == False):
        global passwordEntry #passwordEntry is later used throughout the program
        passwordEntry = getpass.getpass(prompt='Enter Master Password: ')
        """
        #Try to connect to the database using the entered password. If this results in an error, 
        the exception will run and the function will loop through the try block 2 more times. 
        """
        try:
            database = mysql.connector.connect(
                    host ='localhost', 
                    user = 'root', 
                    password = passwordEntry
            )
        except:
            if passwordCheck > 0:
                print("Incorrect Entry. " + str(passwordCheck) + " attempts remaining")
                passwordCheck = passwordCheck - 1
            else:
                print("Incorrect Entry. Access Denied")
                break
        else: 
            check = True
    return check

#Function to check that the database and table being written to exist. If not, they will be created
def checkDatabase():
        database = mysql.connector.connect(
                host ='localhost', 
                user = 'root', 
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
                    user = 'root', 
                    password = passwordEntry,
                    database = 'passwords'
            )
            dbcursor = database.cursor()
            dbcursor.execute("CREATE TABLE entries (Account varchar(255), password varchar(255))")
            print("Database Created")
        finally:
            sleep(2)


#Throughout these functions, while(Ture) loops are used to handle input errors by the user


#Connect to database to add password
def addPassword(): 
    database = mysql.connector.connect(
            host ='localhost', 
            user = 'root', 
            password = passwordEntry,
            database = 'passwords'
    )
    
    dbcursor = database.cursor()    
    
    while(True):
        newName = input("Enter the name of the new account: ")
        if newName == "":
            print("Empty string entered. ", end='')
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
    
    newPassword = getpass.getpass(prompt='Enter the password of the new account: ')
    errorCounter = 3
    while(True):    
        if newPassword == "":
            print("<<<<<<<<WARNING: PASSWORD LEFT BLANK!>>>>>>>>")
        confirmPassword = getpass.getpass(prompt='Confirm new password: ')
        if newPassword != confirmPassword:
            errorCounter = errorCounter - 1
            if errorCounter > 0:
                print('Two different passwords entered. Please reconfirm password (Process will abort after ' + str(errorCounter) + ' more failed attempts)') 
            else:
                print("Too many failed attempts. ", end = ' ')
                break
        else:
            command = "INSERT INTO entries (Account, Password) VALUES (LCASE(%s), %s)"
            entry = (newName, newPassword)
            dbcursor.execute(command, entry)
            database.commit()
            print("Password entered into database. ", end = '')
            break
    
def deleteSelectedPassword():
    database = mysql.connector.connect(
            host ='localhost', 
            user = 'root', 
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

def searchDatabase():
    database = mysql.connector.connect(
            host ='localhost', 
            user = 'root', 
            password = passwordEntry,
            database = 'passwords'
   )
    dbcursor = database.cursor()
    while(True):
            search = input("Enter the name of the Account: ")
            countCommand = """SELECT COUNT(Account) FROM entries WHERE Account='%s' OR Account=LCASE('%s')""" % (search, search)
            dbcursor.execute(countCommand)
            numOfResults = dbcursor.fetchone()
            for x in numOfResults:
                results = x
            if results < 1:
                found = False
                notFound = input("Entry not found. Press Enter to retry or Q to quit: ")
                if (notFound == 'Q' or notFound == 'q'):
                    break
                else:
                    continue
            else:
                found = True
                break
    if (found):
        searchCommand = """SELECT * FROM entries WHERE Account='%s' OR Account=LCASE('%s')""" % (search, search)
        dbcursor.execute(searchCommand)
        print("Account | Password")
        print("------------------")
        searchList = []
        count = 1
        for x in dbcursor:
            print(str(count) + ". " + str(x))
            searchList.append(x[1])
            count += 1

    while(found):
        try:
            selectPassword = int(input("Enter the number of the desired password: "))
            chosenPassword = searchList[selectPassword - 1]
        except:
            print("Invalid choice. Please reenter...")
            continue
        else:
            print("Password of Account: " + chosenPassword)
            exit = input("You may copy the password to your clipboard (Ctrl + Shift + V). Press Enter to return to the Main Menu.")
            break
    
def editSelection(): 
    database = mysql.connector.connect(
            host ='localhost', 
            user = 'root', 
            password = passwordEntry,
            database = 'passwords'
   )
    dbcursor = database.cursor()
    print("Account |  Password")
    print("-------------------")
    dbcursor.execute("SELECT * FROM entries")
    for x in dbcursor:
        print(x)
    while(True):
        selection = input("Enter the name of the account you would like to edit: ")       
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
        
    print("\n1. Name\n2. Password\n")
    nameOrPassword = input("Would you like to edit the name(1) or password(2) of this entry?: ") 
    while(True):
        if nameOrPassword == '1':
            newName = input("Enter the new name for this entry: ")
            confirmNewName = input("Are you sure you want to change the name to " + newName + "? [Y/n]: ")
            if (confirmNewName == 'Y' or confirmNewName == 'y'):
                #kcode to edit database
                editNameCommand = """UPDATE entries SET Account = '%s' Where Account = '%s'""" % (newName, selection)
                dbcursor.execute(editNameCommand) 
                database.commit()
                print("edit complete")
                break
            elif (confirmNewName == 'N' or confirmNewName == 'n'):
                print("Account edit suspended.", end = ' ')        
                break
        elif (nameOrPassword == '2'):
            while(True):
                newPassword = getpass.getpass(prompt="Enter the new password for this entry: ")
                confirmNewPassword = getpass.getpass(prompt="Confirm new password (Type [N,n] to cancel): ")
                if (confirmNewPassword == 'N' or confirmNewPassword == 'n'):
                    print("Password edit suspended.", end = ' ')
                    break
                elif (confirmNewPassword == newPassword):
                    #code to edit database
                    editPasswordCommand = """UPDATE entries SET Password = '%s' Where Account = '%s'""" % (newPassword, selection)
                    dbcursor.execute(editPasswordCommand) 
                    database.commit()
                    print("Password edit complete.", end = ' ')
                    break
                elif (confirmNewPassword != newPassword): 
                    print("Two different passwords entered. Please reconfirm password") 
            break
        else: 
            print("incorrect entry")

def generatePassword():
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    symbols = "~!@#$%^&*_-+=<>"
    while(True):
        try:
            length = int(input("Enter the length of the generated password: "))
        except:
            print("Enter an integer value")
        if (length < 10):
            print("Password must at least be 10 characters long")
            continue
        elif (length > 32):
            print("Password must be no more than 32 characters long")
            continue
        else:
            break
    while(True):
        symbolsChoice = input("Include symbols (~!@#$%^&*_-+=<>) as well as alphanumeric characters? [Y/n]:")  
        if symbolsChoice == 'Y' or symbolsChoice == 'y':
            generatedPassword = ''.join(random.choice(characters + symbols) for n in range(length))
            break
        elif symbolsChoice == 'N' or symbolsChoice == 'n':
            generatedPassword = ''.join(random.choice(characters) for n in range(length))
            break
        else:
            print("Invalid input")
    print("Geniferated Password: " + generatedPassword)
    database = mysql.connector.connect(
            host ='localhost', 
            user = 'root', 
            password = passwordEntry,
            database = 'passwords'
    )
    dbcursor = database.cursor()
    print("1. Edit existing entry\n2. Create new entry")
    editOrCreate = input("Would you like to add this to an existing entry to create a new one with it?")
    if editOrCreate == '1':
        print("Account |  Password")
        print("-------------------")
        dbcursor.execute("SELECT * FROM entries")
        for x in dbcursor:
            print(x)
        while(True):
            selection = input("Enter the name of the account you would like to edit: ")       
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
        while(True):
            confirmNewPassword = input("Confirm change of password [Y/n]: ")
            if (confirmNewPassword == 'N' or confirmNewPassword == 'n'):
                print("Password edit suspended.", end = ' ')
                break
            elif (confirmNewPassword == 'Y' or confirmNewPassword == 'y'):
                editPasswordCommand = """UPDATE entries SET Password = '%s' Where Account = '%s'""" % (generatedPassword, selection)
                dbcursor.execute(editPasswordCommand) 
                database.commit()
                print("Password edit complete.", end = ' ')
                break
            else: 
                print("Invalid input")
    elif editOrCreate == '2':        
        newName = input("Enter the name of the new account: ")
        print("Account: " + newName + "\nPassword: " + generatedPassword)
        confirm = input("Confirm creation of the following entry [Y/n]: ")
        while(True):
            if (confirm == 'Y' or confirm == 'y'):
                command = "INSERT INTO entries (Account, Password) VALUES (%s, %s)"
                entry = (newName, generatedPassword) 
                dbcursor.execute(command, entry)
                database.commit()
                print("New entry created.", end = ' ')
                break
            elif (confirm == 'N' or confirm == 'n'):
                print("Entry creation suspended.", end = ' ')
                break


