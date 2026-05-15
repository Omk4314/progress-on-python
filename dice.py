from random import randint
import sys


previous_values = []
global value


def roll():
    '''Checks the user input and then rolls the dice and stores the value in history'''
    while True:
        while True:
            roll_dice = input("Roll the dice?(yes/ no) [press h to view history] ").strip().lower()
            if roll_dice == "yes" or roll_dice == "no" or roll_dice == "h":
                break
        if roll_dice == "no":
            sys.exit()
        elif roll_dice == "h":
            if previous_values:
                check_history()
            else:
                print("There is no history")
        else:
            value = randint(1, 6)
            print(value)
            history(value)


def history(store):
    previous_values.append(store)


def check_history():
    print(previous_values)

#Calling the roll function
roll()