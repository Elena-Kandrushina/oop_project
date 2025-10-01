from src.models import Category, Product


def test_product_init(product1):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.price == 180000.0
    assert product1.quantity == 5
    assert "256GB" in product1.description
    assert repr(
        product1
    ) == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)" or repr(
        product1
    ).startswith(
        "Product(Samsung Galaxy S23 Ultra"
    )


def test_category_init(category_empty):
    assert category_empty.name == "Смартфоны"
    assert category_empty.products == ""
    assert Category.category_count == 1
    assert Category.product_count == 0


def test_category_init_with_products(category_with_products, product2):
    assert category_with_products.name == "Смартфоны"
    assert len(category_with_products.products) == 95
    assert product2.name in category_with_products.products
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_adding_product_updates_counts(category_empty, product1):
    old_product_count = Category.product_count
    category_empty.add_product(product1)
    assert product1.name in category_empty.products
    assert Category.product_count == old_product_count + 1
    assert len(category_empty.products) == 55


def test_multiple_categories_and_products(product1, product2):
    Category.category_count = 0
    Category.product_count = 0
    cat1 = Category("Смартфоны", "Категория смартфонов", products=[product1])
    cat2 = Category("Планшеты", "Категория планшетов")
    cat2.add_product(product2)
    assert Category.category_count == 2
    assert Category.product_count == 2
    assert len(cat1.products) == 55
    assert len(cat2.products) == 40


def test_product_count_consistency(category_with_products, product1):
    initial_count = Category.product_count
    category_with_products.add_product(product1)
    assert len(category_with_products.products) == 150
    assert Category.product_count == initial_count + 1


def test_category_with_none_products():
    Category.category_count = 0
    Category.product_count = 0
    cat = Category("TestNone", "desc", products=None)
    assert cat.products == ""
    assert Category.product_count == 0
    assert Category.category_count == 1


def test_category_count_increases(category_empty, category_with_products):
    Category.category_count = 0
    Category.product_count = 0
    Category("Категория1", "описание1")
    Category("Категория2", "описание2")
    assert Category.category_count == 2


def test_products_property_and_setter(product1):
    category = Category("Смартфоны", "Раздел смартфонов")
    assert category.products == ""
    category.products = product1
    assert "Samsung Galaxy S23 Ultra" in category.products
    assert "180000.0" in category.products
    assert "5" in category.products


def test_new_product_classmethod():
    product_data = {
        "name": "iPhone 14",
        "description": "Pro",
        "price": 120000,
        "quantity": 5,
    }

    product = Product.new_product(product_data)

    assert product.name == "iPhone 14"
    assert product.description == "Pro"
    assert product.price == 120000
    assert product.quantity == 5


def test_price_setter_positive(product1):
    product1.price = 200
    assert product1.price == 200
    assert product1._Product__price == 200


def test_price_setter_zero_or_negative(capsys, product1):
    product1.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product1.price == 180000.0
    assert product1._Product__price == 180000.0
    product1.price = -50
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product1.price == 180000.0
    assert product1._Product__price == 180000.0
