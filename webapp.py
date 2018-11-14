#!/usr/bin/env python
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
import convert 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'kilgore'       

class QuizForm(FlaskForm):
    username = StringField('name')
    question = StringField('question')
    title = convert.question[0]
    total_questions = convert.number_of_questions


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    form = QuizForm()

    if form.validate_on_submit():

        return 'hi {}.<br><br>Here is question {}'.format(form.username.data, convert.question[int(form.question.data)])    
    return render_template('patho.html', form=form) 



if __name__ == '__main__':
    app.run(host='0.0.0.0')
