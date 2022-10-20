from flask import Flask, jsonify
import socket

app = Flask(__name__)
app_name = "app2"

@app.route('/', methods=['GET'])
def index():
    return jsonify(dict(route="/", app=app_name, hostname=socket.gethostname(), ip=socket.gethostbyname(socket.gethostname())))

@app.route(f"/{app_name}", methods=['GET'])
def app_fn():
    return jsonify(dict(route=f"/{app_name}", app=app_name, hostname=socket.gethostname(), ip=socket.gethostbyname(socket.gethostname())))

if __name__ == "__main__":
    app.run("0.0.0.0", 5000, False)