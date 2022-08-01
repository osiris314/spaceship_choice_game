import random
import os
from spinner import spin_loader
from colorama import Fore, Style
from playsound import *
from slowprint import *
import time
import sys
from loading_bar import loadss
#####################################

# setting celcius symbol
degree_sign = u"\N{DEGREE SIGN}"
#####################################

# make colors 
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
def light_yellow_color():
    print(Fore.LIGHTYELLOW_EX)
#####################################

# story
def start_story():
    light_yellow_color()
    slowprint('Time left: 11 days to impact')
    white_color()
    fastprint('NASA scientists detect a type 3 asteroid named Apophis with a stricking course for Earth.')
    fastprint('Impact estimated to hit: 28, June 2022. First estimations point the impact location Alaska, USA.\n')

    yellow_color()
    slowprint('Time left: 10 days to impact')
    white_color()
    fastprint('Top scientists say the asteroid is too close to Earth to deflect at this point.')
    fastprint('Best plan is to build  spaceships in order to transport humans to an other solar system.')
    fastprint('Most likely Proxima Centuri the closest star to ours.\n')

    yellow_color()
    slowprint('Time left: 1 day to impact')
    white_color()
    fastprint('Spaceships all over the world  launched into the sky for a new home')
    fastprint('Leaving behind 6.350.834.532 people.\n')

    red_color()
    slowprint('Time left: 0 days to impact')
    white_color()
    fastprint('Asteroid Apophis collides with Earth leaving behind a 250.000 crater.')
    fastprint('7 hours later the wall of fire travelled to the other side of the globe')
    fastprint('and burned every single oxygen molecule in the atmosphere.')
    fastprint('Making Earth from a life fairing planet to a hostile one.\n')

    red_color()
    slowprint('Time: 8 days after impact')
    white_color()
    fastprint('It is time for the preparations of the journey to begin.')
    fastprint('First of all the ship was commanded by an AI.')
    fastprint('The AI that commandes the ship will monitor various statistics like, the health of the engine,')
    fastprint('the navigation system, etc. Also it will have to take action if things get out of hand.')
    fastprint('Humans will have to cryo preserve themselves in order to survive the')
    fastprint('9736 years of travel to visit Proxima. And the time was up,')
    fastprint('everyone said goodbye to each other and praied for an Earth like planet')
    fastprint('when they finaly arrived. Every Earther boarded  his pod for the big sleep.')

    blue_color()
    input("Press Enter to continue..")
    white_color()
#####################################

# various lists
name_list=[
       'Proxima Centauri', 'Wolf 359', 'Lalande 21185', 'Epsilon Eridani', 'Lacaille 9352', 'Ross 128',
       'Struve 2398', 'Groombridge 34', 'Epsilon Indi', 'Tau Ceti', 'Gliese 1061', 'YZ Ceti', 'Luyten'
       ]       
event_list=['planet', 'planet', 'disaster']
disaster_list=['solar_flare', 'pods_malfunction']
type_list = ['Rocky', 'Cloudlike', 'Dessert']
atmosphere_list  = ['Toxic', 'Habitable', 'Moderate']
animals_list = ['Not Found', 'Edible Animals', 'Venomous']
water_list = ['Not Found', 'Small Deposits', 'Vast Amounts']
vegetation_list = ['Not Found', 'Toxic Plants', 'Edible Plants']
civilization_list = ['Not Found', 'Found', 'Old Ruins']
utilities_list=['engine_health', 'landing_system', 'pods', 'data_integrity', 'navigation_system', 'life_support']
#####################################
#####################################

