from flask import request, redirect, url_for, Blueprint
from models.medico_model import Medico, Especialidad
from views import medico_view

medico_bp = Blueprint('medico', __name__, url_prefix="/medicos")

@medico_bp.route("/")
def index():
    medicos = Medico.get_all()
    return medico_view.list(medicos)

@medico_bp.route("/create", methods=['GET', 'POST'])
def create():
    especialidades = Especialidad.get_all()
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        correo_electronico = request.form['correo_electronico']
        especialidad_id = request.form['especialidad_id']

        medico = Medico(nombre, apellido, telefono, correo_electronico, especialidad_id)
        medico.save()
        return redirect(url_for('medico.index'))

    return medico_view.create(especialidades)

@medico_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    medico = Medico.get_by_id(id)
    especialidades = Especialidad.get_all()
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        telefono = request.form['telefono']
        correo_electronico = request.form['correo_electronico']
        especialidad_id = request.form['especialidad_id']
        medico.update(nombre=nombre, apellido=apellido, telefono=telefono, correo_electronico=correo_electronico, especialidad_id=especialidad_id)
        return redirect(url_for('medico.index'))

    return medico_view.edit(medico, especialidades)

@medico_bp.route("/delete/<int:id>")
def delete(id):
    medico = Medico.get_by_id(id)
    medico.delete()
    return redirect(url_for('medico.index'))
