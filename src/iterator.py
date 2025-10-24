class Iterator:
    def __init__(self, category_obj):
        """Метод для инициализации экземпляра класса. Задаем значения атрибутам экземпляра."""
        self.category_object = category_obj
        self.index = 0

    def __iter__(self):
        """Метод для получения итератора для перебора объекта."""
        return self

    def __next__(self):
        """Метод для перехода к следующему значению и его считывание."""
        if self.index < len(self.category_object.prod_in_list):
            prod = self.category_object.prod_in_list[self.index]
            self.index += 1
            return prod
        else:
            raise StopIteration


# if __name__ == '__main__':
#     product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#     product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#     product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#     category1 = Category(
#         "Смартфоны",
#         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
#         [product1, product2, product3]
#     )
#
#     iter_1 = Iterator(category1)
#
#     for x in iter_1:
#         print(x)
