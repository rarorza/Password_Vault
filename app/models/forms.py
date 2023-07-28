from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
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
