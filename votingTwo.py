try: 
    #get user's age and citizenship
    age = int(input("Enter your age: "))
    #convert case to lower for case-sensitive comparison
    citizen = input("Choose the country you are a citizen of: (Kenya, Tanzania, Uganda) :").lower()
    #defining the list of valid countries
    valid_countries = ["kenya", "tanzania", "uganda"]

    #checking if the user meets both the age and citizenship requirements
    if (age >= 18 and citizen in valid_countries):
        print(f"Eligible to vote!! country{citizen} and age{age}")
    else:
        print("Not eligible to vote!!")
#handles non-numeric input for age
except ValueError:
    print("Enter Numeric for age!")
