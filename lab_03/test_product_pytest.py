import pytest
from product import Product


@pytest.fixture
def product():
    return Product("Laptop", 2999.99, 10)


@pytest.mark.parametrize(
    "amount, expected_quantity",
    [
        (1, 11),
        (5, 15),
        (10, 20),
        (0, 10),
    ]
)
def test_add_stock(product, amount, expected_quantity):
    product.add_stock(amount)
    assert product.quantity == expected_quantity


def test_add_stock_negative_raises(product):
    with pytest.raises(ValueError):
        product.add_stock(-1)


def test_remove_stock_positive(product):
    product.remove_stock(3)
    assert product.quantity == 7


@pytest.mark.parametrize("amount", [11, 20, 100])
def test_remove_stock_too_much_raises(product, amount):
    with pytest.raises(ValueError):
        product.remove_stock(amount)


def test_remove_stock_negative_raises(product):
    with pytest.raises(ValueError):
        product.remove_stock(-1)


def test_is_available_when_in_stock(product):
    assert product.is_available() is True


def test_is_not_available_when_empty():
    product = Product("Mysz", 99.99, 0)
    assert product.is_available() is False


def test_total_value(product):
    assert product.total_value() == 2999.99 * 10


def test_negative_price_raises():
    with pytest.raises(ValueError):
        Product("Błędny", -10.0, 5)


def test_negative_quantity_raises():
    with pytest.raises(ValueError):
        Product("Błędny", 10.0, -5)