from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_required, login_user, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            password = request.form.get('password')
            if check_password_hash(user.password, password):
                flash('Logged in Successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect Password, Try again', category='error')
        else:
            flash('User does not exist', category='error')
    return render_template('login.html', user=current_user)


@auth.route('/sign-up', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        data = request.form
        email = data['email']
        first_name = data['firstName']
        password1 = data['password1']
        password2 = data['password2']
        if User.query.filter_by(email=email).first():
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 6 characters', category='error')
        elif password1 != password2:
            flash('Passwords are not matching', category='error')
        else:
            flash('Account created successfully', category='success')
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            return redirect(url_for('views.home'))
    return render_template('signup.html', user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))