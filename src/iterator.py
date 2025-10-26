class Iterator:
    """Класс для итерации объектов"""

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
