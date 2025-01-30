#find divisibility of a number by 11
try:
    #getting input as a string from user for digit to digit processing
    num = input("Enter digits: ")

    #initializing variables to store the sum of even and odd
    even = 0
    odd = 0

    #iterating through each position in the string
    for i in range (len(num)):
        if (i % 2 == 0) :
            #if it is the index position is even and digit to the even then convert to integer
            even +=int(num[i])
        else:
            #if it is the index position is odd and digit to the odd then convert to integer
            odd += int(num[i])

    #checking if the reult is divisble by 11
    if ((odd - even) % 11 == 0):
        print(f"number {num} is divisible by 11")
    else:
        print(f"number {num} not divisible by 11")

#handling non-numeric errors
except ValueError:
    print("INVALID INPUT. Please enter a numeric value.")
