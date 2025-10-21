from src.product import Product


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
        self.__products.append(product)
        Category.product_count += 1
