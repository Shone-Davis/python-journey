import json
products = [
    {"id": 1, "name": "Laptop", "price": 899.99,
        "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Mouse",  "price": 19.99,
        "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor", "price": 299.99,
        "category": "Accessories", "in_stock": False},
    {"id": 4, "name": "keyboard", "price": 199.99,
        "category": "Accessories", "in_stock": True},
]


def save_products(products):
    with open("products.json", "w") as file:
        json.dump(products, file, indent=4)


def load_products():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [
            {"id": 1, "name": "Laptop",   "price": 899.99,
             "category": "Electronics", "in_stock": True},
            {"id": 2, "name": "Mouse",    "price": 19.99,
             "category": "Electronics", "in_stock": True},
            {"id": 3, "name": "Monitor",  "price": 299.99,
             "category": "Accessories", "in_stock": False},
            {"id": 4, "name": "Keyboard", "price": 199.99,
             "category": "Accessories", "in_stock": True},
        ]


def add_and_save(products, name, price, category, in_stock):
    products.append({"id": len(products)+1, "name": name, "price": price,
                     "category": category, "in_stock": in_stock})
    with open("products.json", "w")as file:
        json.dump(products, file, indent=4)
    return len(products)


def show_catalogue(products):
    print("========== PRODUCT CATALOGUE ==========")
    for product in products:
        status = "In Stock" if product["in_stock"] else "Out of Stock"
        print(
            f"ID:{product['id']} | {product['name']:<15} | ${product['price']:<8} | {product['category']:<13} | {status}")
    print("========================================")


def get_in_stock(products):
    print("\n____In Stock Only____")
    available = [product["name"]
                 for product in products if product["in_stock"] is True]
    return available


def find_by_category(products, category):
    print(f"\n____{category}____")
    return [product["name"] for product in products if product["category"] == category]


def get_stats(products):
    prices = [product["price"] for product in products]
    cheapest, expensive, average = min(prices), max(
        prices), round(sum(prices) / len(prices), 2)
    return cheapest, expensive, average


products = load_products()
show_catalogue(products)
new = add_and_save(products, "Webcam", 40.99, "Accessories", True)
print("Data saved! Products will be remembered next time.")
print(new)
