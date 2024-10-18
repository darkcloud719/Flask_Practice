from flask import Flask, jsonify, json, Response

app = Flask(__name__)

@app.route("/data")
def get_data():
    # Data to return, usually fetched from a database
    data = {
        "name":"Alick",
        "age":25,
        "city":"Wonderland"
    }

    # return jsonify(data)
    
    response = Response(json.dumps(data), mimetype="application/json", status=200)
    return response

if __name__ == "__main__":
    app.run(debug=True)