from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
    return render_template("thankyou.html", name=data["yourname"])
