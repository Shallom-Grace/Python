#user to enter list of names. The program should ensure names are not duplicated, are sorted in alphabetical order and count the number of names inputted.
#User input name. split function splits string to a list of names

names = input("Enter a list of names: ").split()

#initializing an empty list to store the names
nameList = []

#iterating through the names and adding to the nameList
for name in names:
    nameList.append(name)
    
#converting the nameList to set to remove duplicates
newSet= set(nameList)

#converting the set back to list and sorting the list to alphabetical order
newNameList = list(newSet)
newNameList.sort()

#counting the number of names in the list
total_names = len(newNameList)

#output of the sorted list
print(f"Total names in the list: {newNameList}")


#output of the number of names
print(f"There are {total_names} names in total in the list")