from flask import Flask

app = Flask(__name__)

@app.route("/")
def default():
    return "<h1>Build Successful</h1>"

# db link: postgres://rubeaiwxtkzapn:c306da7057d574936f76017816e64df6b880a662c8b42b7b94c12b5183227b49@ec2-107-22-224-154.compute-1.amazonaws.com:5432/degjcsteagd0gc
