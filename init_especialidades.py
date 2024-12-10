# init_especialidades.py

from models.medico_model import Especialidad  # Importamos el modelo de Especialidad
from database import db
from run import app  # Importamos la aplicación Flask desde 'run.py'

# Crear las especialidades
especialidades = ['Ortodoncia', 'Implantes', 'Periodoncia']

# Iniciar el contexto de la aplicación Flask
with app.app_context():  # Inicia el contexto de la aplicación
    # Iniciar una sesión en la base de datos y agregar las especialidades
    for especialidad in especialidades:
        nueva_especialidad = Especialidad(nombre=especialidad)  # Creamos una nueva especialidad
        db.session.add(nueva_especialidad)  # Añadimos la especialidad a la sesión

    # Hacemos commit para guardar en la base de datos
    db.session.commit()

    print("Especialidades insertadas correctamente.")
