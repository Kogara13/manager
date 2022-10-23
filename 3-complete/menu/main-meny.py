#!/usr/bin/python3

import pyfiglet as fig
import mysql.connector

title1 = "Main"
ascii_title1 = fig.figlet_format(title1, font = "banner3-D")
print(ascii_title1)  

title2 = "Menu"
ascii_title2 = fig.figlet_format(title2, font = "banner3-D")
print(ascii_title2)  
 
print(" 1. Add Password")
print(" 2. Delete Password")
print(" 3. Edit Password")
print(" 4. Generate Password")
print("------------------------------------------")
selection = input("Choose and option: ")    
