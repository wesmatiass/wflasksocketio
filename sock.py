#gunicorn -b 127.0.0.1:5000 -w 3 sock:app
#gunicorn --worker-class eventlet -w 1 module:app

from flask import Flask, render_template
from flask_socketio import SocketIO, send



app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')


app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


@socketio.on('evento')
def handle_my_custom_event(data):
    print('received json: ' + str(data))


if __name__ == "__main__":
   socketio.run(app, debug=True)