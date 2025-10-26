import pytest


def test_smart_init(smartphone_1):
    """Тест на инициализацию"""
    assert smartphone_1.name == "Xiaomi Redmi Note 11"
    assert smartphone_1.description == "1024GB, Синий"
    assert smartphone_1.price == 31000.0
    assert smartphone_1.quantity == 14
    assert smartphone_1.efficiency == 90.3
    assert smartphone_1.model == "Note 11"
    assert smartphone_1.memory == 1024
    assert smartphone_1.color == "Синий"


def test_grass_init(lawn_grass_1):
    """Тест на инициализацию"""
    assert lawn_grass_1.name == "Газонная трава"
    assert lawn_grass_1.description == "Элитная трава для газона"
    assert lawn_grass_1.price == 500.0
    assert lawn_grass_1.quantity == 20
    assert lawn_grass_1.country == "Россия"
    assert lawn_grass_1.germination_period == "7 дней"
    assert lawn_grass_1.color == "Зеленый"


def test_add_smart(smartphone_1, smartphone_2):
    """Тест на сложение общей цены для продуктов (цена*кол-во)"""
    assert smartphone_1 + smartphone_2 == 2114000


def test_add_grass(lawn_grass_1, lawn_grass_2):
    """Тест на сложение общей цены для продуктов (цена*кол-во)"""
    assert lawn_grass_1 + lawn_grass_2 == 16750


def test_add_wrong_type_smart(smartphone_1, wrong_product):
    """Проверяем, что выбрасывается исключение TypeError при попытке добавить некорректный тип."""
    assert f"Ожидался Product, а получен {type(wrong_product).__name__}"


def test_add_wrong_type_grass(lawn_grass_1, wrong_product):
    """Проверяем, что выбрасывается исключение TypeError при попытке добавить некорректный тип."""
    assert f"Ожидался Product, а получен {type(wrong_product).__name__}"


def test_add_wrong_type_smart2(smartphone_1, smartphone_2):
    """Проверяем, что выбрасывается исключение TypeError при попытке добавить некорректный тип."""
    with pytest.raises(TypeError):
        assert smartphone_1 + 1


def test_add_wrong_type_grass2(lawn_grass_1, lawn_grass_2):
    """Проверяем, что выбрасывается исключение TypeError при попытке добавить некорректный тип."""
    with pytest.raises(TypeError):
        assert lawn_grass_1 + 1
