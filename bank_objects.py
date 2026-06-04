class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.history = [f"Account created with account name: {self.name} and account balance: {self.balance}"]

    def __str__(self):
        return f"BankAccount({self.name}, {self.balance})"

    def __repr__(self):
        return f"BankAccount: (name = {self.name}, balance = {self.balance})"

    def __eq__(self, other):
            if not isinstance(other, BankAccount):
                print("NotImplemented!")
            return self.name == other.name and self.balance == other.balance

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        self.history.append(
            f"Amount {deposit_amount} deposited in {self.name} account. Total Balance = ${self.balance}"
        )
        return self.balance

    def withdraw(self, withdrawal_amount):
        if self.balance >= withdrawal_amount:
            self.balance -= withdrawal_amount
            self.history.append(
                f"Amount {withdrawal_amount} withdrawn from {self.name} account. Total Balance = ${self.balance}"
            )
            return self.balance
        else:
            self.history.append(f"Failed to withdraw ${withdrawal_amount}; insufficient funds")
            return self.balance

    def transfer(self, amount, recipient):
        if isinstance(recipient, BankAccount):
            if self.balance >= amount:
                self.balance -= amount
                recipient.balance += amount
                self.history.append(f"Transferred ${amount} to {recipient.name}")
                recipient.history.append(f"Received ${amount} from {self.name}")
                return self.balance
            else:
                self.history.append("Insufficient funds, failed to transfer")
                return self.balance
        else:
            print("Not a valid bank account!")
            return self.balance

    def get_balance(self):
        return self.balance

    def get_history(self):
        return self.history

    # Getter and setter for balance
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        try:
            self._balance = float(balance)
        except ValueError:
            print("Enter numbers")
            self._balance = 0.0

    # Getter and setter for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            print("Missing name!")
            self._name = "Unnamed"
        else:
            self._name = name


def main():
    # Create accounts
    alice = BankAccount("Alice", 100)
    bob = BankAccount("Bob", 50)

    # Test basic operations
    alice.deposit(25)
    alice.withdraw(10)
    alice.withdraw(200)  # Should fail

    # Test transfer
    alice.transfer(30, bob)

    # Inspect results
    print("Alice balance:", alice.get_balance())   # Expected: 85
    print("Bob balance:", bob.get_balance())       # Expected: 80

    print("\nAlice history:")
    for line in alice.get_history():
        print(line)

    print("\nBob history:")
    for line in bob.get_history():
        print(line)


if __name__ == "__main__":
    main()