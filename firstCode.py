try:
    #getting the purchase amount from user to determone discount allowed
    amount = float(input("Enter your amount: "))

   #checking if amount is greater or equal to 5000 for 10% discount
    if amount >= 5000:
        discount = 0.1 * amount
        total_amount = amount - discount
        print(f"Your discount is {discount:.2f}. The amount after discount is {total_amount:.2f}")
    #checking if amount is between 1000 and 4999 for 5% discount
    elif 1000 <= amount <= 4999:
        discount = 0.05 * amount
        total_amount = amount - discount
        print(f"Your discount is {discount:.2f}. The amount after discount is {total_amount:.2f}")
    #checking for negative amount
    elif amount < 0:
        print("Negative amount not allowed")
    else:
    #display the original amount and format to 2dp
        print(f"No discount. Amount is {amount:.2f}")
#handle non-numeric input
except ValueError:
    print("INVALID INPUT. Please enter a numeric value.")
