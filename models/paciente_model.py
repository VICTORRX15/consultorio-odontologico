from database import db

class Paciente(db.Model):
    __tablename__ = "pacientes"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo_electronico = db.Column(db.String(100), nullable=False)

    citas = db.relationship('Cita', back_populates='paciente')

    def __init__(self, nombre, apellido, telefono, correo_electronico):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo_electronico = correo_electronico

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Paciente.query.all()

    @staticmethod
    def get_by_id(id):
        return Paciente.query.get(id)

    def update(self, nombre=None, apellido=None, telefono=None, correo_electronico=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if telefono:
            self.telefono = telefono
        if correo_electronico:
            self.correo_electronico = correo_electronico
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
