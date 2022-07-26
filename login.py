from colorama import *
from slowprint import *
from logo_maker import *
import os

CorrectUsername = "osiris"#<~~~~~~ TYPE NAME HERE
CorrectPassword = "pass"#<~~~~~~ TYPE PASS HERE

def login():
    loop = 'true'
    while (loop == 'true'):
        username = input("Username: ")
        if (username == CorrectUsername):
            password = input("Password: ")
            print('')
            if (password == CorrectPassword):
                slowprint('Logged in successfully as ' + Fore.GREEN + username)
                loop = 'false'
                os.system('cls')
                white_color()
                print('Logged in successfully as ' + Fore.GREEN + username)
            else:
                print('Password incorrect!')
        else:
            print('Username incorrect!')