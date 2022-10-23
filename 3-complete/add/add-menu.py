#!/usr/bin/python3

import pyfiglet as fig

title1 = "Add"
ascii_title1 = fig.figlet_format(title1, font = "banner3-D")
print(ascii_title1)

title2 = "Entry"
ascii_title2 = fig.figlet_format(title2, font = "banner3-D")
print(ascii_title2)

name = input("Enter the Account name: ")
password = input("Enter the Password for the Account: ")
passwordCheck = input("ReEnter the Password: ")
print("------------------------------------------")
