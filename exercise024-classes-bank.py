class BankAccount:
    def __init__(self, account_number, owner):
        self.account_number = account_number
        self.owner = owner
        self.balance = 0.0
    
    def deposit(self, amount):
        if amount <=0:
            print("Error: Insufficient funds to deposit")
        else:
            self.balance += amount
            print(f"An amount of {amount}$ has been deposited")
    def withdraw(self, amount):
        if self.balance <= amount:
            print("Error: Not enough funds in the account.")
        else:
            self.balance -= amount
            print(f"An amount of {amount}$ has been withdrawn")
    def show_balance(self):
        print(self.balance)

b1 = BankAccount("001", "Jan Kowalski")
b1.deposit(500)
print(b1.balance)
b1.withdraw(225)
b1.show_balance()