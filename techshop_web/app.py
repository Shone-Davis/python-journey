from flask import Flask, jsonify

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
    return """
    <h1>NEXABYTE</h1>
    <p>Hardware for the Next Era</p>
    <a href ="/products">View Products</a> | <a href="/about">About Us</a>
    """


@app.route("/about")
def description():
    return """
    <h1>About Nexabyte</h1>
    <h2>The Future, Built Today</h2>
    <p>Welcome to Nexabyte, your premier destination for the hardware that powers the next generation of innovation. We believe that technology shouldn't just keep up with the world, it should drive it forward.</p>
    <a href="/"> <- Back to Home</a>
    """


@app.route("/products")
def all_products():
    html = "<h1>Nexabyte - All Products</h1><pre>"
    html += f"{'ID':<3} | {'Name':<12} | {'Price':<8} | {'Category':<13} | {'Status'}\n"
    html += "-" * 60 + "\n"

    for product in products:
        status = "In stock" if product['in_stock'] else "Out of stock"
        html += f"<a href='/products/{product['id']}'>{product['id']:<3}</a> | {product['name']:<12} | ${product['price']:<8} | {product['category']:<13} | {status}\n"

    html += "</pre><br><a href='/'> <- Back to Home</a>"
    return html


@app.route("/products/<int:id>")
def detail_search(id):
    for product in products:
        if id == product['id']:
            status_text = "In Stock" if product['in_stock'] else "Out of Stock"
            return f"""
            <h1>Product Details</h1>
            <pre>
        Name     : {product['name']}
        Price    : ${product['price']}
        Category : {product['category']}
        Status   : {status_text}
            </pre> 
            <br>
            <a href="/products"><- Back to products</a>
            """
    # Return 404 if not found
    return f"<h1>Product not found!</h1><p>No product with ID {id} exists.</p><a href='/products'>Back</a>", 404


@app.route("/api/products")
def api_products():
    return jsonify(products)


if __name__ == "__main__":
    app.run(debug=True)
