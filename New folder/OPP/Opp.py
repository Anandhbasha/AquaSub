# Abstraction - Parent Class
class Account:
    def __init__(self, acc_number, name, balance):
        self.acc_number = acc_number
        self.name = name
        self._balance = balance  # Protected
        self.__bank_code = "TMB1234"  # Private

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"₹{amount} deposited. New Balance: ₹{self._balance}")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        raise NotImplementedError("Withdraw must be implemented in subclass")

    def get_bank_code(self):  # Getter for private variable
        return self.__bank_code

    def display(self):
        raise NotImplementedError("Display method must be overridden")


# Inheritance & Polymorphism - Child Class 1
class SavingsAccount(Account):
    def __init__(self, acc_number, name, balance, interest_rate):
        super().__init__(acc_number, name, balance)
        self.interest_rate = interest_rate

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds")
        else:
            self._balance -= amount
            print(f"₹{amount} withdrawn. Remaining Balance: ₹{self._balance}")

    def calculate_interest(self):
        interest = self._balance * self.interest_rate / 100
        print(f" Interest Earned: ₹{interest}")
        return interest

    def display(self):
        print(f"\n [Savings Account] {self.name}")
        print(f"Account No: {self.acc_number}")
        print(f"Balance: ₹{self._balance}")
        print(f"Bank Code (Private): {self.get_bank_code()}")


# Inheritance & Polymorphism
class CurrentAccount(Account):
    def __init__(self, acc_number, name, balance, overdraft_limit):
        super().__init__(acc_number, name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self._balance + self.overdraft_limit:
            print(" Overdraft limit exceeded")
        else:
            self._balance -= amount
            print(f"₹{amount} withdrawn. Remaining Balance: ₹{self._balance}")

    def display(self):
        print(f"\n [Current Account] {self.name}")
        print(f"Account No: {self.acc_number}")
        print(f"Balance: ₹{self._balance}")
        print(f"Bank Code (Private): {self.get_bank_code()}")

if __name__ == "__main__":
    # Savings Account
    sa = SavingsAccount("SA1001", "Kumaran", 8000, 5)
    sa.display()
    sa.deposit(2000)
    sa.withdraw(3000)
    sa.calculate_interest()

    #  Current Account
    ca = CurrentAccount("CA2002", "Mohan", 5000, 2000)
    ca.display()
    ca.withdraw(6000)  # Within limit
    ca.withdraw(2000)  # Cross limit