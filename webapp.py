#!/usr/bin/env python
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email
from flask_sqlalchemy import SQLAlchemy
import convert 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'kilgore'       
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/MAT/Dropbox/gatks/flash_cards/database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

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
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if user.password == form.password.data:
                return 'hi {}.<br><br>Here is question {}'.format(form.username.data, convert.question[int(form.question.data)])    
        
        return '<h1>thats not a user</h1>'
    return render_template('patho.html', form=form) 

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(new_user)
        db.session.commit()

        return '<h1>New user created</h1>'
    return render_template('signup.html', form=form)





if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')
