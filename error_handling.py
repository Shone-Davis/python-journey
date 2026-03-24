import json
products = [
    {"id": 1, "name": "Laptop",   "price": 899.99,
        "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Mouse",    "price": 19.99,
        "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor",  "price": 299.99,
        "category": "Accessories", "in_stock": False},
    {"id": 4, "name": "Keyboard", "price": 199.99,
        "category": "Accessories", "in_stock": True}
]

DEFAULT_PRODUCTS = [
    {"id": 1, "name": "Laptop",   "price": 899.99,
        "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Mouse",    "price": 19.99,
        "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor",  "price": 299.99,
        "category": "Accessories", "in_stock": False},
    {"id": 4, "name": "Keyboard", "price": 199.99,
        "category": "Accessories", "in_stock": True},
]


def get_valid_price():
    while True:
        try:
            price = float(input("Enter price: "))
            if price < 0:
                print("Price must be positive!")
            else:
                print(f"Price set: ${price}")
                return price
        except ValueError:
            print("Invalid! Please enter a number.")


def get_valid_category():
    choice = ["Electronics", "Accessories", "Audio"]
    while True:
        category = input(
            "Enter category (Electronics, Accessories, Audio): ").strip().title()
        if category in choice:
            print(f"Category set: {category}")
            break
        else:
            print(f"Invalid category! Choose from: {choice}")
    return category


def find_product_by_id(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    raise ValueError(f"Product with ID {product_id} not found!")


def safe_load_products():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return DEFAULT_PRODUCTS
    except json.JSONDecodeError:
        print("Warning: products.json is corrupted. Loading defaults.")
        return DEFAULT_PRODUCTS


# test 1 _ find valid product
try:
    product = find_product_by_id(products, 3)
    print(f"Found: {product['name']}")
except ValueError as e:
    print(f"Error:{e}")

# test 2 - find invalid product
try:
    product = find_product_by_id(products, 99)
    print(f"Found: {product["name"]}")
except ValueError as e:
    print(f"Error : {e}")

# test 3 - get valid price from user
price = get_valid_price()
print(f"Final price : ${price}")

# test 4 - get valid category
category = get_valid_category()
print(f"Final category: {category}")
