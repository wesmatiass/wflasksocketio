#gunicorn -b 127.0.0.1:5000 -w 3 sock:app
#gunicorn --worker-class eventlet -w 1 sock:app

from flask import Flask, render_template, send_file
from flask_socketio import SocketIO, send

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/google745ad2d45cec360c.html')
def index():
    return send_file('google745ad2d45cec360c.html')

@app.route('/favicon.ico')
def favicon():
    return send_file('w.png')

app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins="*")


@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


@socketio.on('evento')
def handle_my_custom_event(data):
    print('received json: ' + str(data))
    send(str(data), broadcast=True)

if __name__ == "__main__":
   socketio.run(app, debug=True)
