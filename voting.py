try: 
    #get age and kenyan citizenship from user to determine voting eligibility
    age = int(input("Enter your age: "))
    citizen = input("Are you a Kenyan citizen? (YES/NO): ")

    #checking if the user is 18 or above and if user is a kenyan citizen
    if age >= 18 and citizen == "YES":
        print("Eligible to vote!!")
    else:
        print("Not eligible to vote!!")
    #handle numeric input for age
except ValueError:
    print("Enter Numeric for age!")
