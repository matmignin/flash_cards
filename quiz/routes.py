#!/usr/bin/env python3
from flask import render_template, request, url_for, flash, redirect
from quiz_app import app, db, bcrypt
from quiz_app.forms import RegisterForm, LoginForm
from quiz_app.models import User, FileContents
from flask_login import login_user, current_user, logout_user, login_required
import email_validator
# from Flask.ext.uploads import UploadSet, configure_uploads, IMAGES
# import convert

@app.route('/index')
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
  if request.method == 'POST' and 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    return filename
  return render_template('upload.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        # flash(f'account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
        return '<h1>New user created</h1>'
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # if user.password == form.password.data:
            return 'hi {}.<br><br>way to go on loggin in'.format(form.username.data)
            # , convert.question[int(form.question.data)])

        return '<h1>thats not a user</h1>'
    return render_template('login.html', form=form)



@app.route('/quizes', methods=['GET', 'POST'])
def quizes():
  return render_template('quizes.html')
