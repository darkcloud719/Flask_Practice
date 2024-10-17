from flask import Flask, request
import socketio

app = Flask(__name__)
sio = socketio.Server(cors_allowed_origins="*")

app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

@sio.event
def connect(sid, environ):
    print(f"Client connected: {sid}")
    sio.send(sid, "Welcome to the SocketIO Server!")

@sio.event
def message(sid, data):
    print(f"Message from {sid}: {data}")
    sio.send(sid, f"Server received: {data}")

@sio.event
def disconnect(sid):
    print(f"Client disconnected: {sid}")

if __name__ == "__main__":
    app.run(debug=True)
