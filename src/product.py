class Product:
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

    def __str__(self):
        """Метод для строкового вывода экземпляра класса."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Метод для сложения общей цены для продуктов (цена*кол-во)."""
        if not isinstance(other, Product):
            raise TypeError(f"Ожидался Product, а получен {type(other).__name__}")
        return self.total_price + other.total_price

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


# if __name__ == '__main__':
#     prod_obj_1 = Product.new_product('Phone', 'Xiomi', 25000, 10)
#     print(prod_obj_1.name)
#     print(prod_obj_1.description)
#     print(prod_obj_1.price)
#     print(prod_obj_1.quantity)
#
#     prod_obj = Product.new_product('Phone', 'LFKjkjdf', 123454, 4)
#     print(prod_obj.name)
#     print(prod_obj.description)
#     print(prod_obj.price)
#     print(prod_obj.quantity)