# Spaceship class
class SpaceShip():
    def __init__(self, name, current_event, engine_health, landing_system, pods, data_integrity, navigation_system, life_support, scientific_probes) -> None:
        self.name = name
        self.current_event = current_event
        self.engine_health = engine_health
        self.landing_system = landing_system
        self.pods = pods
        self.data_integrity = data_integrity
        self.navigation_system = navigation_system
        self.life_support = life_support
        self.scientific_probes = scientific_probes

    # check spaceship values if critical
    def check():
        if spaceship.engine_health <= 0:
            os.system('cls')
            red_color()
            print('Engine Health Critical')
            print('No More Thrust')
            purple_color
            slowprint('GAME OVER')
            white_color()
            sys.exit()
            
        if spaceship.life_support <= 0:
            os.system('cls')
            red_color()
            print('Life Support Health Critical')
            print('No More Oxygen')
            purple_color()
            slowprint('GAME OVER')
            white_color()
            sys.exit()

        if spaceship.pods <= 0:
            os.system('cls')
            red_color()
            print('All Pods Where Destroyed')
            print('Everyone Died')
            purple_color()
            slowprint('GAME OVER')
            white_color()
            sys.exit()
        
        if spaceship.navigation_system <= 0:
            os.system('cls')
            red_color()
            print('Navigation System Has Been Destroyed')
            print(spaceship.name,'Cannot Navigate To The Next Star')
            purple_color()
            slowprint('GAME OVER')
            white_color()
            sys.exit()
        
        if spaceship.data_integrity < 0:
            spaceship.data_integrity = 0
        
        if spaceship.landing_system < 0:
            spaceship.landing_system = 0

    # reshape spaceship object output
    # setting color depending on values
    def __str__(self) -> str:
        print(Fore.WHITE + 'Spaceship: ' + Fore.LIGHTYELLOW_EX + str(self.name) + Fore.WHITE)  
        if (self.engine_health >= 70) and (self.engine_health <= 100):
            print(Fore.WHITE + 'Engine Health: ' + Fore.GREEN + str(self.engine_health)+ '%' + Fore.WHITE)
        elif (self.engine_health >= 40) and (self.engine_health <= 60):
            print(Fore.WHITE + 'Engine Health: ' + Fore.YELLOW + str(self.engine_health)+ '%' + Fore.WHITE)
        elif (self.engine_health >= 0) and (self.engine_health <= 30):
            print(Fore.WHITE + 'Engine Health: ' + Fore.RED + str(self.engine_health)+ '%' + Fore.WHITE)

        if (self.landing_system >= 70) and (self.landing_system <= 100):
            print(Fore.WHITE + 'Landing System: ' + Fore.GREEN + str(self.landing_system)+ '%' + Fore.WHITE)
        elif (self.landing_system >= 40) and (self.landing_system <= 60):
            print(Fore.WHITE + 'Landing System: ' + Fore.YELLOW + str(self.landing_system)+ '%' + Fore.WHITE)
        elif (self.landing_system >= 0) and (self.landing_system <= 30):
            print(Fore.WHITE + 'Landing System: ' + Fore.RED + str(self.landing_system)+ '%' + Fore.WHITE)
        
        if (self.pods >= 67) and (self.pods <= 100):
            print(Fore.WHITE + 'Cryo Pods: ' + Fore.GREEN + str(self.pods)+ Fore.WHITE)
        elif (self.pods >= 34) and (self.pods <= 66):
            print(Fore.WHITE + 'Cryo Pods: ' + Fore.YELLOW + str(self.pods)+ Fore.WHITE)
        elif (self.pods >= 0) and (self.pods <= 33):
            print(Fore.WHITE + 'Cryo Pods: ' + Fore.RED + str(self.pods)+ Fore.WHITE)
        
        if (self.data_integrity >= 70) and (self.data_integrity <= 100):
            print(Fore.WHITE + 'Library Integrity: ' + Fore.GREEN + str(self.data_integrity)+ '%' + Fore.WHITE)
        elif (self.data_integrity >= 40) and (self.data_integrity <= 60):
            print(Fore.WHITE + 'Library Integrity: ' + Fore.YELLOW + str(self.data_integrity)+ '%' + Fore.WHITE)
        elif (self.data_integrity >= 0) and (self.data_integrity <= 30):
            print(Fore.WHITE + 'Library Integrity: ' + Fore.RED + str(self.data_integrity)+ '%' + Fore.WHITE)
        
        if (self.navigation_system >= 70) and (self.navigation_system <= 100):
            print(Fore.WHITE + 'Navigation System: ' + Fore.GREEN + str(self.navigation_system)+ '%' + Fore.WHITE)
        elif (self.navigation_system >= 40) and (self.navigation_system <= 60):
            print(Fore.WHITE + 'Navigation System: ' + Fore.YELLOW + str(self.navigation_system)+ '%' + Fore.WHITE)
        elif (self.navigation_system >= 0) and (self.navigation_system <= 30):
            print(Fore.WHITE + 'Navigation System: ' + Fore.RED + str(self.navigation_system)+ '%' + Fore.WHITE)

        if (self.life_support >= 70) and (self.life_support <= 100):
            print(Fore.WHITE + 'Life Support: ' + Fore.GREEN + str(self.life_support)+ '%' + Fore.WHITE)
        elif (self.life_support >= 40) and (self.life_support <= 60):
            print(Fore.WHITE + 'Life Support: ' + Fore.YELLOW + str(self.life_support)+ '%' + Fore.WHITE)
        elif (self.life_support >= 0) and (self.life_support <= 30):
            print(Fore.WHITE + 'Life Support: ' + Fore.RED + str(self.life_support)+ '%' + Fore.WHITE)

        if (self.scientific_probes >= 7) and (self.scientific_probes <= 10):
            print(Fore.WHITE + 'Scientific Probes: ' + Fore.GREEN + str(self.scientific_probes)+ Fore.WHITE)
        elif (self.scientific_probes >= 4) and (self.scientific_probes <= 6):
            print(Fore.WHITE + 'Scientific Probes: ' + Fore.YELLOW + str(self.scientific_probes)+ Fore.WHITE)
        elif (self.scientific_probes >= 1) and (self.scientific_probes <= 3):
            print(Fore.WHITE + 'Scientific Probes: ' + Fore.RED + str(self.scientific_probes)+ Fore.WHITE)
        elif (self.scientific_probes >= 0):
            print(Fore.WHITE + 'Scientific Probes: ' + Fore.MAGENTA + str(self.scientific_probes)+ Fore.WHITE)        
        return ''
    
    # display choice menu
    def make_choice(self):
        os.system('cls')
        print(spaceship)
        print('--------------------------')
        print(planet)
        blue_color()
        print('1 to send probe')
        print('2 to attempt landing')
        print('3 to keep searching')
        green_color()
        self.answer = input('Type Choice: ')
        white_color()

        if self.answer == '1':
            try_probes()
        elif self.answer == '2':
            playsound('attempting_to_land.mp3')
            landing_scene()
        elif self.answer == '3':
            SpaceShip.change_current_event(spaceship)
        else:
            SpaceShip.make_choice(spaceship)

    # random event between new_planet and new_disaster
    def change_current_event(self):
        self.current_event = random.choice(event_list)
        if self.current_event == 'planet':
            SpaceShip.Planet.change_stats(planet)
            planet_scene()
            
        elif self.current_event == 'disaster':
            playsound('disaster_ahead.mp3')
            SpaceShip.change_current_disaster(spaceship)
            
        else:
            planet_scene()

    # change spaceschip values manualy     
    def change_stats(selection, value):
        if selection == 'name':
            SpaceShip.name = value
        elif selection == '':
            pass

    # select disaster randomly from disaster_list
    def change_current_disaster(self):
        self.current_disaster = random.choice(disaster_list)
        if self.current_disaster == 'solar_flare':
            disaster_scene()
            
        elif self.current_disaster == 'pods_malfunction':
            disaster_scene()
        else:
            print('else')
