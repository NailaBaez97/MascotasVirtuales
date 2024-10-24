from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db
from routes import alimentos_bp

app = Flask(__name__)
app.config.from_object(Config)

# Inicializamos la base de datos
db.init_app(app)

# Registramos el blueprint de las rutas
app.register_blueprint(alimentos_bp)


# Crear las tablas en la base de datos al iniciar la app
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5001)