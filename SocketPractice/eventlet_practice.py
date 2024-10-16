import socketio

# Create a Socket.IO server instance
sio = socketio.Server()

# Event handler for when a client connects
@sio.event
def connect(sid, environ):
    print(f"Client {sid} connected")

# Event handler for when a client disconnects
@sio.event
def disconnect(sid):
    print(f"Client {sid} disconnected")

# Event handler for receiving a message from the client
@sio.event
def message(sid, data):
    print(f"Message from {sid}: {data}")
    sid.send("Message received!")

# Create a WSGI app for serving the Socket.IO application
app = socketio.WSGIApp(sio)

# Runniing the server using a WSGI server (e.g., eventlet)
import eventlet
eventlet.wsgi.server(eventlet.listen(("0.0.0.0",5000)), app)