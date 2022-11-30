#!/usr/bin/python3

import mysql.connector
import databaseFunctions as database
import main as main
import getpass
import os
from sys import exit
import pyfiglet as fig
from time import sleep


def addMenu():
    os.system('clear')
    generateTitle("Add Entry")
    database.checkDatabase()
    database.addPassword()
    print("Returning to main menu...")
    sleep(3)

def deleteMenu():
    os.system('clear')
    generateTitle("Delete Entry")
    database.checkDatabase()
    database.deleteSelectedPassword()
    print("Returning to Main Menu...")
    sleep(3)

def editMenu():
    os.system('clear')
    generateTitle("Edit Entry")
    database.checkDatabase()
    database.editSelection()
    print("Returning to Main Menu...")
    sleep(3)

def searchMenu():
    os.system('clear')
    generateTitle("Search")
    database.checkDatabase()
    database.searchDatabase()
    print("Returning to main Menu...")
    sleep(3)
    
def generateMenu():
    os.system('clear')
    generateTitle("Pass Gen")
    database.checkDatabase()
    database.generatePassword()
    print("Returning to Main Menu...")
    sleep(3)
    
def generateTitle(page):
    ascii_title = fig.figlet_format(page, font = "banner3-D", width = 200)
    print(ascii_title)
