try:
    num = input("Enter digits: ")

    even = 0
    odd = 0

    for i in range (len(num)):
        if (i % 2 == 0) :
            even +=int(num[i])
        else:
            odd += int(num[i])

    if ((odd - even) % 11 == 0):
        print(f"number {num} is divisible by 11")
    else:
        print(f"number {num} not divisible by 11")
except ValueError:
    print("INVALID INPUT. Please enter a numeric value.")
