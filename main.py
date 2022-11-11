#!/usr/bin/python3

import pyfiglet as fig
import mysql.connector
import getpass
import menuFunctions as menu    
import databaseFunctions as database
from time import sleep

def main():
    menu.generateTitle("Pass Manager")

    check = database.passwordCheck()
    if (check):
        menu.mainMenu()
    else:
        print("error")
    print("\nGoodbye\n")
    sleep(1) 
    return

if __name__ == "__main__":
    main()
