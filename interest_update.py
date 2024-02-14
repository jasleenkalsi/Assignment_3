"""
Description: Asiignment_3
Author: Jasleen kaur
Date: 06/02/2023
"""
import pprint
 
# Define an empty dictionary to store the contents of the input file
account_balances = {}
 
# Open the given input file named account_balances.txt in read mode using a context manager
with open('account_balances.txt', 'r') as file:
    # Process the data in the file
    for line in file:
        # Split each row based on the pipe delimiter
        account_number, balance = line.strip().split('|')
        # Add the contents of the input file to the dictionary
        account_balances[account_number] = float(balance)
 
# Use the pretty print module to display the contents of the dictionary
pprint.pprint(account_balances)
