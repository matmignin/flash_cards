#!/usr/bin/env python3
from flask import (
    render_template,
    request,
    url_for,
    flash,
    redirect,
    send_from_directory,
)
import os
from quiz import app, db, bcrypt
from quiz.forms import RegisterForm, LoginForm
from quiz.models import User, FileContents
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy.exc import IntegrityError


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_password)
        db.session.add(user)
        try:
            db.session.commit()
            flash(f"account created for {form.username.data}!", "success")
            return redirect(url_for("login"))
        except IntegrityError:
            db.session.rollback()
            flash("that username is already in use")
            # return redirect(url_for('signup'))
    return render_template("signup.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    # flash('Added user')
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash("You have been loged in!", "success")
            files = os.listdir(app.config["UPLOAD_FOLDER"])
            return render_template("quizes.html", files=files)
            # return render_template('quizes.html')
        else:
            flash("not a user or correct password")
            # , convert.question[int(form.question.data)])
        # return
    return render_template("login.html", form=form)

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/quizes", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        input = request.files['inputFile']
        if input.filename == '':
            flash('no files')
            return redirect(request.url)
        # if input and allowed_file(file.filename): 
        else:    
            for upload in request.files.getlist("inputFile"):
                upload.save(os.path.join(app.config["UPLOAD_FOLDER"], upload.filename))
        files = os.listdir(app.config["UPLOAD_FOLDER"])
        return render_template("quizes.html", files=files)


@app.route("/quizes/<filename>")
def send_image(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)
