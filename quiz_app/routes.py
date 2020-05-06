#!/usr/bin/env python3
from flask import Flask, render_template, url_for, flash, redirect
from quiz_app import
from quiz_app.forms import
from quiz_app.models import

from flask_login import login_user, current_user, logout_user, login_required



# from wtforms import StringField, PasswordField, BooleanField, SubmitField
# import email_validator
# from wtforms.validators import DataRequired, Email, EqualTo, Length
# from flask_bcrypt import Bcrypt
# import convert

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
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
        if user:
            if user.password == form.password.data:
                return 'hi {}.<br><br>way to go on loggin in'.format(form.username.data)
            # , convert.question[int(form.question.data)])

        return '<h1>thats not a user</h1>'
    return render_template('login.html', form=form)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')


