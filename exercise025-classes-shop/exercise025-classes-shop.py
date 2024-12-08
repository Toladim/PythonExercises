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
    order_counter = 1

    def __init__(self, store: "Store"):
        self.order_id = Order.order_counter
        Order.order_counter += 1
        self.orderItems: list[OrderItem] = []
        store.add_order(self)
    
    def add_item(self, product, quantity):
        if quantity > product.quantity:
            print(f"Not enought items in store. At this moment we have: {product.quantity} pieces")
        elif quantity <= 0:
            print("Error: Quantity must be greater than zero.")
        else:
            order_item = OrderItem(product, quantity)
            self.orderItems.append(order_item)
            product.quantity -= quantity
            print(f"Added {quantity} {product.name} to the order.")
    
    def calculate_total(self):
        return sum(order.calculate_total() for order in self.orderItems)
    
    def show_order_summary(self):
        if not self.orderItems:
            print("The order is empty.")
            return

        print(f"Order summary for Order {self.order_id}:") 
        for order in self.orderItems:
             print(f"    {order.quantity}x {order.product.name} @ {order.product.price:.2f}$ " +
             f"    each: {order.calculate_total():.2f}$")
             
        print(f"Total order cost for order {self.order_id}: {self.calculate_total():.2f}$")

class Store():
    def __init__(self):
        self.orders = []

    def add_order(self, order: Order):
        self.orders.append(order)

    def find_order(self, search_id):
        for order in self.orders:
            if search_id == order.order_id:
                return order.show_order_summary()
            
        print("Order not found")
        return None
    
    def cancel_order(self, id):
        for orderlist in self.orders:
            if id == orderlist.order_id:
                for item in orderlist.orderItems:
                    item.product.quantity += item.quantity
                self.orders.remove(orderlist)
                return
        else:
            print("Order not found")


apple = Product("Apple", 0.5, 882)
banana = Product("Banana", 0.3, 520)
coconut = Product("Coconut", 1, 1000)

store = Store()
order = Order(store)
order.add_item(apple, 10)
order.add_item(banana, 600)
order.add_item(banana, 20)

order2 = Order(store)
order2.add_item(coconut, 10)
order2.add_item(coconut, 60)
#order2.add_item(banana, 20)

store.find_order(1) 
store.find_order(99)  
store.cancel_order(1)
store.find_order(1)
store.cancel_order(1)
print(apple.quantity, banana.quantity)