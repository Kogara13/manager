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

"""
def mainMenu():
    os.system("clear")
    menu.generateTitle("Main Menu")
    print(" 1. Add Password\n
            2. Delete Password\n
            3. Edit Password\n
            4. Generate Password\n
            Q. Quit")
    print("-----------------------------------------")
    while(True):
        selection = input("Choose an option: ")
        if selection == '1':
            menu.addMenu()
        elif selection == '2':
            menu.deleteMenu()
        elif selection == '3':
            menu.editMenu()
        elif selection == '4':
            menu.generateMenu()
        elif (selection == 'Q' or selection == 'q'):
            os.system('clear')
            confirmQuit = input("Are you sure you want to quit? ")
            if (confirmQuit == 'N' or confirmQuit == 'n'):
                continue
            elif (confirmQuit == 'Y' or confirmQuit == 'y'):
                return
            else:
                print("Invalid entry. Returning to Main Menu...")
                sleep(1)
                continue
"""

if __name__ == "__main__":
    main()




