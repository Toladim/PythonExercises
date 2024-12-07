class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
class OrderItem:
    def __init__(self, product: Product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_total(self):
        return self.product.price * self.quantity

class Order:
    def __init__(self):
        self.orderItems: list[OrderItem] = []
    
    def add_item(self, product, quantity):
        if quantity > product.quantity:
            print(f"Not enought items in warehouse. At this moment we have: {product.quantity} pieces")
        else:
            order_item = OrderItem(product, quantity)
            self.orderItems.append(order_item)
            product.quantity -= quantity
            print(f"Added {quantity} {product.name} to the order.")
    
    def calculate_total(self):
        return sum(order.product.price * order.quantity for order in self.orderItems)
    
    def show_order_summary(self):
        print("Total orders:") 
        for order in self.orderItems:
            print(f"In this order was ordered: {order.quantity} pieces of {order.product.name} in price:" +
                 f" {order.product.price:.2f}$ per piece. Total cost: {order.calculate_total():.2f}$  ")
          
            #wyświetla podsumowanie zamówienia (produkty, ilości, cena za sztukę, całkowity koszt).


# Tworzenie produktów
apple = Product("Apple", 0.5, 100)
banana = Product("Banana", 0.3, 50)

# Tworzenie zamówienia
order = Order()
order.add_item(apple, 10)
order.add_item(banana, 60)  # Błąd, za dużo sztuk
order.add_item(banana, 20)
print(order.calculate_total())
order.show_order_summary()