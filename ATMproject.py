# This program simulates a simple ATM where a user can check their balance, deposit money, or withdraw money. The user should be able to:
# - Check their current balance.
# - Deposit money into their account.
# - Withdraw money from their account.

balance = 15000

print("Welcome to Simple Bank ATM")

while True:
    input_text = """
What do you want to do?
1. Check Balance
2. Deposit Amount
3. Withdraw Amount
4. Close Program
:
"""
    user_input = int(input(input_text))
    
    if user_input == 1:
        print(f"Your balance is {balance}")

    elif user_input == 2:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposit success. Your new balance is {balance}")

    elif user_input == 3:
        amount = float(input("Enter amount to withdraw: "))
        if balance >= amount:
            balance -= amount
            print(f"Withdraw success. Your new balance is {balance}")
        else:
            print("Insufficient Balance")
    elif user_input == 4:
        print("Thank you for using Simple Bank ATM. Goodbye!")
        break
    else:
        print("Invlaid Choice! Try Again...")