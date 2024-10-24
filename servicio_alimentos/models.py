from flask_sqlalchemy import SQLAlchemy


# Inicializamos SQLAlchemy
db = SQLAlchemy()

# Definimos el modelo de la tabla alimentacion
class Alimentacion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    mascota_id = db.Column(db.Integer, nullable = False)
    hora_alimentacion = db.Column(db.String(128), nullable = False)
