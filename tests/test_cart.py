from src.cart import Cart

def test_cart_total():
    cart = Cart()
    cart.add("Book", 10, qty=2)
    assert cart.total() == 22.0

def test_cart_total_with_discount():
    cart = Cart()
    cart.add("Book", 10, qty=2)
    assert cart.total(discount=10) == 19.8