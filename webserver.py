import flask
from flask import Flask
from threading import Thread

app = Flask(__name__, template_folder='dashboard')

@app.route('/')
def home():
    return "Bot online" # Put text in the webview tab
def run():
    app.run(host='0.0.0.0', port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()
