"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db
from flask import render_template, request, jsonify, send_file, url_for
import os
from app.models import Users, Posts, Follows
from app.forms import RegisterUserForm, NewPostForm
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
import datetime


###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


@app.route('/api/v1/register', methods=['POST'])
def register():
    form = RegisterUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        location = form.location.data
        biography = form.biography.data
        profile_photo = form.profile_photo.data

        filename = secure_filename(profile_photo.filename)
        profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        joined_on = datetime.datetime.now()

        user = Users(username, password, firstname, lastname, email, location, biography,  filename, joined_on)
        db.session.add(user)
        db.session.commit()

        users = db.session.execute(db.select(Users)).scalars()
        users_data = []
        for user in users:
            users_data.append({
                "message": "User successfully registered",
                "firstname": user.firstname,
                "lastname": user.lastname,
                "username": user.username,
                "password": user.password,
                "email": user.email,
                "location":user.location,
                "biography": user.biography,
                "profile_photo": user.profile_photo,
                "joined_on": user.joined_on
            })

        return jsonify(data=users_data)
    else:
        return form_errors(form)


@app.route('/api/v1/users/<int:user_id>/posts', methods=['GET'])
def posts(user_id):
    posts = db.session.execute(db.select(Post).filter_by(user_id=id)).scalar()
    posts_data = []
    for post in posts:
        posts_data.append({
            "id": post.id,
            "user_id": post.user_id,
            "photo": post.photo,
            "description": post.description,
            "created_on": post.created_on
        })

    return jsonify(data=posts_data)


@app.route('/api/v1/csrf-token', methods=['GET'])
def get_csrf():
    return jsonify({'csrf_token': generate_csrf()})

###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use
def form_errors(form):
    errors = []
    for field, error in form.errors.items():
        errors.append({
            "field": field,
            "message": error[0]
        })

    return jsonify(errors=errors)

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404