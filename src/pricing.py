def apply_discount(total, discount_percent):
    return total * (1 - discount_percent / 100)


def add_tax(total, tax_rate=0.1):
    return total * (1 + tax_rate)