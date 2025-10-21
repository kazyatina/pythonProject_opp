import pytest

from src.product import Product


def test_product_init(product):
    assert product.name == "Xiaomi Redmi Note 11"
    assert product.description == "1024GB, Синий"
    assert product.price == 31000.0
    assert product.quantity == 14


def test_setter_price(product):
    assert product.price == 31000.0
    product.price == -12333.5
    assert "Цена не должна быть нулевая или отрицательная"


@pytest.mark.parametrize(
    "name, description, price, quantity, result",
    [
        ("Тест 1", "Описание 1", 10, 12, Product),
        ("Тест 2", "Описание 2", 40, 31, Product),
    ],
)
def test_product(name: str, description: str, price: float, quantity: int, result: Product) -> None:
    """
    Тестирование класса Product по заготовленным данным
    :param name: Название
    :param description: Описание
    :param price: Цена
    :param quantity: Остаток
    :param result: Ожидание от теста
    :return: None
    """

    assert type(Product(name, description, price, quantity)) == Product


def test_new_product(new_product) -> None:
    """
    Тестирование создания нового продукта с помощью class метода
    :return: None
    """
    assert Product("Xiaomi Redmi 15", "2024GB, Синий", 61000.0, 10)
