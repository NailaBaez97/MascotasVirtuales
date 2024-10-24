from flask import Blueprint, request, jsonify
from models import db, Alimentacion
import datetime


# Creamos el blueprint para las rutas
alimentos_bp = Blueprint('alimentos_bp', __name__)

@alimentos_bp.route('/alimentar', methods=['POST'])
def alimento_mascota():
    data = request.get_json()
    mascotaId = data['mascota_id']
    hora_alimentacion = datetime.datetime.now().isoformat()

    #Crear un nuevo registro de alimentacion
    nueva_alimentacion = Alimentacion(mascota_id = mascotaId, hora_alimentacion = hora_alimentacion)
    db.session.add(nueva_alimentacion)
    db.session.commit()

    return jsonify({"mensje":"Mascota alimentada", "alimentacion":{
        'mascota_id' : mascotaId,
        'hora_alimentacion' : hora_alimentacion
    }}), 201

@alimentos_bp.route('/ultima_alimentacion/<int:mascota_id>', methods = ['GET'])
def obtener_ultima_alimentacion(mascota_id):
    # Obtener la última vez que la mascota fue alimentada
    ultima_alimentacion = Alimentacion.query.filter_by(mascota_id = mascota_id).order_by(Alimentacion.id_alimentacion.desc()).first()
    if ultima_alimentacion:
        return({
            'mascotaId' : ultima_alimentacion.mascota_id,
            'hora_alimentacion' : ultima_alimentacion.hora_alimentacion
        })
    else:
        return jsonify({"mensaje": "Mascota no ha sido alimentada aun "}), 404