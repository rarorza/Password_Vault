from app import app, db, login_manager
from flask import render_template, url_for, request, flash, redirect
from app.models.forms import FormSignUp, FormSignIn, FormCreatePassword, FormDetailsPassword
from app.models.tables import User, Password
from flask_login import current_user, login_required, login_user, logout_user


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/", methods=["GET", "POST"])
def home():
    form_create = FormCreatePassword()
    if current_user.is_authenticated:
        list_password = Password.query.filter_by(id_owner=current_user.id)
        if form_create.validate_on_submit():
            pwd = Password(name=form_create.name.data, id_owner=current_user.id)
            db.session.add(pwd)
            db.session.commit()
            flash("Password create successfully", "alert-success")
    else:
        list_password = None
    return render_template("home.html", form_create=form_create, list_password=list_password)


@app.route("/<password_id>", methods=["GET", "POST"])
def details_pwd(password_id):
    password = Password.query.get(password_id)
    print("----", password.name, password.url)
    list_password = Password.query.filter_by(id_owner=current_user.id)
    if current_user == password.owner:
        form_create = FormCreatePassword()
        form_details = FormDetailsPassword()
        if request.method == "GET":
            form_details.name.data = password.name
            form_details.username.data = password.username
            form_details.pwd.data = password.pwd
            form_details.url.data = password.url
            form_details.category.data = password.category
        if form_details.validate_on_submit() and "submit_save" in request.form:
            password.name = form_details.name.data
            password.username = form_details.username.data
            password.url = form_details.url.data
            password.category = form_details.category.data
            password.pwd = form_details.pwd.data
            db.session.commit()
            flash("Modificação salva com sucesso", "alert-success")
        if form_create.validate_on_submit() and "create" in request.form:
            pwd = Password(name=form_create.name.data, id_owner=current_user.id)
            db.session.add(pwd)
            db.session.commit()
    return render_template("details_pwd.html", password=password, form_details=form_details, form_create=form_create, list_password=list_password)


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
