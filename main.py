#!/usr/bin/python3

import pyfiglet as fig
import mysql.connector
import getpass
import menuFunctions as menu    
import databaseFunctions as database
from time import sleep
import os

def main():
    os.system('clear')
    menu.generateTitle("Pass Manager")

    check = database.passwordCheck()
    if (check):
        menu.mainMenu()
    else:
        print("\nGoodbye\n")
        sleep(1)
        return
    print("\nGoodbye\n")
    sleep(1) 
    return

if __name__ == "__main__":
    main()
