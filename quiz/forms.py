#!/usr/bin/env python3
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length
from quiz.models import User, FileContents
from quiz import db

# import convert


class LoginForm(FlaskForm):
    username = StringField("Enter Username", validators=[DataRequired()])
    quiz_name = db.Column(db.String(150), unique=False)
    password = PasswordField("Enter Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class RegisterForm(FlaskForm):
    username = StringField("Enter Username", validators=[DataRequired()])
    password = PasswordField("Enter Password", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")


# class QuestionForm(FlaskForm):
# question = StringField('question')
# title = convert.question[0]
# total_questions = convert.number_of_questions
