# This program calculates and displays the electricity bill based on units consumed.

# Prompting the user to enter customer details
customer_id = input("Enter Customer ID: ")
customer_name = input("Enter Customer Name: ")
units_consumed = int(input("Enter Units Consumed: "))

# Determining the charges per unit based on the units consumed using if statement
if units_consumed <= 199:
    charge_per_unit = 1.20
elif 200 <= units_consumed < 400:
    charge_per_unit = 1.50
elif 400 <= units_consumed < 600:
    charge_per_unit = 1.80
else:
    charge_per_unit = 2.00

# Calculating the total bill
total_bill = units_consumed * charge_per_unit

# Apply surcharge if the bill exceeds Kshs. 400
if total_bill > 400:
    surcharge = total_bill * 0.15 
    total_bill += surcharge

# Ensure the minimum bill is Kshs. 100
if total_bill < 100:
    total_bill = 100

# Display the final bill
print("Here is an invoice for your current electricity bill: ")
print(f"Customer ID      : {customer_id}")
print(f"Customer Name    : {customer_name}")
print(f"Units Consumed   : {units_consumed}")
print(f"Charge per Unit  : Kshs. {charge_per_unit:.2f}")
print(f"Total Amount to Pay : Kshs. {total_bill:.2f}")