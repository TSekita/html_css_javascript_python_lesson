from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # 制御用に使用

@app.route('/')
def index():
    return render_template('index.html')  # templates/index.html を返す

if __name__ == '__main__':
    # Flask-SocketIOのサーバ起動
    socketio.run(app, host='127.0.0.1', port=5000, debug=True)
