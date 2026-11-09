from src.pricing import apply_discount, add_tax


class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price, qty=1):
        self.items.append((name, price, qty))

    def total(self, discount=0):
        subtotal = sum(price * qty for _, price, qty in self.items)
        discounted_total = apply_discount(subtotal, discount)
        return add_tax(discounted_total)