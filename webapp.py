#!/usr/bin/env python
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
import main 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'kilgore'       

class LoginForm(FlaskForm):
    username = StringField('username')
    password = PasswordField('password')
    question = StringField('question')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    form = LoginForm()

    if form.validate_on_submit():
        return 'the username is: {}.<br> the pasword is: {}.'.format(form.username.data, form.password.data)    
    return render_template('patho.html', form=form)



if __name__ == '__main__':
    app.run(host='0.0.0.0')
