from flask import Flask, request, json, Response, abort

app = Flask(__name__)

items = [
    {"id":1,"name":"Item1","description":"This is item 1"},
    {"id":2,"name":"Item2","description":"This is item 2"}
]

def custom_response(data, status_code):
    return Response(json.dumps(data), status=status_code, mimetype="application/json")

@app.route("/items", methods=["GET"])
def get_items():
    # return custom_response({"items":items}, 200)
    response = Response(json.dumps({"items":items}), status=200, mimetype="application/json")
    return response

@app.route("/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        # return custom_response(item, 200)
        response = Response(json.dumps(item), status=200, mimetype="application/json")
        return response
    # return custom_response({"error":"Item not found"}, 404)
    response = Response(json.dumps({"error":"Item not found"}), status=404, mimetype="application/json")
    return response

@app.route("/items", methods=["POST"])
def create_item():
    #### ***
    new_item = request.get_json()
    if not new_item or "name" not in new_item or "description" not in new_item:
        response = Response(json.dumps({"error":"Invalid item"}), status=400, mimetype="application/json")
        return response
    items.append(new_item)
    response = Response(json.dumps(new_item), status=201, mimetype="application/json")
    return response

@app.route("/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if not item:
        response = Response(json.dumps({"error":"Item not found"}), status=404, mimetype="application/json")
        return response
    updated_data = request.get_json()
    if "name" in updated_data:
        item["name"] = updated_data["name"]
    if "description" in updated_data:
        item["description"] = updated_data["description"]

    response = Response(json.dumps(item), status=200, mimetype="application/json")
    return response

@app.route("/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    global items

    item_to_delete = next((item for item in items if item["id"] == item_id), None)

    if item_to_delete is None:
        response = Response(json.dumps({"error":"Item not found"}), status=404, mimetype="application/json")
        return response

    items = [item for item in items if item["id"] != item_id]
    response = Response(json.dumps({"message":"Item deleted"}), status=200, mimetype="application/json")
    return response


if __name__ == "__main__":
    app.run(debug=True)