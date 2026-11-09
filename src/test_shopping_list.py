# test_shopping_list.py

from shopping_list import cart, add_item, remove_item, get_list_summary


def setup_function():
    """Clears cart before each test run."""
    cart.clear()


def test_add_item():
    result = add_item("apples", 5, 0.50)
    assert len(cart) == 1
    assert cart[0]["name"] == "apples"
    assert cart[0]["quantity"] == 5
    assert "Added 5 apples" in result


def test_add_existing_item_updates_quantity():
    add_item("apples", 2, 0.50)
    add_item("apples", 3, 0.50)
    assert len(cart) == 1
    assert cart[0]["quantity"] == 5


def test_remove_item_partial():
    add_item("apples", 5, 0.50)
    remove_item("apples", 2)
    assert cart[0]["quantity"] == 3


def test_get_list_summary():
    add_item("apples", 2, 0.50)
    add_item("milk", 1, 3.50)
    total_items, total_price = get_list_summary()
    assert total_items == 3
    assert total_price == 4.50
