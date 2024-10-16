import socketio
import time

sio = socketio.Client()

@sio.event
def connect():
    print("Connected to the server")
    sio.emit('message', {'data':'Hello from client'})

@sio.event
def response(data):
    print(f"Message from server: {data}")

@sio.event
def disconnect():
    print('Disconnected from server')

sio.connect('http://localhost:5000')

time.sleep(15)
sio.disconnect()

