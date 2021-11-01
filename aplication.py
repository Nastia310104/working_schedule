from flask import Flask, request
from flask.templating import render_template
from werkzeug.utils import redirect


app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def home():
    """temporary"""
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = 0;

        return render_template("index.html")
    else:
        return render_template("login.html", link_name="Регистрация", link_route="/register")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        return render_template("login.html")
    else:
        return render_template("register.html", link_name="Войти", link_route="/login")