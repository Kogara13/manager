#!/usr/bin/python3

import getpass
import pyfiglet as fig
import mysql.connector

def passwordPage():
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

