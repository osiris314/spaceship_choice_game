import itertools
import threading
import time
import sys
from logo_maker import *

def spin_loader():
    green_color()
    done = False
    #here is the animation
    def spinner():
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if done:
                break
            sys.stdout.write('\rInitializing UI... ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('')

    t = threading.Thread(target=spinner)
    t.start()

    #long process here
    time.sleep(8)
    done = True
    white_color()