# This program takes a list of names from the user, removes duplicates using a set, 
# sorts the names alphabetically, and then displays the final sorted list.
# It also prints the total number of names entered before removing duplicates.

# Getting names from the user
names = input("Enter names separated by commas: ")

# Splitting the input string into a list of names
list_of_names = names.split(",")

# Counting the number of names in the original list
total_names = 0
for name in list_of_names:
    total_names += 1 

# Converting input to a set to remove duplicates, then sorting it

# Creating a set to remove duplicates
duplicate_free = set(list_of_names) 
# Sorting  the set 
sorted_names = sorted(duplicate_free)   

# Display the sorted names using a for loop
print("\nSorted List of Names:")
for name in sorted_names:
    print(name)

# Printing the total number of names entered before removing duplicates
print(f"\nTotal names entered: {total_names}")