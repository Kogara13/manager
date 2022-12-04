#!/usr/bin/python3

#import dependencies
import mysql.connector
import databaseFunctions as database
import main as main
import getpass
import os
from sys import exit
import pyfiglet as fig
from time import sleep

#Function to call pyfiglet and generate titles on each page with the same configuration
def generateTitle(page):
    ascii_title = fig.figlet_format(page, font = "banner3-D", width = 200)
    print(ascii_title)

#Functions called from the different options presented in mainMenu() in main.py

"""
Each function does the following:
    1. Clears the terminal
    2. Generates their respective title
    3. Checks to see that the database exists throught checkDatabase() function in databaseFunctions.py
    4. Calls their respective functions from databaseFuctions.py to access the database
    5. Once, complete, the program will return to mainMenu()
"""

#Add Account and Password to database table
def addMenu():
    os.system('clear')
    generateTitle("Add Entry")
    database.checkDatabase()
    database.addPassword()
    print("Returning to main menu...")
    sleep(3)

#Delete Account and Password from database table
def deleteMenu():
    os.system('clear')
    generateTitle("Delete Entry")
    database.checkDatabase()
    database.deleteSelectedPassword()
    print("Returning to Main Menu...")
    sleep(3)

#Edit existing Account or Password in database table
def editMenu():
    os.system('clear')
    generateTitle("Edit Entry")
    database.checkDatabase()
    database.editSelection()
    print("Returning to Main Menu...")
    sleep(3)

#Search for existing Account and Passwordin database table
def searchMenu():
    os.system('clear')
    generateTitle("Search")
    database.checkDatabase()
    database.searchDatabase()
    print("Returning to main Menu...")
    sleep(3)
    
#Generate random password to use in new or existing database entry
def generateMenu():
    os.system('clear')
    generateTitle("Pass Gen")
    database.checkDatabase()
    database.generatePassword()
    print("Returning to Main Menu...")
    sleep(3)
    
