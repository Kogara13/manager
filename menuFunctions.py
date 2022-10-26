#!/usr/bin/python3

import mysql.connector
import getpass
import os
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
    print("------------------------------------------")
    selection = int(input("Choose and option: "))
    if selection == 1:
        addPassword()
    elif selection == 2:
        deletePassword()
    elif selection == 3:
        editPassword()
    elif selection == 4:
        generatePassword(generateCheck)
        generateCheck += 1

def addPassword():
    os.system('clear')
    generateTitle("Add Entry")
    name = input("Enter the Account name: ")
    password = getpass.getpass(prompt="Enter the Password for the Account: ")
    passwordCheck = getpass.getpass(prompt="Reenter the Password: ")

    print("Password entered into database. Returning to main menu...")
    sleep(3)
    mainMenu()

def deletePassword():
    os.system('clear')
    generateTitle("Delete Entry")

    selection = input("Enter which account you would like to delete: ")
    check = input("Are you sure you want to delete this account entry? [Y/n] ")

    print("Account deleted. Returning to Main Menu...")
    sleep(3)
    mainMenu()

def editPassword():
    os.system('clear')
    generateTitle("Edit Entry")

    selection = input("Enter which account you would like to edit: ")
    print(" 1. Entry name")
    print(" 2. Entry Password")
    print("------------------------------------------")
    entry = int(input("Would you like to change the entry or the password (Enter # of choice): "))
    
    if entry == 1:
        edit = input("What would you like to change the name to?: ")
        confirm = input("Confirm new entry name: ")
        print("Name", end = ' ')
    elif entry == 2:    
        edit = getpass.getpass(prompt="What would you like to change the password to?: ")
        confirm = getpass.getpass(prompt="Confirm new password: ")
        print("Password", end = ' ')
    print("changed. Returning to Main Menu...")
    sleep(3)
    mainMenu()
    
def generatePassword():
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

def generateTitle(page):
    ascii_title = fig.figlet_format(page, font = "banner3-D", width = 200)
    print(ascii_title)


