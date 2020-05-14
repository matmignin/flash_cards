#!/usr/bin/env python3
from quiz_app import db
# from flask_login import UserMixin

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


class fileContents(db.Model):
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(300))
    data = db.column(db.LargeBinar)
