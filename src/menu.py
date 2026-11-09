# menu.py

from shopping_list import cart, add_item, remove_item, get_list_summary


def display_menu():
    print("\n--- Shopping List Menu ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def handle_add():
    name = input("Enter item name: ").strip()
    if not name:
        print("Item name cannot be empty.")
        return

    try:
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: "))
        if quantity <= 0 or price < 0:
            print("Quantity and price must be positive numbers.")
            return
    except ValueError:
        print("Invalid input! Quantity must be an integer and price must be a number.")
        return

    message = add_item(name, quantity, price)
    print(f"\n{message}")


def handle_remove():
    name = input("Enter item name to remove: ").strip()
    try:
        quantity = int(input("Enter quantity to remove: "))
        if quantity <= 0:
            print("Quantity to remove must be greater than 0.")
            return
    except ValueError:
        print("Invalid input! Quantity must be a whole number.")
        return

    message = remove_item(name, quantity)
    print(f"\n{message}")


def handle_view():
    if not cart:
        print("\nYour shopping list is empty.")
        return

    print("\nYour Shopping List:")
    for item in cart:
        item_total = item["quantity"] * item["price"]
        print(f"- {item['quantity']} {item['name']}: ${item_total:.2f}")

    total_items, total_price = get_list_summary()
    print(f"\nTotal Items: {total_items}")
    print(f"Total Price: ${total_price:.2f}")


def run_menu():
    is_running = True
    while is_running:
        display_menu()
        choice = input("Choose an Action (Enter 1-4): ").strip()

        if choice == "1":
            handle_add()
        elif choice == "2":
            handle_remove()
        elif choice == "3":
            handle_view()
        elif choice == "4":
            print("\nThank you for using Shopping List Manager!")
            is_running = False
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")
