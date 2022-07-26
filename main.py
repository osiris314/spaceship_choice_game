from hashlib import new
from colorama import (init, Fore)
import os
from slowprint import *
import random
import sys
######################################
os.system('cls')
######################################
def green_color():
    print(Fore.GREEN)
def red_color():
    print(Fore.RED)
def blue_color():
    print(Fore.BLUE)
def yellow_color():
    print(Fore.YELLOW)
def purple_color():
    print(Fore.MAGENTA)
def white_color():
    print(Fore.WHITE)
#####################################
class SpaceShip():
    def __init__(self, name, engine_health, landing_system_health, pods_left, data_integrity, navigation_system_health, life_support_health, scientific_probes_left):
        self.name = name
        self.engine_health = engine_health
        self.landing_system_health = landing_system_health
        self.pods_left = pods_left
        self.data_integrity = data_integrity
        self.navigation_system_health = navigation_system_health
        self.life_support_health = life_support_health
        self.scientific_probes_left = scientific_probes_left
        # 1 name
        # 2 engine_health
        # 3 landing_system_health
        # 4 pods_left
        # 5 data_integrity
        # 6 navigation_system_health
        # 7 life_support_health
        # 8 scientific_probes_left
    ########################################
    def print_spaceship_information(self):
        print('Name: ', self.name)
        ############
        if (self.pods_left >= 7) and (self.pods_left <= 10):
            green_color()
            print('Human pods: ', self.pods_left)
            sys.stdout.write("\033[F")
            white_color()
        elif (self.pods_left >= 4) and (self.pods_left <= 6):
            yellow_color()
            print('Human pods: ', self.pods_left)
            sys.stdout.write("\033[F")
            white_color()
        elif (self.pods_left >= 0) and (self.pods_left <= 3):
            red_color()
            print('Human pods: ', self.pods_left)
            sys.stdout.write("\033[F")
            white_color()
        ############
        if (self.engine_health >= 70) and (self.engine_health <= 100):
            green_color()
            print('Engine health: ', self.engine_health, '%')
            sys.stdout.write("\033[F")
            white_color()
        elif (self.engine_health >= 40) and (self.engine_health <= 60):
            yellow_color()
            print('Engine health: ', self.engine_health, '%')
            sys.stdout.write("\033[F")
            white_color()
        elif (self.engine_health >= 0) and (self.engine_health <= 30):
            red_color()
            print('Engine health: ', self.engine_health, '%')
            sys.stdout.write("\033[F")
            white_color()
        ############
        if (self.life_support_health >= 70) and (self.life_support_health <= 100):
            green_color()
            print('Life support: ', self.life_support_health, '%')
            sys.stdout.write("\033[F")
            white_color()
        elif (self.life_support_health >= 40) and (self.life_support_health <= 60):
            yellow_color()
            print('Life support: ', self.life_support_health, '%')
            sys.stdout.write("\033[F")
            white_color()
        elif (self.engine_health >= 0) and (self.life_support_health <= 30):
            red_color()
            print('Life support: ', self.life_support_health, '%')
            sys.stdout.write("\033[F")
            white_color()
        ############
        if (self.navigation_system_health >= 70) and (self.navigation_system_health <= 100):
            green_color()
            print('Navigation system: ', self.navigation_system_health, '%')
            sys.stdout.write("\033[F")
            white_color()
        elif (self.navigation_system_health >= 40) and (self.navigation_system_health <= 60):
            yellow_color()
            print('Navigation system: ', self.navigation_system_health, '%')
            sys.stdout.write("\033[F")
            white_color()
        elif (self.navigation_system_health >= 0) and (self.navigation_system_health <= 30):
            red_color()
            print('Navigation system: ', self.navigation_system_health, '%')
            sys.stdout.write("\033[F")
            white_color()
        ############
        if (self.landing_system_health >= 70) and (self.landing_system_health <= 100):
            green_color()
            print('Landing system: ', self.landing_system_health, '%')
            sys.stdout.write("\033[F")
            white_color()
        elif (self.landing_system_health >= 40) and (self.landing_system_health <= 60):
            yellow_color()
            print('Landing system: ', self.landing_system_health, '%')
            sys.stdout.write("\033[F")
            white_color()
        elif (self.landing_system_health >= 0) and (self.landing_system_health <= 30):
            red_color()
            print('Landing system: ', self.landing_system_health, '%')
            sys.stdout.write("\033[F")
            white_color()
        ############
        if (self.data_integrity >= 70) and (self.data_integrity <= 100):
            green_color()
            print('Data intengrity: ', self.data_integrity, '%')
            sys.stdout.write("\033[F")
            white_color()
        elif (self.data_integrity >= 40) and (self.data_integrity <= 60):
            yellow_color()
            print('Data intengrity: ', self.data_integrity, '%')
            sys.stdout.write("\033[F")
            white_color()
        elif (self.data_integrity >= 0) and (self.data_integrity <= 30):
            red_color()
            print('Data intengrity: ', self.data_integrity, '%')
            sys.stdout.write("\033[F")
            white_color()
        ############
        if (self.scientific_probes_left >= 7) and (self.scientific_probes_left <= 10):
            green_color()
            print('Scientific probes: ', self.scientific_probes_left)
            sys.stdout.write("\033[F")
            white_color()
        elif (self.scientific_probes_left >= 4) and (self.scientific_probes_left <= 6):
            yellow_color()
            print('Scientific probes: ', self.scientific_probes_left)
            sys.stdout.write("\033[F")
            white_color()
        elif (self.scientific_probes_left >= 0) and (self.scientific_probes_left <= 3):
            red_color()
            print('Scientific probes: ', self.scientific_probes_left)
            sys.stdout.write("\033[F")
            white_color()
        ########################################
    def set_engine_health(self, new_value):
        if (self.engine_health + new_value) <= 0:
            red_color()
            slowprint(s1.name,' was destroyed, CAUSE: Engines destroyed')
            white_color()
        else:
            self.engine_health = self.engine_health + new_value
        ########################################
    def set_landing_system_health(self, new_value):
        self.landing_system_health = self.landing_system_health + new_value
        ########################################
    def set_pods_left(self, new_value):
        self.pods_left = self.pods_left + new_value
        ########################################
    def set_data_integrity(self, new_value):
        self.data_integrity = self.data_integrity + new_value
        ########################################
    def set_navigation_system_health(self, new_value):
        self.navigation_system_health = self.navigation_system_health + new_value
        ########################################
    def set_life_support_health(self, new_value):
        if (self.life_support_health + new_value) <= 0:
            red_color()
            slowprint('Life support systems destroyed !')
            white_color()
        self.life_support_health = self.life_support_health + new_value
        ########################################
    def set_scientific_probes_left(self, new_value):
        if (self.scientific_probes_left + new_value) <= 0:
            red_color()
            slowprint('No more scientific probes left !')
            white_color()
        else:
            self.life_support_health = self.life_support_health + new_value
#################################################################################
#################################################################################

#s1 = SpaceShip(ship_name, 60, 60, 60, 60, 60, 60, 6)
#s1 = SpaceShip(ship_name, 30, 30, 30, 30, 30, 30, 3)
story_list=['Earth was destroyed','Earth was destroyed','Earth was destroyed']

ship_name = input('Type ship name: ')
os.system('cls')

slowprint(random.choice(story_list))
blue_color()
input("Press Enter to continue..")
white_color()

os.system('cls')
#s1 = SpaceShip(ship_name, 100, 100, 100, 100, 100, 100, 10)
#s1 = SpaceShip(ship_name, 60, 60, 60, 60, 60, 60, 6)
#s1 = SpaceShip(ship_name, 30, 30, 30, 30, 30, 30, 3)
s1 = SpaceShip(ship_name, 30, 70, 60, 40, 50, 10, 4)
s1.print_spaceship_information()
blue_color()
input("Press Enter to continue..")
white_color()
os.system('cls')

while True:
    event_list = ['1', '2', '3']
    # approaching planet
    # approaching black hole
    # solar flare hit the ship
    def generate_random_event():
        pass

