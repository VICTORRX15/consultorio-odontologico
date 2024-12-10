from database import db

class Especialidad(db.Model):
    __tablename__ = "especialidades"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)

    medicos = db.relationship('Medico', back_populates='especialidad')

    def __init__(self, nombre):
        self.nombre = nombre

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Especialidad.query.all()


class Medico(db.Model):
    __tablename__ = "medicos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido = db.Column(db.String(80), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    correo_electronico = db.Column(db.String(100), nullable=False)
    especialidad_id = db.Column(db.Integer, db.ForeignKey('especialidades.id'), nullable=False)

    especialidad = db.relationship('Especialidad', back_populates='medicos')
    citas = db.relationship('Cita', back_populates='medico')

    def __init__(self, nombre, apellido, telefono, correo_electronico, especialidad_id):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo_electronico = correo_electronico
        self.especialidad_id = especialidad_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Medico.query.all()

    @staticmethod
    def get_by_id(id):
        return Medico.query.get(id)

    def update(self, nombre=None, apellido=None, telefono=None, correo_electronico=None, especialidad_id=None):
        if nombre:
            self.nombre = nombre
        if apellido:
            self.apellido = apellido
        if telefono:
            self.telefono = telefono
        if correo_electronico:
            self.correo_electronico = correo_electronico
        if especialidad_id:
            self.especialidad_id = especialidad_id
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
