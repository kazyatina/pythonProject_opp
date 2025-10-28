import unittest

import pytest

from src.category import Category, Order
from src.product import Product


def test_category_init(object_one, object_two):
    """Тест на инициализацию"""
    assert object_one.name == "Смартфоны"
    assert (
        object_one.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert object_two.name == "Телевизоры"
    assert (
        object_two.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )

    assert len(object_one.prod_in_list) == 3
    assert len(object_two.prod_in_list) == 2

    assert object_one.category_count == 2
    assert object_two.category_count == 2

    assert object_one.product_count == 5
    assert object_two.product_count == 5


def test_property_products(object_one):
    """Тест на Getter, который возвращает строку, информацию по продуктам"""
    assert object_one.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_new_product(object_one, new_product) -> None:
    """
    Тестирование создания нового продукта с помощью class метода
    :return: None
    """
    assert Product("Xiaomi Redmi 15", "2024GB, Синий", 61000.0, 10)


def test_category_str(object_one):
    """Тест для строкового вывода экземпляра класса"""
    assert str(object_one) == "Смартфоны, количество продуктов: 27 шт."


def test_iterator(iter_product):
    """Тесты на итерацию объекта"""
    assert iter_product.index == 0
    assert next(iter_product).name == "Samsung Galaxy S23 Ultra"
    assert next(iter_product).name == "Iphone 15"
    assert next(iter_product).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(iter_product)


class TestCategory(unittest.TestCase):
    """Тесты для класса Category."""

    def setUp(self):
        """Создаем новый объект Category перед каждым тестом."""
        self.category = Category("test", "test", ["test", "test", 10, 2])

    def test_add_product_increases_product_count(self):
        """Проверяем, что количество продуктов увеличивается при добавлении."""
        initial_count = Category.product_count
        product = Product("Тестовый продукт", "test", 10.0, 2)

        self.category.add_product(product)

        # Убедимся, что количество продуктов увеличилось на 1
        self.assertEqual(Category.product_count, initial_count + 1)

    def test_add_product_valid_product(self):
        """Проверяем, что продукт корректно добавляется, если передан объект Product."""
        initial_count = Category.product_count
        product = Product("test", "test", 10, 2)
        self.category.add_product(product)
        self.assertEqual(Category.product_count, initial_count + 1)

    def test_add_product_invalid_product(self):
        """Проверяем, что выбрасывается исключение TypeError при попытке добавить некорректный тип."""
        with self.assertRaises(TypeError):
            self.category.add_product("Не продукт")

def test_order_abs_category(fix_category: Category) -> None:
    """
    Тестирование переопределения метода str
    """
    product1 = Product("Продукт1", "Описание продукта", 1200, 10)
    product2 = Product("Продукт2", "Описание продукта", 800, 5)

    # Создание категории и добавление продуктов
    category = Category("Категория1", "Описание категории", [])
    category.add_product(product1)
    category.add_product(product2)
    print(category)

    order = Order(product1)
    assert str(order) == "Продукт1"
    assert order.get_total_cost() == 12000

    order.add_product(product2)

    with pytest.raises(ValueError):
        order.add_product("Не продукт")