#####################################
#####################################

# planet class
    class Planet():
        global candidates
        candidates = 1
        def __init__(self, candidate, name, gravity, type, temperature, atmosphere, animals, water, vegetation, civilization, unlocked) -> None:
            self.candidate = candidates
            self.name = random.choice(name_list)
            self.gravity = random.randint(1, 100)
            self.type = random.choice(type_list)
            self.temperature = random.randint(-50, 100)
            self.atmosphere = random.choice(atmosphere_list)
            self.animals = random.choice(animals_list)
            self.water = random.choice(water_list)
            self.vegetation = random.choice(vegetation_list)
            self.civilization = random.choice(civilization_list)
            self.unlocked = unlocked
        
        # reshape planet object output
        # setting color depending on values
        def __str__(self) -> str:
            if self.unlocked == True:
                print('Candidate: #' + str(self.candidate))
                print(Fore.WHITE + 'Name: ' + Fore.MAGENTA + str(self.name) + Fore.WHITE)  
                if (self.type == 'Rocky'):
                    print(Fore.WHITE + 'Type: ' + Fore.GREEN + str(self.type) + Fore.WHITE)
                elif (self.type == 'Cloudlike'):
                    print(Fore.WHITE + 'Type: ' + Fore.RED + str(self.type) + Fore.WHITE)
                elif (self.type == 'Dessert'):
                    print(Fore.WHITE + 'Type: ' + Fore.YELLOW + str(self.type) + Fore.WHITE)
                elif (self.type == 'Sea Planet'):
                    print(Fore.WHITE + 'Type: ' + Fore.RED + str(self.type) + Fore.WHITE)
                
                if (self.gravity >= 70) and (self.gravity <= 100):
                    print(Fore.WHITE + 'Gravity: ' + Fore.GREEN + str(self.gravity) + '%' + Fore.WHITE)
                elif (self.gravity >= 40) and (self.gravity <= 60):
                    print(Fore.WHITE + 'Gravity: ' + Fore.YELLOW + str(self.gravity) + '%' + Fore.WHITE)
                elif (self.gravity >= 0) and (self.gravity <= 30):
                    print(Fore.WHITE + 'Gravity: ' + Fore.RED + str(self.gravity) + '%' + Fore.WHITE)                    

                if (self.temperature >= -50) and (self.temperature <= -15):
                    print(Fore.WHITE + 'Temperature: ' + Fore.RED + str(self.temperature) + degree_sign + Fore.WHITE)
                elif (self.temperature >= -14) and (self.temperature <= 5):
                    print(Fore.WHITE + 'Temperature: ' + Fore.YELLOW + str(self.temperature) + degree_sign + Fore.WHITE)
                elif (self.temperature >= 6) and (self.temperature <= 30):
                    print(Fore.WHITE + 'Temperature: ' + Fore.GREEN + str(self.temperature) + degree_sign + Fore.WHITE)
                elif (self.temperature >= 31) and (self.temperature <= 50):
                    print(Fore.WHITE + 'Temperature: ' + Fore.YELLOW + str(self.temperature) + degree_sign + Fore.WHITE) 
                elif (self.temperature >= 51) and (self.temperature <= 100):
                    print(Fore.WHITE + 'Temperature: ' + Fore.RED + str(self.temperature) + degree_sign + Fore.WHITE)                                  

                if (self.atmosphere == 'Toxic'):
                    print(Fore.WHITE + 'Atmosphere: ' + Fore.RED + str(self.atmosphere) + Fore.WHITE)
                elif (self.atmosphere == 'Habitable'):
                    print(Fore.WHITE + 'Atmosphere: ' + Fore.GREEN + str(self.atmosphere) + Fore.WHITE)
                elif (self.atmosphere == 'Moderate'):
                    print(Fore.WHITE + 'Atmosphere: ' + Fore.GREEN + str(self.atmosphere) + Fore.WHITE)                                    

                if (self.animals == 'Not Found'):
                    print(Fore.WHITE + 'Animals: ' + Fore.YELLOW + str(self.animals) + Fore.WHITE)
                elif (self.animals == 'Edible Animals'):
                    print(Fore.WHITE + 'Animals: ' + Fore.GREEN + str(self.animals) + Fore.WHITE)
                elif (self.animals == 'Venomous'):
                    print(Fore.WHITE + 'Animals: ' + Fore.RED + str(self.animals) + Fore.WHITE)

                if (self.water == 'Not Found'):
                    print(Fore.WHITE + 'Water: ' + Fore.RED + str(self.water) + Fore.WHITE)
                elif (self.water == 'Vast Amounts'):
                    print(Fore.WHITE + 'Water: ' + Fore.GREEN + str(self.water) + Fore.WHITE)
                elif (self.water == 'Small Deposits'):
                    print(Fore.WHITE + 'Water: ' + Fore.YELLOW + str(self.water) + Fore.WHITE)

                if (self.vegetation == 'Not Found'):
                    print(Fore.WHITE + 'Vegetation: ' + Fore.YELLOW + str(self.vegetation) + Fore.WHITE)
                elif (self.vegetation == 'Toxic Plants'):
                    print(Fore.WHITE + 'Vegetation: ' + Fore.RED + str(self.vegetation) + Fore.WHITE)
                elif (self.vegetation == 'Edible Plants'):
                    print(Fore.WHITE + 'Vegetation: ' + Fore.GREEN + str(self.vegetation) + Fore.WHITE)

                if (self.civilization == 'Not Found'):
                    print(Fore.WHITE + 'Civilization: ' + Fore.RED + str(self.civilization) + Fore.WHITE)            
                elif (self.civilization == 'Found'):
                    print(Fore.WHITE + 'Civilization: ' + Fore.GREEN + str(self.civilization) + Fore.WHITE)
                elif (self.civilization == 'Old Ruins'):
                    print(Fore.WHITE + 'Civilization: ' + Fore.YELLOW + str(self.civilization) + Fore.WHITE)             
                return ''

            elif self.unlocked == False:
                print('Candidate: #' + str(self.candidate))
                print(Fore.WHITE + 'Name: ' + Fore.MAGENTA + str(self.name) + Fore.WHITE)  

                if (self.type == 'Rocky'):
                    print(Fore.WHITE + 'Type: ' + Fore.GREEN + str(self.type) + Fore.WHITE)
                elif (self.type == 'Cloudlike'):
                    print(Fore.WHITE + 'Type: ' + Fore.RED + str(self.type) + Fore.WHITE)
                elif (self.type == 'Dessert'):
                    print(Fore.WHITE + 'Type: ' + Fore.YELLOW + str(self.type) + Fore.WHITE)
                elif (self.type == 'Sea Planet'):
                    print(Fore.WHITE + 'Type: ' + Fore.RED + str(self.type) + Fore.WHITE)
                
                if (self.gravity >= 66) and (self.gravity <= 100):
                    print(Fore.WHITE + 'Gravity: ' + Fore.GREEN + str(self.gravity) + '%' + Fore.WHITE)
                elif (self.gravity >= 34) and (self.gravity <= 65):
                    print(Fore.WHITE + 'Gravity: ' + Fore.YELLOW + str(self.gravity) + '%' + Fore.WHITE)
                elif (self.gravity >= 0) and (self.gravity <= 33):
                    print(Fore.WHITE + 'Gravity: ' + Fore.RED + str(self.gravity) + '%' + Fore.WHITE)                    

                if (self.temperature >= -50) and (self.temperature <= -15):
                    print(Fore.WHITE + 'Temperature: ' + Fore.RED + str(self.temperature) + degree_sign + Fore.WHITE)
                elif (self.temperature >= -14) and (self.temperature <= 5):
                    print(Fore.WHITE + 'Temperature: ' + Fore.YELLOW + str(self.temperature) + degree_sign + Fore.WHITE)
                elif (self.temperature >= 6) and (self.temperature <= 30):
                    print(Fore.WHITE + 'Temperature: ' + Fore.GREEN + str(self.temperature) + degree_sign + Fore.WHITE)
                elif (self.temperature >= 31) and (self.temperature <= 50):
                    print(Fore.WHITE + 'Temperature: ' + Fore.YELLOW + str(self.temperature) + degree_sign + Fore.WHITE) 
                elif (self.temperature >= 51) and (self.temperature <= 100):
                    print(Fore.WHITE + 'Temperature: ' + Fore.RED + str(self.temperature) + degree_sign + Fore.WHITE)                                  

                if (self.atmosphere == 'Toxic'):
                    print(Fore.WHITE + 'Atmosphere: ' + Fore.RED + str(self.atmosphere) + Fore.WHITE)
                elif (self.atmosphere == 'Habitable'):
                    print(Fore.WHITE + 'Atmosphere: ' + Fore.GREEN + str(self.atmosphere) + Fore.WHITE)
                elif (self.atmosphere == 'Moderate'):
                    print(Fore.WHITE + 'Atmosphere: ' + Fore.GREEN + str(self.atmosphere) + Fore.WHITE)                                    

                # N/A values
                print(Fore.WHITE + 'Animals: ' + Fore.CYAN + 'N/A' + Fore.WHITE)
                print(Fore.WHITE + 'Water: ' + Fore.CYAN + 'N/A' + Fore.WHITE)
                print(Fore.WHITE + 'Vegetation: ' + Fore.CYAN + 'N/A' + Fore.WHITE)
                print(Fore.WHITE + 'Civilization: ' + Fore.CYAN + 'N/A' + Fore.WHITE)
                return ''

        # change  all planet values randomly
        def change_stats(self):
            self.candidate = self.candidate + 1
            self.name = random.choice(name_list)
            self.gravity = random.randint(1, 100)
            self.type = random.choice(type_list)
            self.temperature = random.randint(-34, 96)
            self.atmosphere = random.choice(atmosphere_list)
            self.animals = random.choice(animals_list)
            self.water = random.choice(water_list)
            self.vegetation = random.choice(vegetation_list)
            self.civilization = random.choice(civilization_list)
            self.unlocked = False
            playsound('planet_found.wav')
