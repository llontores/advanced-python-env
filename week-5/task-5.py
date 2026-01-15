class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, money):
        self.balance += money

    def withdraw(self, money):
        if money <= self.balance:
            self.balance -= money
        else:
            print("Not enough money")


account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)

print(account.balance)
