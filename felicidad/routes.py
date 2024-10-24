from flask import Blueprint, jsonify
import requests
import datetime

felicidad_bp = Blueprint('felicidad_bp', __name__)

def calcular_felicidad(ultima_alimentacion):
    ahora = datetime.datetime.now()
    ultima_alimentacion_dt = datetime.datetime.fromisoformat(ultima_alimentacion)
    
    # Calculamos la diferencia en horas
    diferencia_horas = (ahora - ultima_alimentacion_dt).total_seconds() / 3600
    
    # Si han pasado menos de 5 horas, la mascota está feliz
    if diferencia_horas < 5:
        return "feliz"
    elif 5 <= diferencia_horas < 5:
        return "neutra"
    else:
        return "triste"

@felicidad_bp.route('/felicidad/<int:mascota_id>', methods=['GET'])
def verificar_felicidad(mascota_id):
    # Hacer una solicitud al servicio de alimentación para obtener la última alimentación
    response = requests.get(f'http://localhost:5001/ultima_alimentacion/{mascota_id}')

    if response.status_code == 200:
        data = response.json()
        ultima_alimentacion = data['hora_alimentacion']  # Asegúrate de usar el campo correcto
        felicidad = calcular_felicidad(ultima_alimentacion)
        return jsonify({"mascotaId": mascota_id, "felicidad": felicidad}), 200

    return jsonify({"mascotaId": mascota_id, "felicidad": "triste"}), 200
