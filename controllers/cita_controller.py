from flask import request, redirect, url_for, Blueprint
from datetime import datetime
from models.cita_model import Cita
from models.medico_model import Medico
from models.paciente_model import Paciente
from views import cita_view

cita_bp = Blueprint('cita', __name__, url_prefix="/citas")

@cita_bp.route("/")
def index():
    citas = Cita.get_all()
    return cita_view.list(citas)

@cita_bp.route("/create", methods=['GET', 'POST'])
def create():
    medicos = Medico.get_all()
    pacientes = Paciente.get_all()
    if request.method == 'POST':
        medico_id = request.form['medico_id']
        paciente_id = request.form['paciente_id']
        fecha_str = request.form['fecha']
        descripcion = request.form['descripcion']

        # fecha = datetime.strptime(fecha_str, '%Y-%m-%d %H:%M')
        fecha = datetime.strptime(fecha_str, '%Y-%m-%dT%H:%M')

        cita = Cita(medico_id, paciente_id, fecha, descripcion)
        cita.save()
        return redirect(url_for('cita.index'))

    return cita_view.create(medicos, pacientes)

@cita_bp.route("/edit/<int:id>", methods=['GET', 'POST'])
def edit(id):
    cita = Cita.get_by_id(id)
    medicos = Medico.get_all()
    pacientes = Paciente.get_all()
    if request.method == 'POST':
        medico_id = request.form['medico_id']
        paciente_id = request.form['paciente_id']
        fecha_str = request.form['fecha']
        descripcion = request.form['descripcion']

        # fecha = datetime.strptime(fecha_str, '%Y-%m-%d %H:%M')
        fecha = datetime.strptime(fecha_str, '%Y-%m-%dT%H:%M')
        cita.update(medico_id=medico_id, paciente_id=paciente_id, fecha=fecha, descripcion=descripcion)
        return redirect(url_for('cita.index'))

    return cita_view.edit(cita, medicos, pacientes)

@cita_bp.route("/delete/<int:id>")
def delete(id):
    cita = Cita.get_by_id(id)
    cita.delete()
    return redirect(url_for('cita.index'))
