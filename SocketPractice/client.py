import socketio
import time

# Create a client instance
sio = socketio.Client()

# Event handler for connection
@sio.event
def connect():
    print("Connected to the server")
    sio.emit("message",{"data":"Hello from client"})

# Event handler for receiving messages
@sio.event
def response(data):
    print(f"Message from server: {data}")

# Event handler for disconnection
@sio.event
def disconnect():
    print("Disconnected from server")

# Coonect to the server
sio.connect("http://localhost:5000")

# Wait for 15 seconds before disconnecting
time.sleep(15)
sio.disconnect()

# Wait for events
# sio.wait()