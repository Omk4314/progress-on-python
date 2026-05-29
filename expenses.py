import csv
import sys
import os


def main():
    print("\n\tWelcome to expense tracker!")
    print("What would you like to do?")
    main_file = tracker_file()
    while True:
        user_response = input("1.Add expense\n2.View expenses\n3.Delete an expense\nEnter 'q' to quit\n-> ")
        if user_response in ("1", "2", "3", "q"):   
            match user_response:
                case "1":
                    add_expense(main_file)
                case "2":
                    view_expense(main_file)
                case "3":
                    delete_expense(main_file)
                case "q":
                    sys.exit()

def tracker_file():
    file_name = input("Enter the file name you want to save your expenses into: ").strip().title()
    if os.path.isfile(f"{file_name}.csv"):
        print("File Already exists")
    else:
        with open(f"{file_name}.csv", "a") as expense_file:
            column_title = csv.writer(expense_file)
            column_title.writerow(["Category","Expense"])
    return f"{file_name}.csv"

def add_expense(main_file): #Add tracker file function as argument to all the functions
    '''Adds expense category to the csv file in category column and expense in expense column'''
    while True:
        user_category = input("Enter the category of the expense: ").strip().title()
        user_expense = input("Enter your expense: ").strip()
        if user_category.isspace() or user_expense.isspace():
            print("The field cannot be empty")
        elif user_category.isdecimal() or user_expense.isalpha():
            print("Category takes the category of expense!")
            print("Expense takes the expense on the category!")
        else:
            break
    with open(main_file, "a", newline = "") as add_file:
        adder = csv.DictWriter(add_file, fieldnames = ["Category", "Expense"], lineterminator = "\n")
        adder.writerow({"Category": user_category, "Expense": user_expense})

def view_expense(main_file):
    '''Shows the user his expenses'''
    if os.path.isfile(main_file):
        with open(main_file) as view_file:
            viewer = csv.DictReader(view_file)
            for row in viewer:
                print(f"{row['Category']}:- {row['Expense']}")
    else:
        print("No file found!")


def delete_expense(main_file):
    view_expense(main_file)
    if os.path.isfile(main_file):
        ask_user = input("\nEnter the category of the expense you want to delete: ").strip().title()
        with open(main_file) as del_file:
            reader = list(csv.reader(del_file))
            for row in reader:
                if ask_user in row:
                    reader.remove(row)
                else:
                    print("Category not found!")
        with open(main_file, "w", newline = "") as deleted_file:
            writer = csv.writer(deleted_file, lineterminator = "\n")
            writer.writerows(reader)
        print("Deleted")
    else:
        print("No file found!")

    




if __name__ == "__main__":
    main()
