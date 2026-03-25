from data import DEFAULT_PRODUCTS


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


if __name__ == "__main__":
    price = get_valid_price()
    print(f"Got price: {price}")
