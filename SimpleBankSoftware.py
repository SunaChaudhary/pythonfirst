#Simple Bank Software

class BankAccount:
    def __init__(self,name,phone,balance=0.00):
        self.name = name
        self.phone = phone
        self.balance = balance
    def get_balance(self):
        print(f"{self.name}'s current balance is {self.balance:2f}")
    def deposit_Amount(self,amount):
        if amount>=0:
            self.balance+=amount
            print(f"Successful deposite {amount:2f} to {self.name} account")
        else:
            print("Invalid deposite amount")
    def withdraw(self,amount):
        if amount>=0 and self.balance>=amount:
            self.balance-=amount
            print(f"Successful withdraw {amount:2f} from {self.name} account")
        else:
            print("Invalid amount or insufficient balance")

C1=BankAccount("Ram", 986757)
C1.deposit_Amount(5000)
C1.withdraw(1000)
C1.get_balance()