#####################################

# START OF THE PROGRAM HERE
start_story()
os.system('cls')
ship_name = input('Type Spaceship Name: ')
os.system('cls')
loadss()
os.system('cls')
spin_loader()
playsound('take_off.mp3')
playsound('planet_found.mp3')
#####################################

# create spaceship object from class Spaceship
spaceship = SpaceShip(
                    name = ship_name,
                    current_event = 0,
                    engine_health =  100,
                    landing_system = 100,
                    pods = 100,
                    data_integrity = 100,
                    navigation_system = 100,
                    life_support = 100,
                    scientific_probes = 10)

SpaceShip.check()

# create planet object from class Planet
planet = SpaceShip.Planet(0, 'name', 'gravity', 'type', 'temperature', 'atmosphere', 'animals', 'water', 'vegetation', 'civilization', False)
#####################################

# current content is new_planet_scene
def new_planet_scene():
    spaceship.Planet.change_stats(planet)
    os.system('cls')
    print(spaceship)
    print(planet)
    SpaceShip.make_choice(spaceship)

# current content is planet_scene
def planet_scene():
    os.system('cls')
    print(spaceship)
    print(planet)
    SpaceShip.make_choice(spaceship)

# current content is landing_scene
def landing_scene():
    os.system('cls')
    green_color()
    print('Landed Succesfuly At:')
    white_color()
    planet.unlocked = True
    print(planet)
    print('---------------------------')
    print(spaceship)
    purple_color()
    print(Fore.MAGENTA + 'Final Score: ' + Fore.LIGHTCYAN_EX + str(score()) + Fore.WHITE)
    white_color()

