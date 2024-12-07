class BankAccount:
    def __init__(self, account_number, owner):
        self.account_number = account_number
        self.owner = owner
        self.balance = 0.00
    
    def deposit(self, amount):
        if amount <=0:
            print("Error: Deposit amount must be greater than zero.")
        else:
            self.balance += amount
            print(f"An amount of {amount}$ has been deposited to account: {self.account_number}. Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <=0:
            print("Error: Withdrawal amount must be greater than zero.")
        else:
            if self.balance < amount:
                print("Error: Not enough funds in the account.")
            else:
                self.balance -= amount
                print(f"An amount of {amount}$ has been withdrawn to account: {self.account_number}. Balance: {self.balance}")

    def show_balance(self):
        print(f"Account {self.account_number} owned by {self.owner} has a balance of {self.balance}$")

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Added new account: {account.account_number}")
    
    def find_account(self, search_num):
        for account in self.accounts:
            if account.account_number == search_num:
                print(f"Account found: {account.owner} - {account.account_number} - Balance: {account.balance}$")
                return account
        print("No account matching the search was found.")
        return None

    def transfer(self, from_account, to_account, amount):
        if amount <=0:
            print("Error: Transfer amount must be greater than zero.")
            return

        sender = self.find_account(from_account)
        recipient = self.find_account(to_account)

        if not sender:
            print(f"Error: Sender account {from_account} not found.")
        elif not recipient:
            print(f"Error: Recipient account {to_account} not found.")
        elif sender.balance < amount:
            print(f"Error: Not enough funds in sender's account {from_account}.")
        else:
            sender.withdraw(amount)
            recipient.deposit(amount)
            print(f"Successfully transferred {amount}$ from account {from_account} to account {to_account}.")

            
 
                   
                


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
bank.transfer(11111, 22222, 200)
bank.transfer(22222, 33333, 3000)
bank.transfer(33333, 44444, -500)
bank.transfer(44444, 55555, 0)
bank.transfer(55555, 11111, 222)


