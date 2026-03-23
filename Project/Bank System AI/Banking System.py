import json

# Account class 
class Account:
    def __init__(self, account_number, name, balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited {amount}")
            print("Deposit successful")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            print("Withdrawal successful")

    def show_balance(self):
        print(f"Balance: {self.balance}")

    def show_transactions(self):
        print("Transaction History:")
        for t in self.transactions:
            print("-", t)


# Bank class 
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_no, name):
        if acc_no in self.accounts:
            print("Account already exists")
        else:
            self.accounts[acc_no] = Account(acc_no, name)
            print("Account created")

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)

    def save_data(self):
        data = {
            acc_no: {
                "name": acc.name,
                "balance": acc.balance,
                "transactions": acc.transactions
            }
            for acc_no, acc in self.accounts.items()
        }

        with open("./Python/Project/bank_data.json", "w") as f:
            json.dump(data, f)

    def load_data(self):
        try:
            with open("./Python/Project/bank_data.json", "r") as f:
                data = json.load(f)

            for acc_no, details in data.items():
                acc = Account(acc_no, details["name"], details["balance"])
                acc.transactions = details["transactions"]
                self.accounts[acc_no] = acc

        except FileNotFoundError:
            pass
        
bank = Bank()
bank.load_data()

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Balance")
    print("5. Transactions")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        acc_no = input("Account number: ")
        name = input("Name: ")
        bank.create_account(acc_no, name)

    elif choice == "2":
        acc_no = input("Account number: ")
        acc = bank.get_account(acc_no)
        if acc:
            amount = float(input("Amount: "))
            acc.deposit(amount)

    elif choice == "3":
        acc_no = input("Account number: ")
        acc = bank.get_account(acc_no)
        if acc:
            amount = float(input("Amount: "))
            acc.withdraw(amount)

    elif choice == "4":
        acc_no = input("Account number: ")
        acc = bank.get_account(acc_no)
        if acc:
            acc.show_balance()

    elif choice == "5":
        acc_no = input("Account number: ")
        acc = bank.get_account(acc_no)
        if acc:
            acc.show_transactions()

    elif choice == "6":
        bank.save_data()
        print("Data saved. Exiting...")
        break