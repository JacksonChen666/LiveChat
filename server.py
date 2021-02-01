from flask import Flask, render_template, send_from_directory
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)


@socketio.on('message')
def handle_message(data):
    socketio.emit('message', data["message"], broadcast=True)


@app.route('/')
def index():
    return render_template("base.html")


@app.route('/js/<path:path>')
def script(path):
    return send_from_directory('js', path)


if __name__ == '__main__':
    socketio.run(app, debug=True)
