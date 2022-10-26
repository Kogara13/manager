#!/usr/bin/python3

import pyfiglet as fig

title = "Delete"
ascii_title = fig.figlet_format(title, font = "banner3-D")
print(ascii_title)

selection = input("Enter which account you would like to delete: ")
check = input("Are you sure you want to delete this account entry? [Y/n] ")

