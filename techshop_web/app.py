import json
import os
from functools import wraps
from flask import session
from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)
app.secret_key = "nexabyte_secret_key_##20"

ADMIN_USERNAME = "bothers"
ADMIN_PASSWORD = "nexabyte&22"


@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["logged_in"] = True  # saving to session
            session["username"] = username  # save username
            return redirect(url_for('homepage'))
        else:
            error = "Invalid username and password!"
    return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('homepage'))


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get("logged_in"):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated


def save_products():
    try:
        with open("products.json", "w") as f:
            json.dump(products, f, indent=4)
    except Exception as e:
        print(f"Error saving the product:{e}")


def load_products():
    if os.path.exists("products.json"):
        with open("products.json", "r") as f:
            return json.load(f)
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


products = load_products()


@app.route("/")
def homepage():
    return render_template("home.html", store_name="NEXABYTE")


@app.route("/about")
def description():
    return render_template("about.html")


@app.route("/products")
def all_products():
    return render_template("products.html", products=products)


@app.route("/products/<int:id>")
def detail_search(id):
    product = next((p for p in products if p["id"] == id), None)
    if product:
        return render_template("product_detail.html", product=product)
    return render_template("product_detail.html", product=None, error=f"Product {id} not found"), 404


@app.route("/api/products")
def api_products():
    return jsonify(products)


@app.route("/add-product", methods=["GET", "POST"])
@login_required
def add_product():
    error = None
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        price = request.form.get("price", "").strip()
        category = request.form.get("category", "").strip()
        if not name:
            error = "Product name is needed!"
        elif not price:
            error = "Price is required"
        elif not category:
            error = "Please select a category!"
        else:
            try:
                price = float(price)
                if price <= 0:
                    error = "Price must be positive"
                else:
                    in_stock = "in_stock" in request.form
                    new_id = max([p["id"] for p in products], default=0)+1
                    products.append({
                        "id": new_id,
                        "name": name,
                        "price": price,
                        "category": category,
                        "in_stock": in_stock
                    })
                    save_products()
                    return redirect(url_for("all_products"))
            except ValueError:
                error = "Price must be a number!"
    return render_template("add_product.html", error=error)


@app.route("/search")
def search():
    query = request.args.get("q", "").strip().lower()
    results = [p for p in products if query in p["name"].lower()]
    return render_template("search.html", results=results, query=query)


@app.route("/delete/<int:product_id>", methods=["POST"])
@login_required
def delete_product(product_id):
    result = next((p for p in products if p["id"] == product_id), None)
    if result:
        products.remove(result)

    save_products()
    return redirect(url_for("all_products"))


if __name__ == "__main__":
    app.run(debug=True)
