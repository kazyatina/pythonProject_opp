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
        self.products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product):
        """Метод для добавления продукта в категорию."""
        self.products.append(product)
        Category.product_count += 1
