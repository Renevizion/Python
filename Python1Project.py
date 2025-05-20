'''
Python 1
Project
Jason Milord
'''

# Inventory list to store all items
inventory = []

def add_item():
    name = input("Please enter the item name: ")
    price = input("Please enter the item price: ")
    quantity = input("Please enter the item quantity: ")
    category = input("Please enter the item category: ")

    item = {
        "name": name,
        "price": float(price),
        "quantity": int(quantity),
        "category": category
    }

    inventory.append(item)
    print("Item added successfully.\n")

def update_item():
    name = input("Enter the name of the item you want to update: ")
    for i in inventory:
        if i["name"] == name:
            new_price = input("Enter the new price: ")
            new_quantity = input("Enter the new quantity: ")
            new_category = input("Enter the new category: ")

            i["price"] = float(new_price)
            i["quantity"] = int(new_quantity)
            i["category"] = new_category

            print("Item updated.\n")
            return
    print("Item not found.\n")

def view_inventory():
    if len(inventory) == 0:
        print("The inventory is currently empty.\n")
    else:
        print("Here is the current inventory:")
        for i in inventory:
            print("Name:", i["name"], "Price:", i["price"], "Quantity:", i["quantity"], "Category:", i["category"])
        print()

def remove_item():
    name = input("Enter the name of the item you want to remove: ")
    for i in inventory:
        if i["name"] == name:
            inventory.remove(i)
            print("Item removed from inventory.\n")
            return
    print("Item not found.\n")

def search_by_category():
    cat = input("Enter the category to search: ")
    print("Items in the category:")
    found = False
    for i in inventory:
        if i["category"] == cat:
            print("Name:", i["name"], "Price:", i["price"], "Quantity:", i["quantity"])
            found = True
    if not found:
        print("No items found in this category.\n")
    else:
        print()

def main():
    while True:
        print("----- Inventory Menu -----")
        print("1. Add item")
        print("2. Update item")
        print("3. View inventory")
        print("4. Remove item")
        print("5. Search by category")
        print("6. Exit")

        choice = input("Please enter a number (1-6): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            update_item()
        elif choice == "3":
            view_inventory()
        elif choice == "4":
            remove_item()
        elif choice == "5":
            search_by_category()
        elif choice == "6":
            print("Thank you for using the inventory system.")
            break
        else:
            print("Invalid choice. Please enter a valid number.\n")

main()
