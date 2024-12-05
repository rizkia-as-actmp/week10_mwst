from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!, nama saya Rizkia Adhy Syahputra, hello flask</h1>"
