from src.product import Product


class Smartphone(Product):
    """Класс-наследник"""

    efficiency: float  # производительность
    model: str
    memory: int
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        """Метод для сложения общей цены для продуктов (цена*кол-во)."""
        if type(other) is Smartphone:
            return self.total_price + other.total_price
        raise TypeError(f"Ожидался Product, а получен {type(other).__name__}")


class LawnGrass(Product):
    """Класс-наследник"""

    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        """Метод для сложения общей цены для продуктов (цена*кол-во)."""
        if type(other) is LawnGrass:
            return self.total_price + other.total_price
        raise TypeError(f"Ожидался Product, а получен {type(other).__name__}")
