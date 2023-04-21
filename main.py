from datetime import datetime
from flask import Flask, render_template, request
import socket
app = Flask(__name__)

users = {}

@app.route("/")
def hello_world():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    CONST_MAX_AMO_TRIES = 2
    user = users.get(IPAddr)

    current_minute = datetime.now().minute
    if user is None:
        users[IPAddr] = {'minute': current_minute, 'retries': 0, 'time': datetime.now().strftime("%H:%M:%S")}
    else:
        if current_minute == user['minute']:
            users[IPAddr]['retries'] += 1
            if users[IPAddr]['retries']< CONST_MAX_AMO_TRIES:
                return "<p>Hello, World!</p>"
            else:
                return "<p>Too many retries</p>"
        else:
            users[IPAddr]['minute'] = current_minute
            users[IPAddr]['retries'] = 0

        users[IPAddr]['time'] = datetime.now().strftime("%H:%M:%S")
    print(users)
    # print(users)
    return "<p>Hello, World!</p>"