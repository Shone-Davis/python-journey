from flask import Flask, render_template, jsonify

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


if __name__ == "__main__":
    app.run(debug=True)
