#!/usr/bin/python3

import mysql.connector
import databaseFunctions as database
import getpass
import os
from sys import exit
import pyfiglet as fig
from time import sleep

generateCheck = 0
    
def mainMenu(): 
    os.system('clear')
    generateTitle("Main Menu")
    print(" 1. Add Password")
    print(" 2. Delete Password")
    print(" 3. Edit Password")
    print(" 4. Generate Password")
    print(" 5. Create Account")
    print(" Q. Quit")
    print("------------------------------------------")
    while(True):
        selection = int(input("Choose and option: "))
        if selection == 1:
            addMenu()
        elif selection == 2:
            deleteMenu()
        elif selection == 3:
            editMenu()
        elif selection == 4:
            generateMenu(generateCheck)
            generateCheck += 1
        elif database.usernameEntry == "root" and selection == 5:
            accountMenu()
        elif (selection == 'Q' or selection == 'q'):
            sys.exit()
        else:
            print("Invalid entry")

def addMenu():
    os.system('clear')
    generateTitle("Add Entry")
    database.checkDatabase()
    database.addPassword()
    print("Password entered into database. Returning to main menu...")
    sleep(3)
    mainMenu()

def deleteMenu():
    os.system('clear')
    generateTitle("Delete Entry")
    database.checkDatabase()
    database.deleteSelectedPassword()
    print("Returning to Main Menu...")
    sleep(3)
    mainMenu()

def editMenu():
    os.system('clear')
    generateTitle("Edit Entry")
    database.checkDatabase()
    database.editSelection()
    print("Returning to Main Menu...")
    sleep(3)
    mainMenu()
    
def generateMenu():
    os.system('clear')
    generateTitle("Pass Gen")

    global generateCheck
    length = input("Enter the length of the password: ")
    if generateCheck == 0:
        print("By default, the password will inlcude lowercase and uppercase characters, and numbers")
        generateCheck += 1
    addSymbols = input("Would you like to include symbols (!@#$%^&* etc.) for extra securty [Y/n]?: ")
    if addSymbols == 'Y' or addSymbols == 'y':
        #functions for generating password
        print("Here is the new password")
    elif addSymbols == 'N' or addSymbols == 'n': 
        #functions for generating password
        print("Here is the new password")

    #Ask if user would like to replace existing password
    #Ask again for assurance

    print("\nReturning to Main Menu...")
    sleep(3)
    mainMenu()

def accountMenu():
    os.system('clear')
    generateTitle("Create Account")

    newUser = input("Enter the new user name: ")
    newPassword = input("Enter the new user password: ")
    while(True):
        confirmPassword = input("Retype the new password: ")
        if confirmPassword == newPassword:
            #access database functions to create account
            break
    print("New account created. Returning to Main Menu...")
    sleep(3)
    mainMenu()
    
    
def generateTitle(page):
    ascii_title = fig.figlet_format(page, font = "banner3-D", width = 200)
    print(ascii_title)


