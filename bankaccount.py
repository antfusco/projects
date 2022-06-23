class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account Owner:   {self.owner}\n\nAccount Balance: {self.balance}'

    def deposit(self, amount):
        self.balance += amount
        print('Deposit Accepted')
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            print('FUNDS UNAVAILABLE')
        else:
            self.balance -= amount
            print('Withdrawl Accepted')
            return self.balance
