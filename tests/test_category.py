def test_category_init(object_one, object_two):
    assert object_one.name == "Смартфоны"
    assert (
        object_one.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert object_two.name == "Телевизоры"
    assert (
        object_two.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )

    assert len(object_one.products) == 3
    assert len(object_two.products) == 2

    assert object_one.category_count == 2
    assert object_two.category_count == 2

    assert object_one.product_count == 5
    assert object_two.product_count == 5
