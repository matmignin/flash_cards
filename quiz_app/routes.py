#!/usr/bin/env python3
from flask import render_template, request, url_for, flash, redirect
from quiz_app import app, db, bcrypt
from quiz_app.forms import RegisterForm, LoginForm, QuestionForm
from quiz_app.models import User, Quiz
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.utils import secure_filename
import email_validator
# import convert
ALLOWED_EXTENSIONS = {'txt', 'pdf'}

@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files()

    newFile = FileContents(name=file.filename, data=file.read())
    db.session.add(newFile)
    db.session.commit()

    return 'saved ' + file.filename + ' to the database'

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
    form = QuestionForm()


    return render_template('quizes.html', form=form)
