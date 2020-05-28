#!/usr/bin/env python3
from flask import render_template, request, url_for, flash, redirect, send_from_directory
# from flask_uploads import UploadSet, configure_uploads, IMAGES
import os
from quiz import app, db, bcrypt
from quiz.forms import RegisterForm, LoginForm
from quiz.models import User, FileContents
from flask_login import login_user, current_user, logout_user, login_required
# from werkzeug import secure_filename


@app.route('/index')
@app.route('/')
def index():
  return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'account created for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()

  # flash('Added user')
  if form.validate_on_submit():
    user = User.query.filter_by(username=form.username.data).first()
    if user and bcrypt.check_password_hash(user.password, form.password.data):
      # if user.password == form.password.data:
      return render_template('quizes.html')
      # return 'hi {}.<br><br>way to go on loggin in'.format(form.username.data)
      # , convert.question[int(form.question.data)])
    flash('not a user')
    return
  return render_template('login.html', form=form)



@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
# file = request.files['inputFile']
		for upload in request.files.getlist("inputFile"):
			# file = upload.filename
			upload.save(os.path.join(app.config['UPLOAD_FOLDER'], upload.filename))
# flash(f'uploaded {file.filename}', 'success')
	return render_template('upload.html')

@app.route('/upload/<filename>')
def send_image(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/quizes')
def gallery():
	files = os.listdir(app.config['UPLOAD_FOLDER'])
	# print(files)
	# for file in request.files.getlist('files'):
		# print(file)
		# destination = "/".join(app.config['UPLOAD_FOLDER', filename])
		# print(destination)
		# file.save(destination)
	# return send_from_directory("images", file.filename)
	return render_template('quizes.html', files=files)
