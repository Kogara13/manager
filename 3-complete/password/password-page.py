#!/usr/bin/python3

import getpass
import pyfiglet as fig
import mysql.connector


title = "KeePass"  
ascii_title = fig.figlet_format(title, font  = "banner3-D")
print(ascii_title)

usernameEntry = input("Enter your Username: ")
passwordEntry = getpass.getpass(prompt='Enter your Database Password: ')
#passwordEntry = input("Enter your Database Password: ")

"""
try:
    database = mysql.connector.connect(
            host="localhost"
            user = usernameEntry
            password = passwordEntry
)
"""
