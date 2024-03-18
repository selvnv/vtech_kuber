from flask import Flask
import socket

app = Flask(__name__)


@app.route('/')
def hello():
    # Возвращаем контент в виде строки
    ip_address = socket.gethostbyname(socket.gethostname())
    return f'Hello World from: {ip_address}\n'


if __name__ == '__main__':
    # Запуск сервера. Порт 8000, перезагрузка и вывод ошибок на странице в режиме отладки
    app.run(host='0.0.0.0', port=8000, debug=True)