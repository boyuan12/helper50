from flask import Flask

app = Flask(__name__)

@app.route("/")
def default():
    return "<h1>Build Successful</h1>"