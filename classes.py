
class Product:
    def __init__(self, id, name, price, category, in_stock=True):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.in_stock = in_stock

    def __str__(self):
        status = "In Stock" if self.in_stock else "Out of Stock"
        return f"[{self.id}] | {self.name:<15} | ${self.price:<8} | {self.category:<13} | {status}"

    def toggle_stock(self):
        self.in_stock = not self.in_stock
        status = "In Stock" if self.in_stock else "Out of Stock"
        print(f"{self.name} is now {status}")

    def apply_discount(self, percent):
        self.price = round(self.price * (1 - percent / 100), 2)
        print(f"{self.name} discounted to ${self.price}")


class Store:
    def __init__(self, name):
        self.name = name
        self.products = []
        self._next_id = 1

    def add_product(self, name, price, category):
        new_product = Product(self._next_id, name, price, category)
        self.products.append(new_product)
        self._next_id += 1

    def show_all(self):
        print(f"__________{self.name} Catelouge__________")
        for product in self.products:
            print(product)
        print("_"*45)

    def find_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        raise ValueError(f"{product_id} not found!")

    def get_in_stock(self):
        return [product for product in self.products if product.in_stock]

    def total_value(self):
        return round(sum(p.price for p in self.products), 2)

    def __str__(self):
        return f"Store : {self.name} | Products : {len(self.products)} | Total Value : {self.total_value()} "


# Create store
shop = Store("TechShop")

# Add products
shop.add_product("Laptop",   899.99, "Electronics")
shop.add_product("Mouse",    19.99,  "Electronics")
shop.add_product("Monitor",  299.99, "Accessories")
shop.add_product("Keyboard", 199.99, "Accessories")

# Show all
shop.show_all()

# Store summary
print(shop)

# Discount laptop
shop.find_by_id(1).apply_discount(15)

# Toggle mouse stock
shop.find_by_id(2).toggle_stock()

# Show in stock only
print("\n--- In Stock ---")
for p in shop.get_in_stock():
    print(p)

# Try finding invalid ID
try:
    shop.find_by_id(99)
except ValueError as e:
    print(f"{e}")
