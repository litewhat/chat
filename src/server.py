import os
from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = os.environ['FLASK_APP_SECRET_KEY']
socketio = SocketIO(app)


@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
