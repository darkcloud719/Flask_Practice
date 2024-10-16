from flask import Flask 
import time

app = Flask(__name__)

@app.route('/block')
def block():
    time.sleep(15)
    return "This request was blocked for 15 seconds."

@app.route('/quick')
def quick():
    return "This request is quick!"

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(threaded=False)
