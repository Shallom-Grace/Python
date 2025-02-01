#program that simulates an inventory system allowing user to add items to the inventory
#specify quantities and update quantities if the items are already present
#they can retrieve information about a specific item by entering its name and calculates and 
#displays the total quantities of all items in the inventory

#initializing inventory dictionary
print('Hello welcome to the ABC inventory system')
inventory = {}

#looping through the inventoryKey input until user types done to break the loop
#get user input for the inventoryKey and inventoryVal to add them to the inventory dictionary
while True:
    inventoryKey = input("Enter item: (Type 'done' to stop)").upper()
    if inventoryKey=="DONE":
        break
    inventoryVal = int(input("Enter value of item: "))
    inventory[inventoryKey] = inventoryVal


#using if condition to update values of the inventoryVal 
#incase of an update, the inventory is updated to the new value
updateVal = input("Do you wish to update quantities of items('YES/NO'): ").upper()
if updateVal == "YES":
    itemUpdate = input("Enter the item that needs a quantity change: ").upper()
    
    #checking if the desired item to be updated is in the existing inventory
    if itemUpdate in inventory:
        newVal = int(input("Enter the new quantity: "))
        inventory[itemUpdate] = newVal
    else:
        print("The item not found in inventory")
        
else:
    print(inventory)

#getting user input from user to retrieve information of an item in the inventory by inputting name of item
retrieve_key= input("Do you wish to retrieve item information?: (yes/no)").upper()
if retrieve_key == "YES":
    getKey = input("Enter name of item to retrieve item information: ").upper()
    retrieve = inventory[getKey]
    print(retrieve)

#initializing total variable to store the sum of the quantity values
total= 0

#using loop to get the values in inventory and sum them to find total
for value in inventory.values():
    total += value
    

#using loop to get the items in the inventory
print("Here is the inventory: ")
for keys, values in inventory.items():
    print(keys, values)

#displaying the total of the values in the inventory    
print(f"Here is the total quantity of all items {total}")

#displaying all items in the inventory
print(inventory)