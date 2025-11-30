# Simple Bank ATM

balance = 15000
print("Welcome to Simple Bank ATM!")

while True:
    input_text = """
What do you want to do?
1. Check Balance
2. Deposit Amount
3. Withdraw Amount
4. Close Program
"""
    print(input_text)
    
    user_input = int(input("Enter your choice (1-4): "))

    if user_input == 1:
        print(f"Your balance is: {balance}")

    elif user_input == 2:
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Your new balance is: {balance}")
        else:
            print("Invalid amount!")

    elif user_input == 3:
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print(f"Your new balance is: {balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance!")

    elif user_input == 4:
        print("Thank you for using Simple Bank ATM!")
        break

    else:
        print("Invalid choice, try again!")
