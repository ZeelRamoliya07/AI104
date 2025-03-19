"""
Write a Python program to create a class representing a bank. Include methods for managing
customer accounts and transactions.
"""

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_no, name, balance=0):
        if acc_no in self.accounts:
            print("Account already exists!")
        else:
            self.accounts[acc_no] = {'name': name, 'balance': balance}
            print("Account created successfully.")

    def deposit(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no]['balance'] += amount
            print(f"Deposited {amount}. New balance: {self.accounts[acc_no]['balance']}")
        else:
            print("Account not found!")

    def withdraw(self, acc_no, amount):
        if acc_no in self.accounts and self.accounts[acc_no]['balance'] >= amount:
            self.accounts[acc_no]['balance'] -= amount
            print(f"Withdrew {amount}. New balance: {self.accounts[acc_no]['balance']}")
        else:
            print("Insufficient funds or account not found!")

    def display_account(self, acc_no):
        if acc_no in self.accounts:
            print(f"Account: {acc_no}, Name: {self.accounts[acc_no]['name']}, Balance: {self.accounts[acc_no]['balance']}")
        else:
            print("Account not found!")

def bank_menu():
    bank = Bank()
    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display Account")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            acc_no = input("Enter Account Number: ")
            name = input("Enter Name: ")
            balance = float(input("Enter Initial Balance: "))
            bank.create_account(acc_no, name, balance)
        elif choice == '2':
            acc_no = input("Enter Account Number: ")
            amount = float(input("Enter Amount to Deposit: "))
            bank.deposit(acc_no, amount)
        elif choice == '3':
            acc_no = input("Enter Account Number: ")
            amount = float(input("Enter Amount to Withdraw: "))
            bank.withdraw(acc_no, amount)
        elif choice == '4':
            acc_no = input("Enter Account Number: ")
            bank.display_account(acc_no)
        elif choice == '5':
            break
        else:
            print("Invalid choice! Try again.")

bank_menu()
