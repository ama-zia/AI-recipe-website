from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from bcrypt import hashpw, gensalt, checkpw
from python_backend.models import db, User

auth_bp = Blueprint('auth_bp', __name__, template_folder='../templates')

@auth_bp.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return "A user with this email already exists."

        hashed_password = hashpw(password.encode('utf-8'), gensalt())
        new_user = User(username=name, email=email, password_hash=hashed_password.decode('utf-8'))
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth_bp.login'))
    return render_template('signup.html')

@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and checkpw(password.encode('utf-8'), user.password_hash.encode('utf-8')):
            login_user(user)
            return redirect(url_for('main_bp.recipes_page'))
        else:
            return "Invalid email or password."
    return render_template('login.html')

@auth_bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))