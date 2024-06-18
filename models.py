class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class CustomerOrder:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
        self.date = None
        self.total = 0
        self.discount = 0
        self.final_total = 0

    def add_product(self, product, quantity):
        self.items.append((product, quantity))

    def set_date(self, date):
        self.date = date

    def calculate_total(self):
        self.total = sum(item[0].price * item[1] for item in self.items)


