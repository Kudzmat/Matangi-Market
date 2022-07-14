# flask forms & specific fields required on the forms
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.modules import User

# new user registration form
class RegisterForm(FlaskForm):  # will inherit from the FlaskForm class

    # will check if user in reg form already exists or not
    # FlaskForm checks all functions in class with 'validate' & also contain class attribute
    def validate_username(self, username_check):
        user = User.query.filter_by(username=username_check.data).first() # we use .data because we want data not the plain variable
        if user:
            raise ValidationError('Username already exists! Please try a different username.')

    def validate_email_address(self, email_check):
        email = User.query.filter_by(email_address=email_check.data).first()
        if email:
            raise ValidationError('This email is already registered! Please try a different one or login.')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email:', validators=[Email(), DataRequired()])
    # password & password validation
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Passowrd:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


# login form, will inherit attributes from FlaskForm
class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = StringField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign In:')