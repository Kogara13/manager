#!/usr/bin/python3

import pyfiglet as fig

title = "Pass-gen"
ascii_title = fig.figlet_format(title, font = "banner3-D", width = 200)
print(ascii_title)

length = input("Enter the length of the password: ")
print("By default, the password will include lowercase and uppercase characters, and numbers")
extra = input("Would you like to include symbols (!@#$%^&* etc.) for extra security")

#Generate new password into variable

#random string based on characters from other strings, for loop through them excluding sybol based on index

#Ask user if they would like to replace an existing password for this one
#Ask again for assurance


