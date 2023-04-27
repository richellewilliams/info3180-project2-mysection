from . import db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import InputRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed

class RegisterUserForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    firstname = StringField('Firstname', validators=[InputRequired()])
    lastname = StringField('Lastname', validators=[InputRequired()])
    firstname = StringField('Firstname', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Email()])
    location = StringField('Location', validators=[InputRequired()])
    biography = TextAreaField('Biography', validators=[InputRequired()])
    profile_photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Only Images Allowed!')])