from app import app
from flask import render_template, url_for, request, flash
from app.models.forms import FormSignUp, FormSignIn


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login")
def login():
    form_signup = FormSignUp()
    form_signin = FormSignIn()

    if form_signup.validate_on_submit() and "submit_sigup" in request.form:
        pass
    return render_template(
        "login.html", form_signup=form_signup, form_signin=form_signin
    )
