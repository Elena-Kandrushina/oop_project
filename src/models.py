class Product:
    """Класс, который хранит информацию о продуктах"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        # для себя запомнить метод, который Герман подсказал

    # чтобы сделать вывод более информативным, можно переопределить
    # метод __str__ или __repr__ в классе Product:
    def __repr__(self):
        """Метод для информативного отображения"""
        return (
            f"Product({self.name}, {self.description}, {self.price}, {self.quantity})"
        )

    @classmethod
    def new_product(cls, product_dict):
        return cls(**product_dict)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price


class Category:
    """Класс, который хранит информацию о категориях продуктов"""

    name: str
    description: str
    products: list
    product_count: int
    category_count: int
    product_count = 0
    category_count = 0

    def __init__(self, name, description, products=None):
        """Метод инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product):
        """Метод для добавления продукта в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return product_str

    @products.setter
    def products(self, product: Product):
        self.__products.append(product)
        Category.product_count += 1


if __name__ == "__main__":     # pragma: no cover
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
