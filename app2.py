from flask import Flask, render_template
import socketio

sio = socketio.Server(cors_allowed_origins="*")

app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)

@app.route('/')
def index():
    return "Socket.IO server is running"

@sio.event
def connect(sid, environ):
    print(f"Clinet {sid} connected")
    sio.emit('messgae', {'data':'Welcome!'}, to=sid)

@sio.event
def disconnect(sid):
    print(f"Client {sid}, disconnected")

@sio.event
def message(sid, data):
    print(f"Message from {sid}:{data}")
    sio.emit('response',{'data':'Message received'}, to=sid)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)