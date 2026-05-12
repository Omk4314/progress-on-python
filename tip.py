def main():
    #Ask user to input bill, tip, people
    bill = input("Enter total bill: ").strip()
    tip = input("How much tip would you like to give?: ").strip()
    people = input("Enter number of people: ").strip()
    per_person = calculate(bill, tip, people)
    print(f"Each person must cobntribute {per_person}$.")

def calculate(bill, tip, people):
    #Convert from str to int and calculate the split
    if "$" in bill:
        bill = bill.removesuffix("$")
    bill = float(bill)
    if "%" in tip:
        tip = tip.removesuffix("%")
    tip = int(tip) / 100
    people = int(people)
    return round((bill + (bill * tip)) / people, 2)

main()