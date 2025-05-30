inventory = {
    "Mango": 5,
    "Apple": 17,
    "Grapes": 40,
    "Tomato": 10,
    "Pineapple": 34,

}

while True:
    print("\n***** INVENTORY MANAGEMENT SYSTEM *****")
    print("1. Add Item")
    print("2. Update your Item Quantity")
    print("3. Delete your Item")
    print("4. Display your Inventory")
    print("5. Search an Item")
    print("6. Exit")

    option = int(input("Enter your choice (1-6): "))

    if option == 1:
        item = input("Enter item name to insert: ")

        if item in inventory:
            print(f"{item} already exists. Use option 2 to update.")
        else:
            qty = int(input(f"Enter quantity for {item}: "))
            inventory[item] = qty
            print(f"{item} added with quantity {qty}.")

    elif option == 2:
        item = input("Enter item name to update: ")

        if item in inventory:
            qty = int(input(f"Enter new quantity for {item}: "))
            inventory[item] = qty
            print(f"{item} quantity updated to {qty}.")
        else:
            print(f"{item} not found in inventory.")

    elif option == 3:
        item = input("Enter item name to delete: ")

        if item in inventory:
            del inventory[item]
            print(f"{item} deleted from inventory.")
        else:
            print(f"{item} not found in inventory.")

    elif option == 4:
        print("\nCurrent Inventory:")
        for item, qty in inventory.items():
            print(f"{item}: {qty}")

    elif option == 5:
        item = input("Enter item name to search: ")

        if item in inventory:
            print(f"{item} found with quantity: {inventory[item]}")
        else:
            print(f"{item} not found in inventory. If you choose to add it, please choose option 1")

    elif option == 6:
        print("Exiting the Inventory Management System!")
        break

    else:
        print("Invalid choice. Please select between 1 and 6.")