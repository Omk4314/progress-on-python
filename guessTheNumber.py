import random

#declaring game state variable 
gameRunning = True

#Ask the user for difficulty and then set the range according to the difficulty selected
difficulty = input("Choose difficulty:\n\tEasy\n\tMedium\n\tHard\n").title()
x = 1
match difficulty:
    case "Easy":
          y = 100
    case "Medium":
         y = 500
    case "Hard":
         y = 1000
    case _:
        print("Invalid input: Please select from the given choices!")

#Generating random number and storing it in a variable
randomNumber = random.randint(x, y)
#Asking the user for input of the number
number = int(input("What's the number I am thinking about?: "))
#Tracking attempt's taken by user to guess the number
attempt = 1

while gameRunning == True:
    if number == randomNumber:
        print("Correct, you got me!")
        gameRunning = False
    elif number > randomNumber:
        print("too high")
        number = int(input("Guess Again: "))
        attempt += 1
    else:
        print("too low")
        number = int(input("Guess Again: "))
        attempt += 1
print(f"You took {attempt} attempts to guess the number!")