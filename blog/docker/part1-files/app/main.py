from flask import Flask
import socket

ip = socket.gethostbyname(socket.gethostname())

app = Flask(__name__)


@app.route('/')
def home():
    """ Function to display something. """

    out = (
        f'Welcome to the Docker Lab.<br>'
        f'The IP address of the server is {ip}.<br>'
    )

    return out


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
