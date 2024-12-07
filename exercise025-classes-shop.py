class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
class OrderItem:
    def __init__(self, product: Product, quantity):
        if quantity >= product.quantity:
            self.product = product
            self.quantity = quantity
        else:
            print(f"Not enought items in warehouse. At this moment we have: {self.product.quantity} pieces")
            return

    def calculate_total(self):
        return self.product.price * self.quantity

class Order:
    def __init__(self):
        self.orderItems: list[OrderItem] = []
    
    def add_item(self, product, quantity):
        pass

# Tworzenie produktów
apple = Product("Apple", 0.5, 100)
banana = Product("Banana", 0.3, 50)

# Tworzenie zamówienia
order = Order()
"""order.add_item(apple, 10)
order.add_item(banana, 60)  # Błąd, za dużo sztuk
order.add_item(banana, 20)"""