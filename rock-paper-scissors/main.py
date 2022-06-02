"""
This file is part of the tasks for the Rock-Scissors-Paper game task. It is part of the tasks/projects carried out in the I4GxZuri Scholarship in the Fullstack Track.


Author: Mudassir Adili Ahmad (adilimudassir)
Date: 2022-06-01
"""
import random

options = ['R', 'P', 'S']

while True:
    user = input("Choose your option (R, P or S): ")

    while user not in options:
        print("Invalid option. Please choose again.")
        user = input("Choose your option (R, P or S): ")

    computer = random.choice(options)

    print("Player ({}): Computer ({}).".format(user, computer))

    if user == computer:
        print("It's a tie!")
    elif user == 'R' and computer == 'S':
        print("You win!")
        break
    elif user == 'R' and computer == 'P':
        print("Computer Win!")
        break
    elif user == 'P' and computer == 'R':
        print("You win!")
        break
    elif user == 'P' and computer == 'S':
        print("Computer Win!")
        break
    elif user == 'S' and computer == 'P':
        print("You win!")
        break
    elif user == 'S' and computer == 'R':
        print("Computer Win!")
        break