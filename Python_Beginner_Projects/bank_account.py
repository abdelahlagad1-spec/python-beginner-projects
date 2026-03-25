class BankAccount:
    def __init__(self, number, balance=0):
        self.number = number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}, New Balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}, New Balance: ${self.balance}")
        else:
            print("Insufficient funds")

    def show_balance(self):
        print(f"Account {self.number}, Balance: ${self.balance}")

account = BankAccount("12345")
account.deposit(1000)
account.withdraw(500)
account.show_balance()