#!/usr/bin/python3

import pyfiglet as fig
import mysql.connector
import getpass
import menuFunctions as menu    
import databaseFunctions as database
from time import sleep
import os

#This comment is left to test the merge

def main():
    os.system('clear')
    menu.generateTitle("Pass Manager")

    check = database.passwordCheck()
    if (check):
        mainMenu()
    else:
        print("\nGoodbye\n")
        sleep(1)
        return
    print("\nGoodbye\n")
    sleep(1) 
    return


def mainMenu():
    while(True):
        os.system("clear")
        menu.generateTitle("Main Menu")
        exit = True
        print("1. Add Password\n2. Delete Password\n3. Search Password\n4. Edit Password\n5. Generate Password\nQ. Quit")
        print("-----------------------------------------")
        selection = input("Choose an option: ")
        if selection == '1':
            menu.addMenu()
            continue
        elif selection == '2':
            menu.deleteMenu()
            continue
        elif selection == '3':
            menu.searchMenu()
            continue
        elif selection == '4':
            menu.editMenu()
            continue
        elif selection == '5':
            menu.generateMenu()
            continue
        elif (selection == 'Q' or selection == 'q'):
            os.system('clear')
            confirmQuit = input("Are you sure you want to quit? [Y/N]:  ")
            if (confirmQuit == 'N' or confirmQuit == 'n'):
                exit = False
            elif (confirmQuit == 'Y' or confirmQuit == 'y'):
                exit = True
            else:
                print("Invalid entry. Returning to Main Menu...")
                sleep(2)
                continue
            if (exit):
                break
            else:
                continue
    return


if __name__ == "__main__":
    main()




