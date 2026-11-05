inventory = {
    "Laptop": 10,
    "Mouse": 20,
    "Keyboard": 15
}

while True:
    print("\n--- Inventory Manager ---")
    print("1. Add Product")
    print("2. Update Product")
    print("3. Delete Product")
    print("4. Display Inventory")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        product = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        inventory[product] = quantity
        print("Product added successfully!")

    elif choice == "2":
        product = input("Enter product name: ")

        if product in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[product] = quantity
            print("Product updated successfully!")
        else:
            print("Product not found!")

    elif choice == "3":
        product = input("Enter product name: ")

        if product in inventory:
            del inventory[product]
            print("Product deleted successfully!")
        else:
            print("Product not found!")

    elif choice == "4":
        print("\nCurrent Inventory:")
        for product, quantity in inventory.items():
            print(product, ":", quantity)

    elif choice == "5":
        print("Exiting Inventory Manager.")
        break

    else:
        print("Invalid choice!")