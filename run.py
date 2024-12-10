import os
from flask import Flask, request,render_template,redirect,url_for
from controllers.auth_controller import auth_bp
from flask_login import LoginManager, login_required, current_user
from models.usuario_model import Usuario
from controllers import (
    paciente_controller,
    medico_controller,
    cita_controller,
    usuario_controller
)
from database import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///consultorio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)  
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login' 

@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))

app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('home'))  
    return redirect(url_for('auth.login'))  

# Registro de Blueprints
app.register_blueprint(paciente_controller.paciente_bp)
app.register_blueprint(medico_controller.medico_bp)
app.register_blueprint(cita_controller.cita_bp)
app.register_blueprint(usuario_controller.usuario_bp)

@app.context_processor
def inject_active_path():
    def is_active(path):
        return 'active' if request.path.startswith(path) else ''
    return dict(is_active=is_active)

@app.route("/home")

def home():
    return render_template("base.html")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
