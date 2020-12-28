import re
import string
import random
import os
import sqlite3
import sys
import time
import hashlib

special_chars = string.punctuation
lowercase = string.ascii_lowercase 
uppercase = string.ascii_uppercase
numbers = string.digits

def clear_screen():
    try:
        os.system('clear')
        print("**** welcome to hsa password manager ****\n")
    except:
        os.system('cls')
        print("**** welcome to hsa password manager ****\n")

def menu():
    clear_screen()
    while True:
        option = int(input("1) create new password\n2) display passwords\n"))
        if [1, 2].__contains__(option):
            break
    if option == 1:
        clear_screen()
        print('Create a key that you will use to identify the password eg. facebook, instagram e.t.c.')
        password_key = input("Enter the password key: ")
        password = generate_password()
        clear_screen()
        # save to sqlite db
        # cursor.execute(f"INSERT INTO passwords VALUES('{password_key}', '{password.encode()}')")
        cursor.execute(f"INSERT INTO passwords VALUES(?, ?)",(password_key, password))
        connection.commit()

        #use repr() to literally display a string containing special characters
        print(f"the following password hass been succefully created\n{password_key}: {repr(password)}")
        print(cursor.execute("SELECT * FROM passwords").fetchall())

    elif option == 2:
        rows = cursor.execute("select * from passwords").fetchall()
        # print(rows)
        formatted_result = [f"{key:<10}{repr(password)}" for key, password in rows]
        clear_screen()
        key, password = "Key", "Password"
        print('\n'.join([f"{key:<11}{password}"] + formatted_result))


def generate_password():
    password = ''
    password += ''.join(random.sample(list(string.digits), k=5))
    password += ''.join(random.sample(list(string.ascii_uppercase), k=5))
    password += ''.join(random.sample(list(string.ascii_lowercase), k=5))
    password += ''.join(random.sample(list(string.punctuation), k=5))
    password += ''.join(random.sample(list(string.printable), k=10))
    password = list(password)
    random.shuffle(password)
    password = ''.join(password)
    print(password)

    return password

if __name__ == "__main__":
    #open the database
    if os.path.exists('pwd.db'):
        #check authentication
        try:
            password = sys.argv[1]
        except:
            clear_screen()
            print("Provide the password\nsyntax:pwdmg.py (password) (key **optional)")
            quit()
        connection = sqlite3.connect("pwd.db")
        cursor = connection.cursor()
        root_hash = cursor.execute("SELECT password from passwords where key = 'root_user'").fetchall()
        root_hash = root_hash[0][0]

        if root_hash != hashlib.md5(password.encode('utf-8')).hexdigest():
            sys.exit('Incorrect Password')
        else:
            menu()

    else:
        clear_screen()
        password = input('Welcome to initial setup \nEnter your account password: ')
        pwd_hash = hashlib.md5(password.encode('utf-8')).hexdigest()

        connection = sqlite3.connect("pwd.db")
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE passwords (key TEXT, password TEXT)")
        cursor.execute(f"INSERT INTO passwords VALUES (?, ?)",("root_user", pwd_hash))
        connection.commit()

        menu()