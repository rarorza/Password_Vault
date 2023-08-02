from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FormSignUp(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    pwd = PasswordField("Password", validators=[DataRequired(), Length(6, 128)])
    confirm_pwd = PasswordField(
        "Confirm password", validators=[DataRequired(), EqualTo("pwd")]
    )
    submit_signup = SubmitField("SignUp")


class FormSignIn(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    pwd = PasswordField("Password", validators=[DataRequired(), Length(6, 128)])
    remember = BooleanField("Remember data")
    submit_signin = SubmitField("SignIn")


class FormDetailsPassword(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    username = StringField("Username")
    url = StringField("URL")
    category = StringField("Category")
    pwd = StringField("Password")
    len_pwd = IntegerField("Length")
    num_pwd = IntegerField("Numbers")
    spe_pwd = IntegerField("Special")
    submit_save = SubmitField("Save")


class FormCreatePassword(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    create = SubmitField("Create")