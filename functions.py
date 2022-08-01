from slowprint import *
from colorama import Fore, Style
import os
import pyfiglet
from loading_bar import *
from spinner import *
ascii_banner = pyfiglet.figlet_format("AIDA")#<~~~~~~ TYPE LOGO HERE

def green_logo():
    green_color()
    print(ascii_banner)
    white_color()
def start_story():
    slowprint('Time left: 11 days to impact')
    fastprint('NASA scientists detect a type 3 asteroid named Apophis with a sticking course for Earth. Impact estimated to hit')
    fastprint(' 28, June 2022. First estimations point the impact location Alaska, USA.\n')

    slowprint('Time left: 10 days to impact')
    fastprint('Top scientists say the asteroid is too close to Earth to deflect at this point.')
    fastprint('Best plan is to build  spaceships in order to transport humans to an other solar system.')
    fastprint('Most likely Proxima Centuri the closest star to ours.\n')

    slowprint('Time left: 1 day to impact')
    fastprint('Spaceships all over the world  launched into the sky for a new home')
    fastprint('Leaving behind 6.350.834.532 people.\n')

    slowprint('Time left: 0 days to impact')
    fastprint('Asteroid Apophis collides with Earth leaving behind a 250.000 crater.')
    fastprint('7 hours later the wall of fire travelled to the other side of the globe')
    fastprint('and burned every single oxygen molecule in the atmosphere.')
    fastprint('Making Earth from a life fairing planet to a hostile one.\n')

    slowprint('Time left: 8 days after impact')
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

def start_story():
    slowprint('Time left: 11 days to impact')
    fastprint('NASA scientists detect a type 3 asteroid named Apophis with a sticking course for Earth. Impact estimated to hit')
    fastprint(' 28, June 2022. First estimations point the impact location Alaska, USA.\n')

    slowprint('Time left: 10 days to impact')
    fastprint('Top scientists say the asteroid is too close to Earth to deflect at this point.')
    fastprint('Best plan is to build  spaceships in order to transport humans to an other solar system.')
    fastprint('Most likely Proxima Centuri the closest star to ours.\n')

    slowprint('Time left: 1 day to impact')
    fastprint('Spaceships all over the world  launched into the sky for a new home')
    fastprint('Leaving behind 6.350.834.532 people.\n')

    slowprint('Time left: 0 days to impact')
    fastprint('Asteroid Apophis collides with Earth leaving behind a 250.000 crater.')
    fastprint('7 hours later the wall of fire travelled to the other side of the globe')
    fastprint('and burned every single oxygen molecule in the atmosphere.')
    fastprint('Making Earth from a life fairing planet to a hostile one.\n')

    slowprint('Time left: 8 days after impact')
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


def start_ship():
    os.system('cls')
    green_logo()
    green_color()
    fastprint('Type Your Credentials')
    white_color()

    
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
    os.system('cls')