import json
from data import FILENAME, DEFAULT_PRODUCTS


def save_products(products):
    with open("products.json", "w") as file:
        json.dump(products, file, indent=4)


def load_products():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return DEFAULT_PRODUCTS
    except json.JSONDecodeError:
        print("Warning: products.json is corrupted. Loading defaults..")
    return DEFAULT_PRODUCTS


def show_catalogue(products):
    print("========== PRODUCT CATALOGUE ==========")
    for product in products:
        status = "In Stock" if product["in_stock"] else "Out of Stock"
        print(
            f"ID:{product['id']} | {product['name']:<15} | ${product['price']:<8} | {product['category']:<13} | {status}")
    print("========================================")


def get_in_stock(products):
    return [product["name"]
            for product in products if product["in_stock"] is True]


def find_by_category(products, category):
    return [product["name"] for product in products if product["category"] == category]


def get_stats(products):
    prices = [float(product["price"]) for product in products]
    cheapest, expensive, average = min(prices), max(
        prices), round(sum(prices) / len(prices), 2)
    return cheapest, expensive, average


def add_and_save(products, name, price, category, in_stock):
    products.append({"id": len(products)+1, "name": name, "price": price,
                     "category": category, "in_stock": in_stock})
    save_products(products)
    return len(products)


def find_product_by_id(products, product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    raise ValueError(f"Product with ID {product_id} not found!")


def remove_products(products):
    answer = input("Would you like to change or remove any products(y/n): ")
    if answer != 'y':
        print("Thankyou")
        return
    item = input("Enter product name: ").strip()
    updated_products = [
        product for product in products if product["name"].lower() != item.lower()]
    if len(updated_products) == len(products):
        print(f"No product named {item} were found!")
    else:
        try:

            with open("products.json", "w") as file:
                json.dump(updated_products, file, indent=4)
            print(f"successfully removed {item}")
        except Exception as e:
            print(f"Failed to save file: {e}")


if __name__ == "__main__":
    products = load_products()
    show_catalogue(products)
