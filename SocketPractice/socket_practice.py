import flask
import socketio

sio = socketio.Server(cors_allowed_origins="*")

@sio.event
def connect(sid,environ):
    print(f"Client {sid} connected")
    sio.emit("message", {"Welcome to the server!"}, to=sid)

@sio.event
def disconnect(sid):
    print(f"Client {sid} disconnected")

@sio.event
def message(sid, data):
    print(f"Message from {sid}: {data}")
    sio.send("Message received!", to=sid)

@sio.event
def my_custom_event(sid, data):
    print(f"Received custom event from {sid}: {data}")
    sio.emit("custom_response", "Data received!", to=sid)

@sio.event
def join_room(sid, room):
    sio.enter_room(sid, room)
    print(f"Client {sid} joined room {room}")
    sio.emit("message", f"Client {sid} joined room {room}", room=room)


@sio.event
def leave_room(sid, room):
    sio.leave_room(sid, room)
    print(f"Client {sid} left room {room}")
    sio.emit("message", f"Client {sid} left room {room}", room=room)

@sio.emit("announcement",{"message":"This is a broadcast message"}, broadcast=True)

@sio.event
def error(sid, data):
    print(f"Error from client {sid}: {data}")
    sio.emit("error_Response", {"error":"An error occurred"}, to=sid)

@sio.event
def my_event_with_ack(sid,data):
    print(f"Received {data} from {sid}")
    return {"status":"Received"}

# On thie client-side
# socket.emit("my_event_with_ack", {"data":"test"}, (response) => {
#     console.log(response.status)
# })

# @sio.emit("broadcast","Hello, everyone!", broadcast=True)
