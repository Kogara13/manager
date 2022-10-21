#!/usr/bin/python3

import pyfiglet as fig


title = "KeePass"  
ascii_title = fig.figlet_format(title, font  = "banner3-D")
print(ascii_title)

passworkEntry = input("Enter your Database Password: ")


try:
    
