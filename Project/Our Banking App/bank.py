import json
import os
import random
import string

class Account:
    def account_number(self):
        digits = [str(random.randint(0, 9)) for _ in range(4)]
        alphabets = [random.choice(string.ascii_lowercase) for _ in range(3)]    
        letters = [random.choice(string.ascii_letters) for _ in range(3)]    

        combined = digits + alphabets + letters

        random.shuffle(combined)
        return "".join(combined)
    
    def __init__(self, name , age , contact , location , cnic , password):
        self.acc_number = self.account_number()
        self.name = name
        self.password = password
        self.age = age
        self.contact = contact
        self.location = location
        self.cnic = cnic
        self.balance = 0
        
    
class Bank:
    def __init__(self):
        self.accounts = []
        
        
    def create_account(self):
        name = input("Enter your Name: ")
        contact = int(input("Enter your Phone Number: "))
        age = int(input("Enter your Age: "))
        
        if age < 18:
            print("You are not eligible to open an account")
            return
        
        location = input("Enter your Location: ")
        cnic = int(input("Enter your CNIC Number: "))
        password = str(input("Enter your Account Password: "))
        user = Account(name , age , contact , location , cnic , password)
        
        user_data = {
            "Account Number":user.acc_number,
            "Password":user.password,
            "Name":user.name,
            "Age":user.age,
            "Contact":user.contact,
            "Location":user.location,
            "CNIC":user.cnic,
            "Balance":user.balance
        }
        
        file_path = "./Python/Project/Our Banking App/bank_data.json"
        
        # Load existing data
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                try:
                    data = json.load(f)
                except:
                    data = {"accounts": []}
        else:
            data = {"accounts": []}

        data["accounts"].append(user_data)

        # Save updated data
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)

        f.close()
        print("Account Created Successfully")
        
        print("***********************************************************************")
        print("Account Details: \n")
        print(f"Account Number: {user.acc_number}")
        print(f"Name: {user.name}")
        print(f"Age: {user.age}")
        print(f"Contact: {user.contact}")
        print(f"Location: {user.location}")
        print(f"CNIC: {user.cnic}")
        print(f"Balance: {user.balance} \n")
        print("Note Your Account Number")
        print("***********************************************************************")
        
    def deposit(self):
        accout_number = str(input("Enter your Account Number: "))
        account_password = str(input("Enter your Account Password: "))
        
        with open("./Python/Project/Our Banking App/bank_data.json", "r") as f:
            data = json.load(f)
        
            found = False
            
            for acc in data["accounts"]:
                if acc["Account Number"] == accout_number and acc["Password"] == account_password:
                    amount = int(input("Enter the amount you want to deposit: "))
                    acc["Balance"] += amount
                    found = True
                    break
            
            if not found:                   
                print("Account not found")
                return
        f.close()
            
        with open("./Python/Project/Our Banking App/bank_data.json", "w") as f:
            json.dump(data, f, indent=4)
        f.close()
            
        
    def withdraw(self):
        accout_number = str(input("Enter your Account Number: "))
        account_password = str(input("Enter your Account Password: "))
        
        with open("./Python/Project/Our Banking App/bank_data.json", "r") as f:
            data = json.load(f)
        
            found = False
            
            for acc in data["accounts"]:
                if acc["Account Number"] == accout_number and acc["Password"] == account_password:
                    amount = int(input("Enter the amount you want to Withdraw: "))
                    if amount < acc["Balance"] or amount == acc["Balance"]:
                        acc["Balance"] -= amount
                    else:
                        print("Insufficient balance")
                    found = True
                    break
            
            if not found:                   
                print("Account not found")
                return
        f.close()
            
        with open("./Python/Project/Our Banking App/bank_data.json", "w") as f:
            json.dump(data, f, indent=4)
        f.close()
            
    def check_balance(self):
        accout_number = str(input("Enter your Account Number: "))
        account_password = str(input("Enter your Account Password: "))
        
        with open("./Python/Project/Our Banking App/bank_data.json", "r") as f:
            data = json.load(f)
        
            found = False
            
            for acc in data["accounts"]:
                if acc["Account Number"] == accout_number and acc["Password"] == account_password:
                    print(f"Your Balance is: {acc['Balance']}")
                    found = True
                    break
            
            if not found:                   
                print("Account not found")
                return
        f.close()

    def update_details(self):
        accout_number = str(input("Enter your Account Number: "))
        account_password = str(input("Enter your Account Password: "))
        
        with open("./Python/Project/Our Banking App/bank_data.json", "r") as f:
            data = json.load(f)
        
            found = False
            
            for acc in data["accounts"]:
                if acc["Account Number"] == accout_number and acc["Password"] == account_password:
                    
                    name = str(input("Enter your Name: "))
                    contact = int(input("Enter your Contact: "))
                    location = str(input("Enter your Location: "))
                    password = str(input("Enter your Password: "))
                    acc["Name"] = name
                    acc["Contact"] = contact
                    acc["Location"] = location
                    acc["Password"] = password
                    
                    found = True
                    break
            
            if not found:                   
                print("Account not found")
                return
        f.close()
        
        with open("./Python/Project/Our Banking App/bank_data.json", "w") as f:
            json.dump(data, f, indent=4)
        f.close()
        
        
    def delete_account(self):
        accout_number = str(input("Enter your Account Number: "))
        account_password = str(input("Enter your Account Password: "))
        
        with open("./Python/Project/Our Banking App/bank_data.json", "r") as f:
            data = json.load(f)
        
            found = False
            
            for acc in data["accounts"]:
                if acc["Account Number"] == accout_number and acc["Password"] == account_password:
                    data["accounts"].remove(acc)
                    found = True
                    break
            
            if not found:                   
                print("Account not found")
                return
        f.close()
        
        with open("./Python/Project/Our Banking App/bank_data.json", "w") as f:
            json.dump(data, f, indent=4)
        f.close()
        
        print("Account Deleted Successfully")
            
print("Press 1 for Createing an Account ")
print("Press 2 for Depositing Money ")
print("Press 3 for Withdrawing Money")
print("Press 4 for Checking Balance")
print("Press 5 for Updating Details")
print("Press 6 for Deleting Account " )

choice = int(input("Enter your choice: "))

b1 = Bank()

if choice == 1:
    b1.create_account()
    
if choice == 2:
    b1.deposit()
    
if choice == 3:
    b1.withdraw()

if choice == 4:
    b1.check_balance()

if choice == 5:
    b1.update_details()
    
if choice == 6:
    b1.delete_account()