from database import db
from datetime import datetime

class Cita(db.Model):
    __tablename__ = "citas"

    id = db.Column(db.Integer, primary_key=True)
    medico_id = db.Column(db.Integer, db.ForeignKey('medicos.id'), nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)
    fecha = db.Column(db.DateTime, nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)

    medico = db.relationship('Medico', back_populates='citas')
    paciente = db.relationship('Paciente', back_populates='citas')

    def __init__(self, medico_id, paciente_id, fecha, descripcion):
        self.medico_id = medico_id
        self.paciente_id = paciente_id
        self.fecha = fecha
        self.descripcion = descripcion

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Cita.query.all()

    @staticmethod
    def get_by_id(id):
        return Cita.query.get(id)

    def update(self, medico_id=None, paciente_id=None, fecha=None, descripcion=None):
        if medico_id:
            self.medico_id = medico_id
        if paciente_id:
            self.paciente_id = paciente_id
        if fecha:
            self.fecha = fecha
        if descripcion:
            self.descripcion = descripcion
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
