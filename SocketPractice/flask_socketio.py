from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Socket.IO server is running"


@socketio.on('connect')
def handle_connect():
    print("Client connected")
    SocketIO.emit('message', "Welcome to the SocketIO server!")

@socketio.on('message')
def handle_message(msg):
    print(f"Message: {msg}")
    SocketIO.send(f"Server received: {msg}", broadcast=True)

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

if __name__ == "__main__":
    socketio.run(app, debug=True)


    