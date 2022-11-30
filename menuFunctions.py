#!/usr/bin/python3

import mysql.connector
import databaseFunctions as database
import main as main
import getpass
import os
from sys import exit
import pyfiglet as fig
from time import sleep

"""    
def mainMenu(): 
    os.system('clear')
    generateTitle("Main Menu")
    print(" 1. Add Password")
    print(" 2. Delete Password")
    print(" 3. Search Password")
    print(" 4. Edit Password")
    print(" 5. Generate Password")
    print(" Q. Quit")
    print("------------------------------------------")
    while(True):
        selection = input("Choose and option: ")
        if selection == '1':
            addMenu()
        elif selection == '2':
            deleteMenu()
        elif selection == '3':
            searchMenu()
        elif selection == '4':
            editMenu()
        elif selection == '5':
            generateMenu()
        elif (selection == 'Q' or selection == 'q'):
            break
        else:
            print("Invalid entry")
"""

def addMenu():
    os.system('clear')
    generateTitle("Add Entry")
    database.checkDatabase()
    database.addPassword()
    print("Returning to main menu...")
    sleep(3)
    main.mainMenu()

def deleteMenu():
    os.system('clear')
    generateTitle("Delete Entry")
    database.checkDatabase()
    database.deleteSelectedPassword()
    print("Returning to Main Menu...")
    sleep(3)
    main.mainMenu()

def editMenu():
    os.system('clear')
    generateTitle("Edit Entry")
    database.checkDatabase()
    database.editSelection()
    print("Returning to Main Menu...")
    sleep(3)
    main.mainMenu()

def searchMenu():
    os.system('clear')
    generateTitle("Search")
    database.checkDatabase()
    database.searchDatabase()
    print("Returning to main Menu...")
    sleep(3)
    main.mainMenu()
    
def generateMenu():
    os.system('clear')
    generateTitle("Pass Gen")
    database.checkDatabase()
    database.generatePassword()
    print("Returning to Main Menu...")
    sleep(3)
    main.mainMenu() 
    
def generateTitle(page):
    ascii_title = fig.figlet_format(page, font = "banner3-D", width = 200)
    print(ascii_title)
