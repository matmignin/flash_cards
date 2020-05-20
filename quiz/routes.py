#!/usr/bin/env python3
from flask import render_template, request, url_for, flash, redirect
from quiz import app, db, bcrypt
from quiz.forms import RegisterForm, LoginForm
from quiz.models import User, FileContents
from flask_login import login_user, current_user, logout_user, login_required
# from Flask.ext.uploads import UploadSet, configure_uploads, IMAGES
# import convert

@app.route('/index')
@app.route('/')
def index():
  return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # flash('Added user')
    if form.valid ate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # if user.password == form.password.data:
            return render_template('quizes.html')
            # return 'hi {}.<br><br>way to go on loggin in'.format(form.username.data)
            # , convert.question[int(form.question.data)])
        flash('not a user')
        return
    return render_template('login.html', form=form)



@app.route('/quizes', methods=['GET', 'POST'])
def quizes():
  if request.method == 'POST' and 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    return filename
  return render_template('quizes.html')
