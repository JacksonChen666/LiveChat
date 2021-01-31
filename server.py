from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on('message')
def handle_message(data):
    print(f'received message: {data}')


@app.route('/')
def index():
    return render_template("base.html")


if __name__ == '__main__':
    socketio.run(app, debug=True)
