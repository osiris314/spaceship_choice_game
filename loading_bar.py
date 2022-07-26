import time
import tqdm
from logo_maker import *
from random import *
from colorama import *
from slowprint import *
#######################################
def work1():
    time.sleep(random())
def work2():
    time.sleep(random())
def work3():
    time.sleep(random())
def work4():
    time.sleep(random())
def work5():
    time.sleep(random())
def work6():
    time.sleep(random())
def work7():
    time.sleep(random())
def work8():
    time.sleep(random())
def work9():
    time.sleep(random())
def work10():
    time.sleep(random())
def work11():
    time.sleep(random())
def work12():
    time.sleep(random())

########################################
def power_worker():
    power_work_set = [work1, work2, work3, work4, work5, work6, work7, work8, work9, work10]
    return power_work_set

def mechanics_worker():
    mechanics_work_set = [work1, work2, work3, work4, work5, work6, work7, work8]
    return mechanics_work_set

def life_support_worker():
    life_support_work_set = [work1, work2, work3, work4, work5, work6]
    return life_support_work_set

def navigation_worker():
    navigation_work_set = [work1, work2, work3, work4, work5, work6, work7, work8, work9]
    return navigation_work_set

def communication_worker():
    communication_work_set = [work1, work2, work3, work4, work5, work6, work7, work8, work9, work10, work11, work12]
    return communication_work_set

def system_integrity_worker():
    system_integrity_work_set = [work1, work2, work3, work4, work5, work6, work7, work8]
    return system_integrity_work_set
##################################
def green_loading_bar():
    print(Fore.GREEN)
    a = power_worker()
    for i in tqdm.tqdm(range(10)):
        b = a[i]()

def red_loading_bar():
    print(Fore.RED)
    a = mechanics_worker()
    for i in tqdm.tqdm(range(8)):
        b = a[i]()

def blue_loading_bar():
    print(Fore.BLUE)
    a = life_support_worker()
    for i in tqdm.tqdm(range(6)):
        b = a[i]()

def yellow_loading_bar():
    print(Fore.YELLOW)
    a = navigation_worker()
    for i in tqdm.tqdm(range(9)):
        b = a[i]()

def magenta_loading_bar():
    print(Fore.MAGENTA)
    a = communication_worker()
    for i in tqdm.tqdm(range(12)):
        b = a[i]()

def white_loading_bar():
    print(Fore.WHITE)
    a = system_integrity_worker()
    for i in tqdm.tqdm(range(8)):
        b = a[i]()

def test_loading_bars():
    green_loading_bar()
    red_loading_bar()
    blue_loading_bar()
    yellow_loading_bar()
    white_loading_bar()
##################################
def loadss():
    green_color()
    fastprint('Power Management')
    green_loading_bar()

    red_color()
    fastprint('Mechanics')
    red_loading_bar()

    blue_color()
    fastprint('Life Support')
    blue_loading_bar()

    yellow_color()
    fastprint('Navigation')
    yellow_loading_bar()

    magenta_color()
    fastprint('Communications')
    magenta_loading_bar()

    white_color()
    fastprint('Overall System Integrity')
    white_loading_bar()

