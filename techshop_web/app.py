import json
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop",   "price": 899.99,
        "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "Mouse",    "price": 19.99,
        "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor",  "price": 299.99,
        "category": "Accessories", "in_stock": False},
    {"id": 4, "name": "Keyboard", "price": 199.99,
        "category": "Accessories", "in_stock": True},
]


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
def delete_product(product_id):
    result = next((p for p in products if p["id"] == product_id), None)
    if result:
        products.remove(result)

    save_products()
    return redirect(url_for("all_products"))


if __name__ == "__main__":
    app.run(debug=True)
