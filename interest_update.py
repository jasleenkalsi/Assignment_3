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
 
# Iterate through the dictionary of bank records and calculate interest for each record
for account_number, balance in account_balances.items():
    # Calculate the interest rate based on the balance
    if balance > 0:
        if balance < 1000:
            interest_rate = 0.01
        elif balance < 5000:
            interest_rate = 0.025
        else:
            interest_rate = 0.05
    else:
        interest_rate = 0.1  # Negative balance, charge interest
 
    # Calculate the monthly interest
    interest = (balance * interest_rate) / 12
    # Update the balance of each record in the dictionary to reflect the interest payment or charge
    account_balances[account_number] += interest
 
# Use the pretty print module to display the contents of the dictionary
pprint.pprint(account_balances)
 
import csv
 
# Define the filename for the CSV file
filename = "updated_balances_JS.csv"  # Change 'JS' to your initials
 
# Open the CSV file in write mode using a context manager
with open(filename, 'w', newline='') as csvfile:
    # Define the headings for the file
    fieldnames = ['Account', 'Balance']
   
    # Create a CSV writer object
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
   
    # Write the headings to the CSV file
    writer.writeheader()
   
    # Iterate through the dictionary of updated account balances and write each record to the CSV file
    for account, balance in account_balances.items():
        writer.writerow({'Account': account, 'Balance': balance})
 
# Verify the data has been successfully written to the file
print(f"Data has been successfully written to {filename}")
 
# Verify that the file does not contain any blank rows
with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
    if len(rows) == 0:
        print("The file is empty.")
    else:
        print(f"The file contains {len(rows) - 1} records (excluding header).")
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
 