import re
import string
import random
import os
import sqlite3

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
        option = int(input("1) create new password\n2) retrive password\n"))
        if [1, 2].__contains__(option):
            break
    if option == 1:
        clear_screen()
        print('Create a key that you will use to identify the password eg. facebook, instagram e.t.c.')
        password_key = input("Enter the password key: ")
        password = generate_password()
        clear_screen()
        #use repr() to literally display a string containing special characters

        print(f"the following password hass been succefully created\n{password_key}: {repr(password)}")

    # elif option == 2:


def generate_password():
    password = ''
    password += ''.join(random.sample(list(string.digits), k=5))
    password += ''.join(random.sample(list(string.ascii_uppercase), k=5))
    password += ''.join(random.sample(list(string.ascii_lowercase), k=5))
    password += ''.join(random.sample(list(string.punctuation), k=5))
    password += ''.join(random.sample(list(string.printable), k=10))    

    return password

if __name__ == "__main__":
    #open the database
    connection = sqlite3.connect("pwd.db")
    #run the program
    menu()
    
