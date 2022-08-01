import pyfiglet
from colorama import (init, Fore)
import os
import time
##################################################
init()
os.system('cls')
ascii_banner = pyfiglet.figlet_format("AIDA")#<~~~~~~ TYPE LOGO HERE
##################################################
def green_color():
    print(Fore.GREEN)

def red_color():
    print(Fore.RED)

def blue_color():
    print(Fore.BLUE)

def yellow_color():
    print(Fore.YELLOW)

def magenta_color():
    print(Fore.MAGENTA)

def white_color():
    print(Fore.WHITE)
##################################################
def green_logo():
    green_color()
    print(ascii_banner)
    white_color()

def red_logo():
    red_color()
    print(ascii_banner)
    white_color()

def blue_logo():
    blue_color()
    print(ascii_banner)
    white_color()

def yellow_logo():
    yellow_color()
    print(ascii_banner)
    white_color()

def magenta_logo():
    magenta_color()
    print(ascii_banner)
    white_color()

def white_logo():
    white_color()
    print(ascii_banner)
    white_color()
##################################################
def test_logos():
    green_logo()
    red_logo()
    blue_logo()
    yellow_logo()
    white_logo()
##################################################