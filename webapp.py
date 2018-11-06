#!/usr/bin/env python
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
import main 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'kilgore'       

class QuizForm(FlaskForm):
    username = StringField('username')
    question = StringField('question')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    form = QuizForm()

    if form.validate_on_submit():
        return 'hi {}.<br> the Question for{} is.<br><br>{}'.format(form.username.data, form.question.data, main.question[int(form.question.data)])    
    return render_template('patho.html', form=form) 



if __name__ == '__main__':
    app.run(host='0.0.0.0')
