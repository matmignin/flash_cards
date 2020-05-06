#!/usr/bin/env python3
from quiz_app import db


class LoginForm(FlaskForm):
    username = StringField('Enter Username', validators=[DataRequired()])
    password = PasswordField('Enter Password', validators=[DataRequired()])
    # remember = BooleanField('remember me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    email = StringField('Enter Email', validators=[DataRequired(), Email(message='invalid email')])
    username = StringField('Enter Username', validators=[DataRequired()])
    password = PasswordField('Enter Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class QuestionForm(FlaskForm):
    question = StringField('question')
    title = convert.question[0]
    total_questions = convert.number_of_questions

