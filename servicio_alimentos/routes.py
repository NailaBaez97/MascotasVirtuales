from flask import Blueprint, request, jsonify
from models import db, Alimentacion
import datetime

alimentos_bp = Blueprint('alimentos_bp', __name__)

@alimentos_bp.route('/alimento', methods=['POST'])
def alimento_mascota():
    data = request.get_json()
    mascota_id = data['mascotaId']
    hora_alimentacion = datetime.datetime.now().isoformat()

    #Crear un nuevo registro
    nueva_alimentacion = Alimentacion(mascota_id = mascota_id, hora_alimentacion = hora_alimentacion)
    db.session.add(nueva_alimentacion)
    db.session.commit()

    return jsonify({"mensje":"Mascota alimentada", "alimentacion":{
        'mascotaId' : mascota_id,
        'hora_alimentacion' : hora_alimentacion
    }}), 201

@alimentos_bp.route('/ultima_alimentacion/<int:mascota_id>', methods = ['GET'])
def obtener_ultima_alimentacion(mascota_id):

    ultima_alimentacion = Alimentacion.query.filter(mascota_id = mascota_id).order_by(Alimentacion.id.desc()).first()
    if ultima_alimentacion:
        return({
            'mascotaId' : ultima_alimentacion.mascota_id,
            'hora_alimentacion' : ultima_alimentacion.hora_alimentacion
        })
    else:
        return jsonify({"mensaje": "Mascota no ha sido alimentada aun "}), 404