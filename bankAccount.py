# This program defines a simple BankAccount class that allows users to deposit, withdraw, check their balance, and view account details.
class BankAccount:
    #using a constructor to initialize the account details
    def __init__(self, account_number, customer_name, balance, date_of_opening):
        #self is used to store the details of account number, customer name, balance and date of opening
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.date_of_opening = date_of_opening

#method to calculate deposit
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}"

#method to calculate withdraw
    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return f"Withdrawn: {amount}"

#method to calculate check balance
    def check_balance(self):
        print(f"Current Balance: {self.balance}")

#method to show customer details
    def customer_details(self):
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Date of Opening: {self.date_of_opening}")
        print(f"Balance: {self.balance}")

#checking workings of the class
account = BankAccount("1789673", "Grace Omamo", 450000, "2024-02-14")
#deposit money and print result
print(account.deposit(20000))
#withdraw money and print result
print(account.withdraw(6890))
#checking the current balance
account.check_balance()
#printing out customer details
account.customer_details()