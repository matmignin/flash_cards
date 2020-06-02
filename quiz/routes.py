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
from quiz.models import User

# from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy.exc import IntegrityError

upload_folder = app.config["UPLOAD_FOLDER"]


@app.route("/")
@app.route("/index")
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
            return redirect(url_for('signup'))
    return render_template("signup.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        hash_check = bcrypt.check_password_hash(user.password, form.password.data) 
        if user and hash_check:
            flash("You have been loged in!", "success")
            files = os.listdir(upload_folder)
            return render_template("quizes.html", files=files)

        else:
            flash("not a user or correct password")
    return render_template("login.html", form=form)


@app.route('/quizes', methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if request.files:
            input = request.files["inputFile"]
            if input.filename == "":
                flash("no file selected")
                return redirect(request.url)
            else:
                for upload in request.files.getlist("inputFile"):
                    upload.save(os.path.join(upload_folder, upload.filename))
    files = os.listdir(upload_folder)
    return render_template("quizes.html", files=files)


@app.route("/quizes/<filename>")
def send_image(filename):
    return send_from_directory(upload_folder, filename)
