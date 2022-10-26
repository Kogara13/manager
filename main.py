#!/usr/bin/python3

import pyfiglet as fig
import mysql.connector
import getpass
import functions

functions.generateTitle("Pass Manager")
usernameEntry = input("Enter your Username: ")
passwordEntry = getpass.getpass(prompt='Enter your Database Password: ')
entry = True

if entry == True:
    functions.mainMenu()

