import pytest

from src.commerce import Category, Product
from src.grass import LawnGrass
from src.phone import Smartphone


def test_product_inheritance():
    """Тест наследования классов"""
    assert issubclass(Smartphone, Product)


def test_smartphone_creation():
    """Тест создания смартфона"""
    phone = Smartphone("iPhone", "Смартфон", 100000, 5, "A15", "13 Pro", "128GB", "Graphite")
    assert phone.memory == "128GB"
    assert isinstance(phone, Product)


def test_add_product_restriction():
    """Тест ограничения на добавление продуктов"""
    cat = Category("Тест", "Тест")
    with pytest.raises(TypeError):
        cat.add_product("не продукт")


def test_addition_restriction():
    """Тест ограничения сложения"""
    phone = Smartphone("Phone", "Desc", 1000, 2, "A1", "M1", "64GB", "Black")
    grass = LawnGrass("Grass", "Desc", 500, 3, "RU", "10 дней", "Green")

    with pytest.raises(TypeError):
        phone + grass


def test_valid_addition():
    """Тест корректного сложения"""
    phone1 = Smartphone("Phone1", "Desc", 1000, 2, "A1", "M1", "64GB", "Black")
    phone2 = Smartphone("Phone2", "Desc", 1500, 3, "A2", "M2", "128GB", "White")
    assert phone1 + phone2 == 1000 * 2 + 1500 * 3


def test_category_str_with_inherited():
    """Тест строкового представления с наследниками"""
    products = [
        Smartphone("Phone", "Desc", 1000, 2, "A1", "M1", "64GB", "Black"),
        LawnGrass("Grass", "Desc", 500, 3, "RU", "10 дней", "Green"),
    ]
    cat = Category("Тест", "Тест", products)
    assert str(cat) == "Тест, количество продуктов: 5 шт."
