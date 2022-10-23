#!/usr/bin/python3

import pyfiglet as fig

title = "Edit"
ascii_title = fig.figlet_format(title, font = "banner3-D")
print(ascii_title)

selection = input("Enter which account you would like to edit: ")
print("1. Entry Name")
print("2. Entry Password")
print("------------------------------------------")
choice = input("Would you like to change the entry or the password (Enter number of choice): ")

#If changing the name
edit = input ("What would you like to change the name to: " )

#If changing password
passChange = input("Enter new Password: ")
passCheck = input("Reenter new Password: ")


#Print that name or password has been changed
