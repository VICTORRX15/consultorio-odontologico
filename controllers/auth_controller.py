from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required,current_user
from models.usuario_model import Usuario
from database import db

auth_bp = Blueprint('auth', __name__, template_folder='../templates/usuario')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:  # Si ya está autenticado
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = Usuario.query.filter_by(username=username).first()
        if user and user.verify_password(password):
            login_user(user)
            flash('Inicio de sesión exitoso.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Usuario o contraseña incorrectos.', 'error')

    return render_template('login.html')

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if Usuario.query.filter_by(username=username).first():
            flash('El usuario ya existe.')
        else:
            new_user = Usuario(username=username)
            new_user.set_password(password)
            db.session.add(new_user)
            db.session.commit()
            flash('Usuario registrado exitosamente.')
            return redirect(url_for('auth.login'))
    return render_template('register.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Sesión cerrada.')
    return redirect(url_for('auth.login'))