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
        if amount <=0:
            print("Error: Insufficient funds to withdraw")
        else:
            if self.balance < amount:
                print("Error: Not enough funds in the account.")
            else:
                self.balance -= amount
                print(f"An amount of {amount}$ has been withdrawn")

    def show_balance(self):
        print(self.balance)

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Added new account: {account.account_number}")
    
    def find_account(self, search_num):
        found = False
        for account in self.accounts:
            if str(search_num) in str(account.account_number):
                print(f"{account.owner} - {account.account_number} - Balance: {account.balance}")
                found = True
        if not found:
            print("No account matching the search was found.")

    #TO DO - przepisac funkcje transfer z uzyciem funkcji find_account
    def transfer(self, from_account, to_account, amount):
        if amount <=0:
            print("Error: Insufficient funds to transfer")
        else:
            for s_account in self.accounts:
                if s_account.account_number != from_account:
                    print("We could not locate the sender's account. Please verify the account details and try again.!")
                else:
                    if s_account.balance < amount:
                        print("Not enough funds in the sender's account.")
                    else:
                        for r_account in self.accounts:
                            if r_account != to_account:
                                print("We could not locate the recipient's account. Please verify the account details and try again.!")
                            else:
                                s_account.withdraw(amount)
                                r_account.deposit(amount)


ba1 = BankAccount(11111, "Jan Kowalski")
ba2 = BankAccount(22222, "Henryk Suchy")
ba3 = BankAccount(33333, "Anna Dzik")
ba4 = BankAccount(44444, "Barbara Lewa")
ba5 = BankAccount(55555, "John Smith")

ba1.deposit(5000)
ba2.deposit(5000)
ba3.deposit(5000)
ba4.deposit(5000)
ba5.deposit(5000)


ba1.withdraw(225)
ba2.withdraw(-5)
ba3.withdraw(0)
ba4.withdraw(2250)
ba5.withdraw(5000)

ba1.show_balance()
ba2.show_balance()
ba3.show_balance()
ba4.show_balance()
ba5.show_balance()

bank = Bank()

bank.add_account(ba1)
bank.add_account(ba2)
bank.add_account(ba3)
bank.add_account(ba4)
bank.add_account(ba5)

bank.find_account(22222)
"""bank.transfer(11111, 22222, 5000)
bank.transfer(22222, 33333, 200)
bank.transfer(33333, 44444, -200)
bank.transfer(44444, 55555, 0)
bank.transfer(55555, 11111, 222)
"""

