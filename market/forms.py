#works similarly to models with classses and fields
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField#for diff kinds of field import rest

class RegisterForm(FlaskForm):
    username=StringField(label='Username: ')#convetion to take label
    email_address=StringField(label="Email Address: ")
    password1=PasswordField(label="Password: ")
    password2=PasswordField(label="Confirm Password: ")
    submit=SubmitField(label="submit")