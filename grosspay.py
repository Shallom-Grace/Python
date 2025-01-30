#get hours and rate from user to calculate the gross pay
rate = float(input("Enter the rate of hours worked: "))
hours = float(input("Enter the number of hours worked: "))
gross = rate * hours

print(f"The gross pay is {gross} for {hours} and {rate}")