# current content is disaster_scene
def disaster_scene():
    os.system('cls')
    print(spaceship)
    print('---------------------------')
    red_color()
    choose_disaster_option()
    new_planet_scene()
#####################################

# disasters
def choose_disaster_option():
    spaceship.current_disaster = random.choice(disaster_list)

    # solar flare disaster scenario
    if spaceship.current_disaster == 'solar_flare':
        red_color()
        slowprint('Disaster: Solar Flare')
        white_color()
        fastprint('bla bla bla bla bla bla bla bla bla bla bla ')
        fastprint('bla bla bla bla bla bla bla bla bla bla bla ')
        fastprint('bla bla bla bla bla bla bla bla bla bla bla ')
        display_disaster_options()
    
    # pods malfunction disaster scenario
    elif spaceship.current_disaster == 'pods_malfunction':
        red_color()
        slowprint('Disaster: Pods Malfunction')
        white_color()
        fastprint('bla bla bla bla bla bla bla bla bla bla bla ')
        fastprint('bla bla bla bla bla bla bla bla bla bla bla ')
        fastprint('bla bla bla bla bla bla bla bla bla bla bla ')
        display_disaster_options()

# display disaster memu options
def display_disaster_options():
    blue_color()
    print('1 Let Ship Take The Hit')
    print('2 Try To Escape')
    green_color()
    spaceship.answer = input('Type Choice: ')
    white_color()
    if spaceship.answer == '1':
        dis= random.choice(utilities_list)
        if dis == 'engine_health':
            spaceship.engine_health = spaceship.engine_health - random.randint(11, 17)
        elif dis == 'landing_system':
            spaceship.landing_system = spaceship.landing_system - random.randint(11, 17)
        elif dis == 'pods':
            spaceship.pods = spaceship.pods - random.randint(11, 17)
        elif dis == 'data_integrity':
            spaceship.data_integrity = spaceship.data_integrity - random.randint(11, 17)
        elif dis == 'navigation_system':
            spaceship.navigation_system = spaceship.navigation_system - random.randint(11, 17)
        elif dis == 'life_suppot':
            spaceship.life_support = spaceship.life_support = random.randint(11, 17)

    elif spaceship.answer == '2':
        dis= random.choice(utilities_list)
        if dis == 'engine_health':
            spaceship.engine_health = spaceship.engine_health - random.randint(0, 27)
        elif dis == 'landing_system':
            spaceship.landing_system = spaceship.landing_system - random.randint(0, 27)
        elif dis == 'pods':
            spaceship.pods = spaceship.pods - random.randint(0, 27)
        elif dis == 'data_integrity':
            spaceship.data_integrity = spaceship.data_integrity - random.randint(0, 27)
        elif dis == 'navigation_system':
            spaceship.navigation_system = spaceship.navigation_system - random.randint(0, 27)
        elif dis == 'life_suppot':
            spaceship.life_support = spaceship.life_support = random.randint(0, 27)
    SpaceShip.check()
