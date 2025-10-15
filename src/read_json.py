import json
import os
from logging import Logger

from settings_logger import module_logger
from src.category import Category
from src.product import Product

logger: Logger = module_logger(__name__)


def read_json(path: str) -> dict:
    """Функция для чтения файла json с категориями"""
    logger.info("Запуск работы функции")
    try:
        full_path = os.path.abspath(path)
        with open(full_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.info("Чтение файла - успешно")
        return data
    except FileNotFoundError:
        logger.error("Ошибка в чтении, файл не найден или пустой")
        return {}
    except Exception as err:
        logger.error("Ошибка")
        logger.error(err)
        return {}


def created_objects(data: dict) -> list:
    """Функция для чтения файла json с категориями"""
    if data:
        logger.info("Запуск работы функции")
        category_obj = []
        for category in data:
            product_obj = []
            for product in category["products"]:
                product_obj.append(Product(**product))
            category["products"] = product_obj
            category_obj.append(Category(**category))
            logger.info("json успешно преобразован в объекты классов")
        return category_obj
    else:
        logger.error("Ошибка, невозможно преобразовать пустой json-файл")
        return []


# if __name__ == '__main__':
#     data_list = read_json(FILE_JSON)
#     category_list = created_objects(data_list)
#     print(category_list)
#     print(category_list[0].name)
#     print(category_list[1].name)
