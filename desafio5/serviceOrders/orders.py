from flask import Flask, jsonify, Response

app = Flask(__name__)
@app.route("/orders")
def orders():
    orders_data = [
        {
            "order_id": 1,
            "item": "Laptop",
            "quantity": 2
        },
        {
            "order_id": 2,
            "item": "Smartphone",
            "quantity": 5
        },
        {
            "order_id": 3,
            "item": "Headphones",
            "quantity": 10
        }
    ]
    return jsonify(orders_data)
app.run(host="0.0.0.0", port=8000)

