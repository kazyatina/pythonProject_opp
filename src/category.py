from abc import ABC, abstractmethod
from typing import Any

from src.class_exceptions import Exceptions
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

    @prod_in_list.setter
    def prod_in_list(self, product: Product) -> None:
        """Сеттер для добавления продукта в категорию."""
        if isinstance(product, Product):
            try:
                if product.quantity <= 0:
                    raise Exceptions("Товар с нулевым количеством не может быть добавлен")
            except Exceptions as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар добавлен.")
            finally:
                print("Обработка добавления товара завершена.")

        else:
            raise TypeError("Товар должен быть класс Product")

    def add_product(self, product: Product):
        """Метод для добавления продукта в категорию."""
        if isinstance(product, Product):
            try:
                if product.quantity <= 0:
                    raise Exceptions("Товар с нулевым количеством не может быть добавлен")
            except Exceptions as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар добавлен.")
            finally:
                print("Обработка добавления товара завершена.")

        else:
            raise TypeError("Товар должен быть класс Product")

    def middle_price(self):
        """Среднее значение цены"""
        try:
            result = round(sum([product.price for product in self.__products]) / len(self.__products), 1)
            return result
        except ZeroDivisionError:
            return 0


class Order(BaseCategory):
    """
    Класс "Заказ", который наследуется от абстрактного класса и получает общие абстрактные методы
    """

    def __init__(self, product: Any) -> None:
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.product = product

    def add_product(self, product: Any):
        """Абстрактный метод для добавления нового продукта в заказ"""
        if not isinstance(product, Product):
            raise ValueError("Объект не является экземпляром класса Product.")
        if isinstance(product, Product):
            try:
                if product.quantity <= 0:
                    raise Exceptions("Товар с нулевым количеством не может быть добавлен")
            except Exceptions as e:
                print(str(e))
            else:
                self.product = product
                print("Товар добавлен.")
            finally:
                return "Обработка добавления товара завершена."

    def get_total_cost(self) -> Any:
        """Абстрактный метод для получения общей стоимости заказа"""
        return self.product.price * self.product.quantity

    def __str__(self) -> str:
        """Метод для строкового вывода экземпляра класса."""
        product: Product = self.product
        return product.name
