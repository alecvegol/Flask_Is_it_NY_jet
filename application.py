from flask import Flask, render_template, request

import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/more")
def more():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("more.html", new_year=new_year)

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)