#####################################

# calculate score
def score():
    score_value = (
        int(spaceship.engine_health) +
        int(spaceship.landing_system) +
        int(spaceship.pods) +
        int(spaceship.data_integrity) +
        int(spaceship.navigation_system) +
        int(spaceship.life_support) +
        int(planet.gravity) +
        int(type_score()) +
        int(temperature_score()) +
        int(atmosphere_score()) +
        int(animals_score()) +
        int(water_score()) +
        int(vegetation_score()) +
        int(civilization_score())
        )
    return score_value

# calculate atmosphere score
def atmosphere_score():
    if planet.atmosphere == 'Toxic':
        return 0
    elif planet.atmosphere == 'Moderate':
        return 25
    elif planet.atmosphere == 'Habitable':
        return 50    

# calculate type score
def type_score():
    if planet.type == 'Rocky':
        return int(50)
    elif planet.type == 'Cloudlike':
        return int(25)
    elif planet.type == 'Dessert':
        return int(0)

# calculate temperature score
def temperature_score():
    return (100 - planet.temperature)

# calculate animal score
def animals_score():
    if planet.animals == 'Not Found':
        return 25
    if planet.animals == 'Edible Animals':
        return 50
    if planet.animals == 'Venomous':
        return 0

# calculate water score
def water_score():
    if planet.water == 'Not Found':
        return 0
    if planet.water == 'Small Deposits':
        return 25
    if planet.water == 'Vast Amounts':
        return 50         

# calculate vegetation score
def vegetation_score():
    if planet.vegetation == 'Not Found':
        return 25
    if planet.vegetation == 'Edible Plants':
        return 50
    if planet.vegetation == 'Toxic Plants':
        return 0

# calculate civilization score
def civilization_score():
    if planet.civilization == 'Not Found':
        return 0
    if planet.civilization == 'Found':
        return 50
    if planet.civilization == 'Old Ruins':
        return 25
#####################################

# unlock full planet stats if scientific pods
# are remaining
def try_probes():
    if planet.unlocked == True:
        planet_scene()
    if spaceship.scientific_probes <= 0:
        playsound('no_more_probes_left.mp3')
        planet_scene()
    elif spaceship.scientific_probes >= 1:
        spaceship.scientific_probes = spaceship.scientific_probes - 1
        planet.unlocked = True
        playsound('probe_sent.mp3')
        planet_scene()

#####################################
#####################################
############ S T A R T ##############
#####################################
#####################################
planet_scene()