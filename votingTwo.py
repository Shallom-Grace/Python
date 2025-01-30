try: 
    age = int(input("Enter your age: "))
    citizen = input("Choose the country you are a citizen of: (Kenya, Tanzania, Uganda) :").lower()
    valid_countries = ["kenya", "tanzania", "uganda"]

    if (age >= 18 and citizen in valid_countries):
        print(f"Eligible to vote!! country{citizen} and age{age}")
    else:
        print("Not eligible to vote!!")
except ValueError:
    print("Enter Numeric for age!")