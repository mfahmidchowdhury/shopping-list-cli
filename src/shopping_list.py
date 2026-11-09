# shopping_list.py

# Global data structure: A list of dictionaries
cart = []


def add_item(name, quantity, price):
    """Adds a new item or updates an existing item's quantity in the cart."""
    name_clean = name.strip().lower()
    for item in cart:
        if item["name"] == name_clean:
            item["quantity"] += quantity
            item["price"] = price
            return f"Updated {item['name']} quantity to {item['quantity']}!"

    new_item = {"name": name_clean, "quantity": quantity, "price": price}
    cart.append(new_item)
    return f"Added {quantity} {name_clean} at ${price:.2f} each to your shopping list!"


def remove_item(name, quantity):
    """Removes a specified quantity of an item from the cart."""
    name_clean = name.strip().lower()
    for item in cart:
        if item["name"] == name_clean:
            if quantity >= item["quantity"]:
                cart.remove(item)
                return f"Removed all {name_clean} from your shopping list!"
            else:
                item["quantity"] -= quantity
                return f"Removed {quantity} {name_clean} from your shopping list!"
    return f"Item '{name_clean}' was not found in your shopping list."


def get_list_summary():
    """Calculates total items and overall cart cost."""
    total_items = sum(item["quantity"] for item in cart)  # Built-in iteration
    total_price = sum(item["quantity"] * item["price"] for item in cart)
    return total_items, total_price
