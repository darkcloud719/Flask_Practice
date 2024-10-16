from flask import Flask
import eventlet
from eventlet import wsgi

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    # wsgi.server(eventlet.listen(("0.0.0.0", 5000)), app)
    eventlet.wsgi.server(eventlet.listen(("0.0.0.0",5000)), app)

