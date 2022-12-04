#!/usr/bin/python3

#importing necessary dependencies
import pyfiglet as fig
import mysql.connector
import getpass
import menuFunctions as menu    
import databaseFunctions as database
from time import sleep
import os

#main function. All other functions stem from this here.
def main():
    os.system('clear')
    menu.generateTitle("Pass Manager")

    #function for entering master password. Returns a boolean value indicating if access is granted
    check = database.passwordCheck()
    if (check):
        mainMenu()
    else:
        #Printed when the user selects Quit (Q.) from the Main Menu
        print("\nGoodbye\n")
        sleep(1)
        return
    print("\nGoodbye\n")
    sleep(1) 
    return


def mainMenu():
    while(True): #This while loop iterates every time the user returns to the main menu, and if the user ever enters an invalid option
        #clear terminal
        os.system("clear")
        menu.generateTitle("Main Menu")
        exit = True #boolean to check if the user wants to exit the program
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
    #call main function
    main()




