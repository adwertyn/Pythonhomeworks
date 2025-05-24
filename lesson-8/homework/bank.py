import random
import json


class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def to_dict(self):
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance
        }
class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()
    def create_account(self, name, initial_deposit):
        account_number = str(random.randint(100000, 999999))
        while account_number in self.accounts:
            account_number = str(random.randint(100000, 999999))
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        self.save_to_file()
        print(f"Account created successfully. Account Number: {account_number}")
    
    def view_account(self, account_number):
        if account_number in self.accounts:
            acc = self.accounts[account_number]
            print(f"Account Number: {acc.account_number}")
            print(f"Name: {acc.name}")
            print(f"Balance: ${acc.balance:.2f}")
        else:
            print("Account not found, please try again")
    
    def deposit(self, account_number, amount):
        if account_number in self.accounts and amount > 0:
            self.accounts[account_number].balance += amount
            self.save_to_file()
            print("Deposit successful.")
        else:
            print("Invalid account or amount.")
            
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            acc = self.accounts[account_number]
            if 0 < amount <= acc.balance:
                acc.balance -= amount
                self.save_to_file()
                print("Withdrawal successful.")
            else:
                print("Insufficient balance or invalid amount.")
        else:
            print("Account not found.")
    
    def save_to_file(self):
        with open("accounts.txt", "w") as f:
            data = {k: v.to_dict() for k, v in self.accounts.items()}
            f.write(json.dumps(data))
    
    def load_from_file(self):
        try:
            with open("accounts.txt", "r") as f:
                content = f.read().strip()
                if content:
                    data = json.loads(content)
                    for acc_num, acc_data in data.items():
                        self.accounts[acc_num] = Account(
                            acc_data["account_number"],
                            acc_data["name"],
                            acc_data["balance"]
                        )
        except FileNotFoundError:
            pass

    
    
bank = Bank()
while True:
    print('''1. Create Account
2. View Account
3. Deposit
4. Withdraw
5. Exit''')
    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter your name: ")
        deposit = float(input("Enter initial deposit: "))
        bank.create_account(name, deposit)
    elif choice == "2":
        acc_num = input("Enter account number: ")
        bank.view_account(acc_num)
    elif choice == "3":
        acc_num = input("Enter account number: ")
        amount = float(input("Enter deposit amount: "))
        bank.deposit(acc_num, amount)
    elif choice == "4":
        acc_num = input("Enter account number: ")
        amount = float(input("Enter withdrawal amount: "))
        bank.withdraw(acc_num, amount)
    elif choice == "5":
        break
    else:
        print("Invalid option.")