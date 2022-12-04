#!/usr/bin/bash

sudo apt update
sudo apt install python3 python3-pip python-dev 
pip install pyfiglet
sudo apt install mysql-server
sudo systemctl start mysql.service

echo "Dependencies installed. Please take the necessary steps to finish setting up a mySQL database.\n
These can be found in the Program documentation, or by visiting the link below.\n\n"
echo "https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04mport pyperclip"
