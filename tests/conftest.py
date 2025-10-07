import pytest

from src.models import Category, Product, Smartphone, LawnGrass


@pytest.fixture
def product1():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


@pytest.fixture
def product2():
    return Product("iPhone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category_empty():
    Category.category_count = 0
    Category.product_count = 0
    return Category("Смартфоны", "Категория смартфонов")


@pytest.fixture
def category_with_products(product1, product2):
    Category.category_count = 0
    Category.product_count = 0
    return Category("Смартфоны", "Категория смартфонов", products=[product1, product2])


@pytest.fixture
def product3():
    return Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )


@pytest.fixture
def product4():
    return LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
