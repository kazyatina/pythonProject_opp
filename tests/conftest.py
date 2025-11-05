import pytest

from src.category import Category
from src.class_heritage import LawnGrass, Smartphone
from src.iterator import Iterator
from src.product import Product


@pytest.fixture
def object_one():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ],
    )


@pytest.fixture
def object_two():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        products=[
            Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7),
            Product("Samsung Ultra", "Серый цвет, 4K", 180000.0, 5),
        ],
    )


@pytest.fixture
def product():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)


@pytest.fixture
def new_product():
    return Product("Xiaomi Redmi 15", "2024GB, Синий", 61000.0, 10)


@pytest.fixture
def total_price_1():
    return Product("Xiaomi Redmi 15", "2024GB, Синий", 61000.0, 10)


@pytest.fixture
def total_price_2():
    return Product("Xiaomi Mi 5", "1024GB, Синий", 9000.0, 10)


@pytest.fixture
def iter_product(object_one):
    return Iterator(object_one)


@pytest.fixture
def wrong_product():
    return "Banana"


@pytest.fixture
def smartphone_1():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")


@pytest.fixture
def smartphone_2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def lawn_grass_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawn_grass_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def fix_category() -> Category:
    """
    Фикстура для Category
    :return: Category
    """
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Apple iPhone 14 Pro", "128GB, Золотой цвет, 48MP камера", 120000.0, 10)
    product3 = Product("Google Pixel 7 Pro", "128GB, Белый цвет, 50MP камера", 90000.0, 7)
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    return category1


@pytest.fixture
def no_quantity():
    return Category("Электроника", "Гаджеты", [])
