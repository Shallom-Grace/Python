"""
This Python program defines a BankAccount class that allows a user 
to perform basic banking operations such as depositing money, 
withdrawing money, checking the balance, and displaying customer details. 
It demonstrates object-oriented programming by encapsulating 
bank account functionalities in a class.
"""

# Defining the BankAccount class
class BankAccount:
    def __init__(self, customer_name, date_of_opening, balance, account_number):
        """
        Constructor to initialize a bank account with the 
        customer's name, account opening date, balance, and account number.
        """
        self.customer_name = customer_name  # Customer's name
        self.date_of_opening = date_of_opening  # Account opening date
        self.account_number = account_number  # Unique account number
        self.balance = balance  # Initial account balance

    def deposit(self, amount):
        """
        Method to deposit money into the account.
        It ensures the deposit amount is greater than zero.
        """
        if amount > 0:
            self.balance += amount
            return f"Deposited: KES {amount}"
        return "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        """
        Method to withdraw money from the account.
        It checks if the withdrawal amount does not exceed the balance.
        """
        if amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        return f"Withdrawn: KES {amount}"

    def check_balance(self):
        """Method to display the current balance of the account."""
        print(f"Current Balance: KES {self.balance}")

    def customer_details(self):
        """Method to display customer details including name, account number, and balance."""
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: KES {self.balance}")


# Creating a BankAccount object for a customer named Grace
account = BankAccount("Grace", "2025-03-27", 200, "AB300")

# Depositing money into the account
deposit_result = account.deposit(5000)
print(deposit_result)

# Withdrawing money from the account
withdraw_result = account.withdraw(2000)
print(withdraw_result)

# Checking the updated balance
account.check_balance()

# Displaying customer details
account.customer_details()