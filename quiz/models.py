#!/usr/bin/env python3
from quiz import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    # quizes = db.relationship('Quiz', backref='author', lazy=True)

    def __repr__(self):
        return "User('(self.username)')"


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_name = db.Column(db.String(150), unique=False)
    subject = db.Column(db.String(100), unique=False)

    # user_id = db.Column(db.Integer, db.ForeignKey('FileContents.id'), nullable=False)
    #
    def __repr__(self):
        return "Quiz('(self.quiz_name)', '(self.subject)')"


class FileContents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300))
    question = db.Column(db.Text)
    answer = db.Column(db.Text)
