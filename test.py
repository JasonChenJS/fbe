from flask import Flask

app = Flask(__name__)

@app.route("/")
def index ():
    return "Hello, World!"

if "__main__" == __name__:
    app.run(host="0.0.0.0", debug=True)
