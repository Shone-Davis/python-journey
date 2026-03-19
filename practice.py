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


def add_product(products, name, price, category, in_stock):
    products.append({"id": len(products)+1, "name": name, "price": price,
                     "category": category, "in_stock": in_stock})
    return len(products)


show_catalogue(products)
instock = get_in_stock(products)
print(instock)
section = find_by_category(products, "Electronics")
print(section)
cheapest, expensive, average = get_stats(products)
print("\n--- Store Stats ---")
print(f"Cheapest  : ${cheapest}")
print(f"Expensive : ${expensive}")
print(f"Average   : ${average}")
total = add_product(products, "Headphone", 199.99, "Accessories", True)
print(f"Total prducts : {total}")
