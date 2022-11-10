#!/usr/bin/python3

import pyfiglet as fig
import mysql.connector
import getpass
import menuFunctions as menu    
import databaseFunctions as database

menu.generateTitle("Pass Manager")

check = database.passwordCheck()
if (check):
    menu.mainMenu()
else:
    print("error")

