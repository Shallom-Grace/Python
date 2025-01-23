try:
    amount = float(input("Enter your amount: "))

    if amount >= 5000:
        discount = 0.1 * amount
        total_amount = amount - discount
        print(f"Your discount is {discount:.2f}. The amount after discount is {total_amount:.2f}")
    elif 1000 <= amount <= 4999:
        discount = 0.05 * amount
        total_amount = amount - discount
        print(f"Your discount is {discount:.2f}. The amount after discount is {total_amount:.2f}")
    elif amount < 0:
        print("Negative amount not allowed")
    else:
        print(f"No discount. Amount is {amount:.2f}")
except ValueError:
    print("INVALID INPUT. Please enter a numeric value.")