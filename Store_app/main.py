from product import load_products, show_catalogue, add_and_save, get_stats, find_product_by_id, remove_products
from validation import get_valid_price, get_valid_category


def main():
    products = load_products()
    show_catalogue(products)

    print("\n---Store Stats---")
    cheapest, expensive, average = get_stats(products)
    print(f"Cheapest  : ${cheapest}")
    print(f"Expensive : ${expensive}")
    print(f"Average   : ${average}")

    print("\n---Add New Product---")
    name = input("Product name: ").strip().title()
    price = get_valid_price()
    category = get_valid_category()
    total = add_and_save(products, name, price, category, True)
    print(f"Added! Total products : {total}")

    print("\n---Find Product---")
    try:
        product_id = int(input("Enter product ID to find: "))
        product = find_product_by_id(products, product_id)
        print(f"Found :{product["name"]} - {product["price"]}")
    except ValueError as e:
        print(f"{e}")

    print("\n---remove product---")
    remove_products(products)


if __name__ == "__main__":
    main()
