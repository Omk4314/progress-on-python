import csv
import json
import os
import re
import sys

def main():
    '''Main function'''
    print("===Personal Finance Tracker===")
    print("What would youy like to do?")
    print("SELECT THE CORRESPONDING NUMBER FOR THE GIVEN OPREATION")
    while True:
        while True:
            usr_response = input("1. Add Transaction\n2. View Monthly Report\n3. Export Report To CSV\n4.Delete Transaction\n5.Delete Report\n6.Exit\n--> ").strip()
            if usr_response in ("1", "2", "3", "4", "5"):
                break
        match usr_response:
            case "1":
                add_transaction()
            case "2":
                view_report()
            case "3":
                export_report()
            case "4":
                delete_trans()
            case "5":
                delete_report()
            case "6":
                sys.exit()


def add_transaction():
    '''Adds the user transaction to a file as a dictionary'''
    while True:
        input_date = input("Enter the transaction date(dd/mm/yyyy): ").strip()
        if re.search(r"^\d{1,2}/ ?\d{1,2}/ ?\d{4}$", input_date):
            trans_date = input_date
            break
        else:
            print("Enter date in dd/mm/yyyy format!")
    while True:
        trans_type = input("Is it income or expense? ").strip().lower()
        if trans_type in ("income", "expense"):
            break
    
    trans_category = input("Enter the category you did the transaction for: ").strip().title()

    while True:
        try:
            trans_amount = float(input("Enter transaction amount: ").strip())
            break
        except ValueError:
            print("Enter the numbers!")
    
    while True:
        ask_user = input("Do you want to add a description[Y/N]? ").strip().upper()
        if ask_user in ("Y", "N"):
            break
    if ask_user == "Y":
        trans_descrp = input("Enter transaction description\n--> ")
    else:
        trans_descrp = None
    
    transaction = {"date": trans_date, "type": trans_type, "category": trans_category, "amount": trans_amount, "description": trans_descrp}
    with open("report.txt", "a") as report_file:
        report_file.write(f"{json.dumps(transaction)}\n")


def view_report():
    '''Shows monthy income and monthly expense and net balance and returns the user input'''
    view_income = []
    view_expense = []
    total_income = 0
    total_expense = 0
    while True:
        view_month = input("Enter the month and year of the transaction(mm/yyyy): ").strip()
        if re.search(r"^\d{1,2}/ ?\d{4}$", view_month):
            break
        else:
            print("Enter in the mm/yyyy format!")
    with open("report.txt") as view_file:
        lines = view_file.readlines()
        if not lines:
            print("No Transactions To View!")
        else:
            for trans_dict in lines:
                view_dict = json.loads(trans_dict)
                if view_month == re.search(r"^\d{1,2}/ ?(\d{1,2}/ ?\d{4})$", view_dict['date']).group(1):
                    if view_dict['type'] == "income":
                        view_income.append(f"\t{view_dict['category']}: {view_dict['amount']}\n")
                        total_income += view_dict['amount']
                    else:
                        view_expense.append(f"\t{view_dict['category']}: {view_dict['amount']}\n")
                        total_expense += view_dict['amount']

                    print(f"===REPORT FOR {view_month}===")
                    for income_trans in view_income:
                        print("Income:")
                        print(income_trans)
                    print(f"Total Income: ${total_income}")
                    for expense_trans in view_expense:
                        print("Expenses: ")
                        print(expense_trans)
                    print(f"Total Expenses: ${total_expense}\n")
                    print(f"Net Balance: ${total_income - total_expense}")
        return view_month, total_income, total_expense

    
def export_report():
    '''Exports monthly report to csv'''
    trans_month, total_income, total_expense = view_report()
    safe_month = trans_month.replace("/", "_")
    if total_income == 0 and total_expense == 0:
        print("No Transactions to Export!")
    else:
        if os.path.isfile(f"Report_{safe_month}.csv"):
            print("Report already exported!")
        else:
            with open(f"Report_{safe_month}.csv", "a", newline = "") as export_file:
                writer = csv.DictWriter(export_file, fieldnames = ["Type", "Category", "Description", "Amount"], lineterminator = "\n")
                writer.writeheader()
                with open("report.txt") as info_file:
                    for info_dict in info_file.readlines():
                        new_dict = json.loads(info_dict)
                        if trans_month == re.search(r"^\d{1,2}/ ?(\d{1,2}/ ?\d{4})$", new_dict['date']).group(1):
                            writer.writerow({'Type': new_dict['type'], 'Category': new_dict['category'], 'Description': new_dict['description'], 'Amount': new_dict['amount']})

                total_writer = csv.writer(export_file, lineterminator = "\n")
                total_writer.writerows([[None, None, "Total Income", total_income],
                                        [None, None, "Total Expense", total_expense],
                                        [None, None, "Net Balance", total_income - total_expense]])    
                

def delete_trans():
    delete_cat = input("Enter category of the transaction you want to delete: ").strip()
    delete_date = input("Enter the date of the transaction you want to delete(dd/mm/yyyy)")
    remaining_trans = []
    if os.path.isfile("report.txt"):
        with open("report.txt") as del_file:
            trans_lines = del_file.readlines()
            for trans_line in trans_lines:
                Dict = json.loads(trans_line)
                if delete_cat not in Dict.values() and delete_date not in Dict.values():
                    remaining_trans.append(Dict)
        
        with open("report.txt", "W") as new_file:
            for data in remaining_trans:
                new_file.write(f"{json.dumps(data)}\n")
    else:
        print("No transaction to delete try adding a transaction!")

def delete_report():
    ask_report = input("Enter the name of the report you want to delete: ")
    if os.path.isfile(f"{ask_report}.csv"):
        os.remove(f"{ask_report}.csv")
    else:
        print("NO Report Found With The Given Name")
if __name__ == "__main__":
    main()