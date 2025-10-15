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
        self.price = price
        self.quantity = quantity


# if __name__ == '__main__':
#     test = Product('Phone', 'Xiomi', 25000, 10)
#     print(test.name)
#     print(test.description)
#     print(test.price)
#     print(test.quantity)
