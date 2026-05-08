#Adding a error1, erro2, erro3 variables to make the code readable
error1 = "\nThe password must atleast be 8 characters long"
error2 = "The password must contain atleast an uppercase letter and it must be alphanumeric"
#print the criteria and check if the given password meets the criteria
print("The following is the criteria for a Strong password:")
print(f"{error1}\n{error2}")
while True:
    password = input("\nEnter your password: ")
    #The password should be 8 characters long
    # it should have a uppercase letter and it should be alphanumeric
    if len(password) >= 8 and any(char.isupper() for char in password) and any(char.isdecimal() for char in password):
        print("\nCongrats!, it's a strong password")
        print()
        break
    else:
        print(error1,error2, sep = "\n")
        print()
    
