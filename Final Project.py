"""
This program will act as an inventory management system with some added features

Key Functions: 
Allows user to add or remove items from the inventory, along with view the inventory
Allows the user to add items to a list that will need to be restocked soon and you will also be able to view this list as well
Allows user to make a list of items that are not selling well and you may view this list as well
Gives user the option of changing the price or putting the order on no-retsock
Allows user to view list of items with a new price and items to not restock on

This program will work best for restaurants, grocery stores, clothing stores, or any business that requires inventory checks
"""

# Function to add an item to the inventory
def add_item():
  # Get inputs
  item = input("\nEnter name of item: ")
  quantity = int(input("Enter quantity of item: "))
  # add item to inventory
  inventory[item] = inventory.get(item, 0) + quantity
  # Print the item added and how many of that item was added
  print(f"\n{quantity} {item} added to inventory.")

# Function to remove an item from the inventory
def remove_item():
  # Get item the user wants to remove
  item = input("\nEnter item name: ")
  # Check if item is in inventory
  if item not in inventory:
    print("Item not found in inventory.")
  else:
    # Get input of how much they want to remove of the item specified
    quantity = int(input("Enter amount to be removed: "))
    # Check to see if the quantity input is valid for what is in the inventory
    if quantity > inventory[item]:
      print(f"\nError: Only {inventory[item]} {item}(s) in inventory.")
    else:
      inventory[item] -= quantity
      print(f"\n{quantity} {item}(s) removed from inventory.")

# Function to view the entire inventory
def view_inventory():
  # Check to see if the inventory is empty
  if not inventory:
    print("\nInventory is empty.")
  else:
    print(f"\nCurrent inventory for {company}:")
    # Loop through each item in the inventory
    # Print each item along with the quantity
    for item, quantity in inventory.items():
      print(f"{item}: {quantity}")

# Function to make a list of items low in inventory
def low_inventory():
  print("\nWhat will need to be restocked soon?\n")
  # Get inputs
  low_item = input("Enter name of item: ")
  quantity_to_order = int(input("Enter quantity of item to be ordered: "))
  # add item to low inventory list
  low_inventory_list[low_item] = low_inventory_list.get(low_item, 0) + quantity_to_order
  # Print the item added and how many of that item is needed to be shipped
  print(f"\n{quantity_to_order} {low_item}(s) should be ordered soon in order to restock.")

# Function to view low inventory list
def view_low_inventory():
  # Check to see if the low inventory list is empty
  if not low_inventory_list:
    print("\nLow inventory list is empty.")
  else:
    print(f"\nCurrent low inventory for {company}:")
    # Loop through each item in the inventory
    # Print each item along with the quantity
    for low_item, quantity_to_order in low_inventory_list.items():
      print(f"{low_item}: Order {quantity_to_order}")

# Function to make a list of items that aren't selling
def not_selling():
  # Get inputs
  item_not_selling = input("\nEnter name of item that isn't selling: ")
  price = float(input("How much do you sell this item for? $"))
  price = round(price, 2)
  # Ask user what they want to do about the item that isn't selling
  print("\nWhat would you like to do with this item?")
  print("1. Drop the price")
  print("2. Get rid of item (don't restock again once all sell)")
  print("3. Keep item the same")
  choice = input("Enter 1, 2, or 3: ")

  if choice == "1":
    # Get item original price
    price_drop = float(input("\nHow much of a price drop would you like on this item? $"))
    price_drop = round(price_drop, 2)
    new_price = price - price_drop
    print(f"The new price of {item_not_selling} is ${new_price}")
    new_price_list[item_not_selling] = new_price_list.get(item_not_selling, 0.00) + new_price
  elif choice == "2":
    dont_restock[item_not_selling] = dont_restock.get(item_not_selling, "DO NOT ORDER AGAIN")
    print(f"\nThe item, {item_not_selling}, has now been added to the no-restock list")
  else:
    not_selling_list[item_not_selling] = not_selling_list.get(item_not_selling, "Advertise item more!")
    
    
  
  


### Main


# Start with empty lists
inventory = {}
low_inventory_list = {}
not_selling_list = {}
new_price_list = {}
dont_restock = {}


# Find out what the user is getting inventory for (company?)
company = input("What company will you be doing inventory for? ")


while True:
  # Prompt user of what they would like to do with their inventory
  print("\nWhat would you like to do?")
  print("1. Add item to inventory")
  print("2. Remove item from inventory")
  print("3. View current inventory")
  print("4. Make a list of items low in inventory")
  print("5. View low inventory list")
  print("6. Make a list of items that are not selling")
  print("7. View list of items that are not selling")
  print("8. View list of items with a new price")
  print("9. View list of items that should not be restocked again")
  
  # Get users input
  choice = input("Enter your choice (1-9): ")
  # Based on users input, assign the corresponding function
  if choice == "1":
    add_item()
  elif choice == "2":
    remove_item()
  elif choice == "3":
    view_inventory()
  elif choice == "4":
    low_inventory()
  elif choice == "5":
    view_low_inventory()
  elif choice == "6":
    not_selling()
  elif choice == "7":
    if not not_selling_list:
      print("\nItems not selling list is empty.")
    else:
      print()
      print(not_selling_list)
  elif choice == "8":
    if not new_price_list:
      print("\nNew Price list is empty.")
    else:
      print()
      print(new_price_list)
  elif choice == "9":
    if not dont_restock:
      print("\nNo-restock list is empty.")
    else:
      print()
      print(dont_restock)
  else:
    quit()


