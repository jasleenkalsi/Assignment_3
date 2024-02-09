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


