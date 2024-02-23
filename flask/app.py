from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route("/")
def get_index():
    me = "Harshith"
    return f"<p>{me}!</p>"

@app.route("/hello")
def get_hello():
    me = "Harshith"
    return f"<p>Hello, {me} from the World!</p>"

@app.route("/bye")
def get_goodbye():
    me = "Harshith"
    return f"<p>Goodbye, {me} from the World! Come back soon!</p>"

@app.route("/data")
def get_data():
    data = [
        {"name":"suzy","type":"dog"},
        {"name":"sandy","type":"cat"}
    ]
    return jsonify(data)

@app.route("/api/status")
def get_status():
    data = [
        { "name":"suzy", "status":"sleeping"},
        { "name":"dorothy", "status":"hungry"},
    ]
    return jsonify(data)

@app.route("/<path:path>")
def serve_static(path):
    return send_from_directory('.', path)
