#!/usr/bin/env python
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email
import convert 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'kilgore'       

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    remember = BooleanField('remember me')
    question = StringField('question')
    title = convert.question[0]
    total_questions = convert.number_of_questions

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='invalid email')])
    username = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        return 'hi {}.<br><br>Here is question {}'.format(form.username.data, convert.question[int(form.question.data)])    
    return render_template('patho.html', form=form) 

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    return render_template('signup.html', form=form)





if __name__ == '__main__':
    app.run(host='0.0.0.0')
