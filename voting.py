try: 
    age = int(input("Enter your age: "))
    citizen = input("Are you a Kenyan citizen? (YES/NO): ")

    if age >= 18 and citizen == "YES":
        print("Eligible to vote!!")
    else:
        print("Not eligible to vote!!")
except ValueError:
    print("Enter Numeric for age!")