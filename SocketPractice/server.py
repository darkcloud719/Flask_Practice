from flask import Flask, render_template
import socketio

# Create a Socket.IO server instance
sio = socketio.Server(cors_allowed_origins="*")

# Wrap it with a WSGI-compatible framework (Flask)
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

# Define a route for the root page
@app.route('/')
def index():
    return "Socket.IO server in running"

# Event handler for client connections
@sio.event
def connect(sid, environ):
    print(f"Client {sid} connected")
    sio.emit("message",{"data":"Welcome!"}, to=sid)

# Event handler for client disconnections
@sio.event
def disconnect(sid):
    print(f"Clienet {sid} disconnected")

# Event handler for custom message
@sio.event
def message(sid, data):
    print(f"Message from {sid}: {data}")
    sio.emit("response", {"data","Message received"}, to=sid)

# Run the server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)