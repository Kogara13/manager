#!/usr/bin/python3

import pyfiglet as fig
import mysql.connector
import getpass
import menuFunctions as menu    

menu.generateTitle("Pass Manager")
usernameEntry = input("Enter your Username: ")
passwordEntry = getpass.getpass(prompt='Enter your Database Password: ')
entry = True

if entry == True:
    menu.mainMenu()

