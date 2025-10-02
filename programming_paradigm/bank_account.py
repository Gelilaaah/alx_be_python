class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the balance"""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if sufficient funds exist"""
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current balance"""
        print(f"Current Balance: ${self.account_balance}")
