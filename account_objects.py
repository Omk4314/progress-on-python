from bank_account import BankAccount
class CheckingAccount(BankAccount):
    def __init__(self, name, balance, overdraft_limit = 16):
        super().__init__(name, balance)
        self.overdraft_limit = overdraft_limit

    def __str__(self):
        return f"This is the Checking Account, the name of the owner is {self.name} and the balance is {self.balance}."

    def __repr__(self):
        return f"Checking Account: (name = {self.name}, balance = {self.balance}, overdraft_limit = {self.overdraft_limit})"

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.history.append(f"Amount {amount} withdrawn from {self.name} account. Total Balance = ${self.balance}")
            return self.balance
        else:
            if self.balance - amount -35 < -self.overdraft_limit:
                self.history.append(f"Withdrawal rejected! exceeded the overdraft limit")
                return self.balance
            self.balance -= (amount + 35)
            self.history.append(f"Overdraft: Withdrew ${amount} with $35 fee. New balance: ${self.balance}")
            return self.balance

    def transfer(self, amount, recipient):
        if isinstance(recipient, BankAccount):
            if self.balance >= amount:
                self.balance -= amount
                recipient.balance += amount
                self.history.append(f"Transferred ${amount} to {recipient.name}")
                recipient.history.append(f"Received ${amount} from {self.name}")
                return self.balance
            self.balance -= (amount + 35)
            self.history.append(f"Overdraft: Tansferred ${amount} with $35 fee to {recipient.name}. New balance: ${self.balance}")
            recipient.balance += amount
            self.history.append(f"Received ${amount} from {self.name}")
            return self.balance
        else:
            print("Not a valid bank account!")
            return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, name, balance, intrest_rate = 0.02):
        super().__init__(name, balance)
        self.intrest_rate = intrest_rate

    def __str__(self):
        return f"This is the Savings Account, the name of the owner is {self.name} and the balance is {self.balance}."

    def __repr__(self):
        return f"Savings Account: (name = {self.name}, balance = {self.balance}, intrest_rate = {self.intrest_rate})"

    def apply_intrest(self):
        intrest = self.balance * self.intrest_rate
        self.balance += intrest
        self.history.append(f"Interest applied: ${intrest}. New balance: ${self.balance}")
        return self.balance



def main():
    
    # --- Checking Account Tests ---
    print("=== Checking Account ===")
    checking = CheckingAccount("Alice", 100, overdraft_limit=100)

    checking.withdraw(50)      # Normal: balance 50
    checking.withdraw(80)      # Overdraft: balance -65 (80 + 35 fee)
    checking.withdraw(100)     # Exceeds overdraft limit: should fail, balance stays -65
    checking.deposit(20)       # Balance -45

    print("Checking balance:", checking.get_balance())  # Expected: -45
    print("Checking history:")
    for line in checking.get_history():
        print(line)

    # --- Savings Account Tests ---
    print("\n=== Savings Account ===")
    savings = SavingsAccount("Bob", 1000, intrest_rate=0.05)
    savings.apply_intrest()     # Balance 1050
    savings.withdraw(2000)       # Should fail (no overdraft)
    savings.withdraw(50)         # Balance 1000

    print("Savings balance:", savings.get_balance())  # Expected: 1000
    print("Savings history:")
    for line in savings.get_history():
        print(line)

    # --- Cross-account Transfer ---
    print("\n=== Cross-Account Transfer ===")
    checking2 = CheckingAccount("Charlie", 50, overdraft_limit=100)
    savings2 = SavingsAccount("Dana", 200, intrest_rate=0.02)

    checking2.transfer(75, savings2)   # Charlie overdrafts by 25 + 35 fee. Dana receives 75.
    print("Charlie balance:", checking2.get_balance())   # Expected: -60
    print("Dana balance:", savings2.get_balance())       # Expected: 275

if __name__ == "__main__":
    main()