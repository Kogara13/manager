#!/usr/bin/bash

sudo apt update
sudo apt install python3 python3-pip python-dev 
pip install pyfiglet
sudo apt install mysql-server
sudo systemctl start mysql.service

echo "Dependencies installed. Please take the necessary steps to finish setting up a mySQL database"
echo "https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04mport pyperclip"

#sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password'"

#mysql_secure_installation

#sudo mysql -u root -p -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH auth_socket"

#sudo mysql_secure_installation
