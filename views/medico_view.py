from flask import render_template

def list(medicos):
    return render_template('medico/index.html', medicos=medicos)

def create(especialidades):
    return render_template('medico/create.html', especialidades=especialidades)

def edit(medico, especialidades):
    return render_template('medico/edit.html', medico=medico, especialidades=especialidades)
