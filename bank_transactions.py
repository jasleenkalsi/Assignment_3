"""
Description: Assignment_3
Author: Jasleen kaur
Date: 06/02/2024

"""


#for currency formatting
import random
import locale

# Set the locale for currency formatting
locale.setlocale(locale.LC_ALL, '')

# Define the transaction options set
transaction_options = {"D", "W", "Q"}

# Declare a variable to store the current user's bank balance
user_balance = float(random.randint(-1000, 10000))

# Format the balance using currency formatting
formatted_balance = locale.currency(user_balance, grouping=True)

# Display the interface
print("*" * 39)
print(f"{'PIXELL RIVER FINANCIAL':^39}")
print(f"{'ATM Simulator':^39}")
print(f"{'Your current balance is:':^39} {formatted_balance}")
print("\n" + "*" * 39)
print(f"{'Deposit: D':<20}{'Withdraw: W':<19}{'Quit: Q':<19}")
print("*" * 39)


import random
import locale

# Define transaction options set
transaction_options = {"D", "W", "Q"}

# Generate random bank balance
bank_balance = float(random.randint(-1000, 10000))

# Format the interface display
interface = """
***************************************         
         PIXELL RIVER FINANCIAL
             ATM Simulator
  Your current balance is: {}

               Deposit: D
              Withdraw: W
              Quit: Q              
***************************************
"""

# Format balance with currency formatting
formatted_balance = locale.currency(bank_balance, grouping=True)

# Display the interface
print(interface.format(formatted_balance))

# Prompt the user for a selection and ensure it's valid
while True:
    user_selection = input("Enter your selection: ").upper()
    if user_selection in transaction_options:
        break
    else:
        print("""
***************************************
            INVALID SELECTION
***************************************
           """)

# Process user's selection
if user_selection == "D":
    # For Deposit, prompt the user for the transaction amount
    deposit_amount = float(input("Enter amount of transaction: "))
    # Add the deposit amount to the current balance
elif user_selection == "W":
    # For Withdrawal, prompt the user for the transaction amount
    withdraw_amount = float(input("Enter amount of transaction: "))
    if withdraw_amount > bank_balance:
        # Display insufficient funds message
        print("""
***************************************
            INSUFFICIENT FUNDS
***************************************
""")
    else:
        # Subtract the withdrawal amount from the current balances
        bank_balance -=  withdraw_amount

# Display the updated balance
print("""
***************************************
  Your current balance is: {} 
***************************************
""".format(locale.currency(bank_balance, grouping=True)))
