from flask import Flask

app = Flask(__name__)

@app.route("/")
def default():
    return "<h1>Build Successful</h1>"

# db link: postgres://qpyazjzqokyzax:ed7333462683a13b5b70e32f451378d79d95dfe41a18d97c9adf983fd3cab49b@ec2-54-225-106-93.compute-1.amazonaws.com:5432/d658ji5p1npm9e