from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def hello_world(username=None):
    return render_template("index.html", name=username)


@app.route("/<username>")
def hello_personal(username=None):
    return render_template("personal.html", name=username)


@app.route("/blog/2024/10")
def blog():
    return "These are my thoughts on blogs!"
