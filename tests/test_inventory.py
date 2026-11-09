from src.inventory import in_stock

def test_in_stock():
    assert in_stock(3) is True
    assert in_stock(0) is False