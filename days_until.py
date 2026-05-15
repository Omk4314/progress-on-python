from datetime import date
#Take input from user for target
while True:
    try:
        user_input = int(input("Enter you target date in (dd/mm/yyyy): "))
        day, month, year = user_input.split("/")
    except (ValueError, AttributeError):
        print("Enter the date, month, year in dd/mm/yyyy format")
    else:
        break

    
target = date(year, month, day)
now = date.today()
days_until = target - now
print(f"There are {days_until.days} days until {user_input}")