from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'   # セッション用の秘密鍵
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')  # templates/index.html を返す

# SocketIOイベントの例
@socketio.on('message')
def handle_message(msg):
    print('受信:', msg)

if __name__ == '__main__':
    # Flask-SocketIOのサーバ起動
    socketio.run(app, host='127.0.0.1', port=5000, debug=True)
