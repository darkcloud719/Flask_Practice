from flask import Flask

app = Flask(__name__)

@app.route("/item/<int:item_id>")
def get_item(item_id):
    return f"Item ID: {item_id}"

@app.route("/price/<float:price>")
def get_price(price):
    return f"Price: {price}"

@app.route("/user/<string:username>")
def get_user(username):
    return f"Username: {username}"

@app.route("/files/<path:filepath>")
def get_file(filepath):
    return f"Fielpath: {filepath}"

@app.route("/uuid/<uuid:object_id>")
def get_uuid(object_id):
    return f"Object ID: {object_id}"

if __name__ == "__main__":
    app.run(debug=True)