class Product:
    """Класс для создания продуктов в Категориях"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
        """Добавление нового продукта в класс Product"""
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
