class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity

    def increase_quantity(self, amount):
        if amount > 0:
            self.quantity += amount

    def decrease_quantity(self, amount):
        if amount > 0 and self.quantity >= amount:
            self.quantity -= amount
        else:
            print("Недопустимое количество для уменьшения.")

# Создание экземпляров класса "Product"
product1 = Product("Книга", 20.0, 50)
product2 = Product("Флешка", 10.0, 100)

# Вывод общей стоимости для каждого товара
print("Общая стоимость товара 1:", product1.get_total_price())
print("Общая стоимость товара 2:", product2.get_total_price())

# Увеличение и уменьшение количества товаров
product1.increase_quantity(30)
product2.decrease_quantity(20)

# Вывод обновленного количества
print("Обновленное количество товара 1:", product1.quantity)
print("Обновленное количество товара 2:", product2.quantity)
