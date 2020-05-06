#!/usr/bin/env python3


from flask import Flask, render_template, url_for, flash, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
import email_validator
from wtforms.validators import DataRequired, Email, EqualTo, Length
from flask_sqlalchemy import SQLAlchemy
import convert

app = Flask(__name__)


app.config['SECRET_KEY'] = 'kilgore'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    quizes = db.relationship('Quiz', backref='author', lazy=True)

    def __repr__(self):
        return f"User('(self.username)', '(self.email)')"

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_name= db.Column(db.String(150), unique=False)
    subject = db.Column(db.String(100), unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Quiz('(self.quiz_name)', '(self.subject)')"

class LoginForm(FlaskForm):
    username = StringField('Enter Username', validators=[DataRequired()])
    password = PasswordField('Enter Password', validators=[DataRequired()])
    # remember = BooleanField('remember me')
    submit = SubmitField('Login')


class QuestionForm(FlaskForm):
    question = StringField('question')
    title = convert.question[0]
    total_questions = convert.number_of_questions

class RegisterForm(FlaskForm):
    email = StringField('Enter Email', validators=[DataRequired(), Email(message='invalid email')])
    username = StringField('Enter Username', validators=[DataRequired()])
    password = PasswordField('Enter Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
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
                return 'hi {}.<br><br>Here is question'.format(form.username.data) 
            # , convert.question[int(form.question.data)])

        return '<h1>thats not a user</h1>'
    return render_template('login.html', form=form)


@app.route('/index')
@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0')
