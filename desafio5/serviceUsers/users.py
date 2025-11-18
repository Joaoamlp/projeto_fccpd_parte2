from flask import Flask, jsonify, Response

app = Flask(__name__)
@app.route("/users")
def users():
    users_data = [
        {
            "user": "Alice",
            "role": "Admin"
        },
        {
            "user": "Bob",
            "role": "User"
        },
        {
            "user": "Charlie",
            "role": "Guest"
        }
    ]
    return jsonify(users_data)

app.run(host="0.0.0.0", port=8000) 