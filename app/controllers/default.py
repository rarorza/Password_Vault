from app import app, db, login_manager
from flask import render_template, url_for, request, flash, redirect
from app.models.forms import FormSignUp, FormSignIn
from app.models.tables import User
from flask_login import current_user, login_required, login_user, logout_user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form_signup = FormSignUp()
    form_signin = FormSignIn()

    if form_signup.validate_on_submit() and "submit_signup" in request.form:
        email_db = User.query.filter_by(email=form_signup.email.data).first()
        if email_db is not None and email_db.email == form_signup.email.data:
            flash("Email already exists", "alert-danger")
        else:
            user = User(
                email=form_signup.email.data, password=form_signup.pwd.data
            )
            db.session.add(user)
            db.session.commit()
            flash(
                f"Account created successfully, email: {form_signup.email.data}",
                "alert-success",
            )

    if form_signin.validate_on_submit() and "submit_signin" in request.form:
        user_db = User.query.filter_by(email=form_signin.email.data).first()
        if user_db and user_db.verify_password(form_signin.pwd.data):
            login_user(user_db, remember=form_signin.remember.data)
            flash(
                f"Login successful, email: {form_signin.email.data}",
                "alert-success",
            )
            param_next = request.args.get("next")
            if param_next:
                return redirect(param_next)
            else:
                return redirect(url_for("home"))
        else:
            flash("Login failed, incorrect email or password", "alert-danger")

    return render_template(
        "login.html", form_signup=form_signup, form_signin=form_signin
    )


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))
