#Asking for input from user
x = input("What's x? ")
y = input("What's y? ")
#Check if the user's input is a digit
if x.isdecimal() and y.isdecimal() :
    x = int(x)
    y = int(y)
    #Display arthematic opreations on the screen
    print(x + y) 
    print(x - y)
    print(x * y)
    if y == 0 :
        print("Cannot divide by zero")
    else:
        print(x / y)
else:
    print("Invalid input!!")


    