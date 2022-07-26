from logo_maker import *
from loading_bar import *
from login import *
from slowprint import *
from spinner import *
import os

green_logo()
green_color()
fastprint('Type Your Credentials')
white_color()

login()
green_logo()

fastprint('Testing System Integrity')
loadss()

print('')
green_color()
fastprint('System Check-Up Complete. System Integrity at 100%')
white_color()
time.sleep(2)

os.system('cls')
spin_loader()
