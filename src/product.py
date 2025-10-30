from abc import ABC, abstractmethod
from typing import Any


class BaseProduct(ABC):
    """Абстрактный класс указывает на то, что абстрактные методы должны реализоваться во всех
    наследованных классах."""

    @classmethod
    @abstractmethod
    def new_product(cls, product) -> Any:
        pass

    @abstractmethod
    def __str__(self):
        pass


class MixinPrint:
    """
    Миксин класс который при инициализации показывает в консоль имя класса и его аттрибуты
    """

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}, {self.name}, {self.description}, {self.price}, {self.quantity}"


class Product(BaseProduct, MixinPrint):
    """Класс для создания продуктов в Категориях"""

    name: str
    description: str
    price: float
    quantity: int
    total_price: float

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        self.total_price = self.price * self.quantity
        super().__init__()

    def __str__(self):
        """Метод для строкового вывода экземпляра класса."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод для сложения общей цены для продуктов (цена*кол-во)."""
        if type(other) is Product:
            return self.total_price + other.total_price
        raise TypeError(f"Ожидался Product, а получен {type(other).__name__}")

    @property
    def price(self):
        """Getter, который возвращает информацию по цене"""
        return self.__price

    @price.setter
    def price(self, price):
        """Setter, который проверяет цену на положительность, возвращает вывод с ошибкой"""
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price

    @classmethod
    def new_product(cls, product):
        """Метод для добавления нового продукта в класс Product"""
        name = product["name"]
        description = product["description"]
        price = product["price"]
        quantity = product["quantity"]
        return cls(name, description, price, quantity)
