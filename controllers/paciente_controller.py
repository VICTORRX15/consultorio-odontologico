from flask import request, redirect, url_for, Blueprint
from models.paciente_model import Paciente
from views import paciente_view

paciente_bp = Blueprint('paciente', __name__, url_prefix="/pacientes")

@paciente_bp.route("/")
def index():
    pacientes = Paciente.get_all()
    return paciente_view.list(pacientes)

@paciente_bp.route("/create", methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        correo_electronico = request.form['correo_electronico']
        
        paciente = Paciente(nombre, apellido, telefono, correo_electronico)
        paciente.save()
        return redirect(url_for('paciente.index'))

    return paciente_view.create()

@paciente_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    paciente = Paciente.get_by_id(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        correo_electronico = request.form['correo_electronico']
        paciente.update(nombre=nombre, apellido=apellido, telefono=telefono, correo_electronico=correo_electronico)
        return redirect(url_for('paciente.index'))

    return paciente_view.edit(paciente)

@paciente_bp.route("/delete/<int:id>")
def delete(id):
    paciente = Paciente.get_by_id(id)
    paciente.delete()
    return redirect(url_for('paciente.index'))
