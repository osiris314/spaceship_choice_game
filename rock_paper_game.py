import random
import os

os.system('cls')
while True:
    a = True
    list  = ["scissors", "paper", "rock", "lizard", "spock"]
    pc = random.choice(list)
    choice = "a"

    #print (pc)
    choic = int(input("Enter the number: 1.scissors 2.paper 3.rock 4.lizard 5.spock: "))

    if (choic == 1):
        choice = "scissors"
    elif (choic == 2):
        choice = "paper"
    elif (choic == 3):
        choice = "rock"
    elif (choic == 4):
        choice = "lizard"
    elif (choic == 5):
        choice = "spock"
    else:
        print("Type a valid number...")

    #scissors
    if (choice == "scissors" and pc == "lizard"):
        print ('\033[1;32mScissors decapitates Lizard\033[1;m')
    if (choice == "lizard" and pc == "scissors"):
        print ('\033[1;31mScissors decapitates Lizard\033[1;m')
    if (choice == "scissors" and pc == "paper"):
        print ('\033[1;32mScissors cuts Paper\033[1;m')
    if (choice == "paper" and pc == "scissors"):
        print ('\033[1;31mScissors cuts Paper\033[1;m')
    if (choice == "scissors" and pc == "scissors"):
        print ('\033[1;33mIt is a Tie\033[1;m')

    #Paper
    if (choice == "paper" and pc == "rock"):
        print ('\033[1;32mPaper covers rock\033[1;m')
    if (choice == "rock" and pc == "paper"):
        print ('\033[1;31mPaper covers rock\033[1;m')
    if (choice == "paper" and pc == "spock"):
        print ('\033[1;32mPaper disproves Spock\033[1;m')
    if (choice == "spock" and pc == "paper"):
        print ('\033[1;31mPaper disproves Spock\033[1;m')
    if (choice == "paper" and pc == "paper"):
        print ('\033[1;33mIt is a Tie\033[1;m')
 
    #rock   
    if (choice == "rock" and pc == "scissors"):
        print ('\033[1;32mRock crushes Scissors\033[1;m')
    if (choice == "scissors" and pc == "rock"):
        print ('\033[1;31mRock crushes Scissors\033[1;m')
    if (choice == "rock" and pc == "lizard"):
        print ('\033[1;32mRock smashes Lizard\033[1;m')
    if (choice == "lizard" and pc == "rock"):
        print ('\033[1;31mRock smashes Lizard\033[1;m')
    if (choice == "rock" and pc == "rock"):
        print ('\033[1;33mIt is a Tie\033[1;m')

    #lizard
    if (choice == "lizard" and pc == "spock"):
        print ('\033[1;32mLizard poisons Spock\033[1;m')
    if (choice == "spock" and pc == "lizard"):
        print ('\033[1;31mLizard poisons Spock\033[1;m')
    if (choice == "lizard" and pc == "paper"):
        print ('\033[1;32mLizard eats Paper\033[1;m')
    if (choice == "paper" and pc == "lizard"):
        print ('\033[1;31mLizard eats Paper\033[1;m')
    if (choice == "lizard" and pc == "lizard"):
        print ('\033[1;33mIt is a Tie\033[1;m')

    #spock
    if (choice == "spock" and pc == "rock"):
        print ('\033[1;32mSpock vaporizes Rock\033[1;m')
    if (choice == "rock'" and pc == "spock"):
        print ('\033[1;31mSpock vaporizes Rock\033[1;m')
    if (choice == "spock" and pc == "scissors"):
        print ('\033[1;32mSpock smashes scissors\033[1;m')
    if (choice == "scissors" and pc == "spock"):
        print ('\033[1;31mSpock smashes scissor\033[1;m')
    if (choice == "spock" and pc == "spock"):
        print ('\033[1;33mIt is a Tie\033[1;m')

    print('\n')
