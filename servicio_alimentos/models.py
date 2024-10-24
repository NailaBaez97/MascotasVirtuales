from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Alimentacion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    mascota_id = db.Column(db.Integer, nullable = False)
    hora_alimentacion = db.Column(db.String(128), nullable = False)
