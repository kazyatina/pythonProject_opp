from abc import ABC, abstractmethod
from typing import Any

from src.product import Product


class BaseCategory(ABC):
    """
    Абстрактный класс с перечислением методов для класса Category и его дочерних классов
    """

    @abstractmethod
    def add_product(self, product: Any) -> Any:
        pass

    def get_total_cost(self) -> Any:
        pass


class Category:
    """Класс для создания категорий"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        """Метод для строкового вывода экземпляра класса."""
        goods_count = 0
        for product in self.__products:
            goods_count += product.quantity
        return f"{self.name}, количество продуктов: {goods_count} шт."

    @property
    def products(self):
        """Getter, который возвращает строку, информацию по продуктам"""
        prod_list = ""
        for pl in self.__products:
            prod_list += f"{str(pl)}\n"
        return prod_list

    @property
    def prod_in_list(self):
        """Getter, который возвращает словарь, информацию по продуктам"""
        return self.__products

    def add_product(self, product: Product):
        """Метод для добавления продукта в категорию."""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError


class Order(BaseCategory):
    """
    Класс "Заказ", который наследуется от абстрактного класса и получает общие абстрактные методы
    """

    def __init__(self, product: Any) -> None:
        self.product = product

    def add_product(self, product: Any) -> None:
        """Абстрактный метод для добавления нового продукта в заказ"""
        if not isinstance(product, Product):
            raise ValueError("Объект не является экземпляром класса Product.")
        self.product = product

    def get_total_cost(self) -> Any:
        """Абстрактный метод для получения общей стоимости заказа"""
        return self.product.price * self.product.quantity

    def __str__(self) -> str:
        product: Product = self.product
        return product.name
