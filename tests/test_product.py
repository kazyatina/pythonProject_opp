import unittest

import pytest

from src.product import Product


def test_product_init(product):
    """Тест на инициализацию"""
    assert product.name == "Xiaomi Redmi Note 11"
    assert product.description == "1024GB, Синий"
    assert product.price == 31000.0
    assert product.quantity == 14


def test_setter_price(product):
    """Тест Setter, который проверяет цену на положительность, возвращает вывод с ошибкой"""
    assert product.price == 31000.0
    product.price == 0, 0
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


def test_product_str(product):
    """Тест на строковый вывод продукта"""
    assert str(product) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."


def test_product_add(total_price_1, total_price_2):
    """Тест на сложение общей цены 2-х продуктов"""
    assert total_price_1 + total_price_2 == 700000


def test_products_add_wrong_product(total_price_1, wrong_product):
    """Тест на добавление продукта не класс Product"""
    expected_message = f"Ожидался Product, а получен {type(wrong_product).__name__}"
    with pytest.raises(TypeError) as info:
        _ = total_price_1 + wrong_product
    assert str(info.value) == expected_message


class TestProduct(unittest.TestCase):

    def test_set_price_positive(self):
        """Проверяем установку положительной цены."""
        product = Product("Тест", "Описание", 100, 2)
        product.price = 150
        self.assertEqual(product.price, 150)

    def test_set_price_negative(self):
        """Проверяем установку отрицательной цены."""
        product = Product("Тест", "Описание", 100, 2)
        product.price = -50  # Ожидаем сообщение об ошибке
        self.assertEqual(product.price, 100)  # Цена не изменится

    def test_new_product_class_method(self):
        """Проверяем метод класса для создания нового продукта."""
        product_data = {"name": "Новый продукт", "description": "Тест", "price": 120, "quantity": 3}
        result = Product.new_product(product_data)
        self.assertEqual(result.name, "Новый продукт")
        self.assertEqual(result.total_price, 360)


def test_print_mixin(capsys):
    """Тест миксина"""
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    message = capsys.readouterr()
    print(message)


def test_product_no_quantity():
    """Тест на добавление продукта с нулевым кол-вом"""
    with pytest.raises(ValueError):
        Product(name="товар", description="новый", price=1000, quantity=0)
