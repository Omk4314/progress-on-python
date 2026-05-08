#setting an active flag
active = True
#Using while to run the generator as long as the user wants
while active:
    #Take input from the user
    #check if it is positive if not prompt the user Again
    while True:
        number = int(input("\nEnter a number: "))
        if number > 0:
            break
    #Using for loop iterate generate the multiplication table
    print()
    for i in range(10):
        print(f"{number} * {i + 1} = {number * (i + 1)}")
    print()
    #Asking the user if he wants to continue??
    repeat = input("Do you want to enter another number(yes/no)? ").lower()
    if repeat == "no":
        active = False