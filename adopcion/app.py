from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Función para conectar a la base de datos
def get_db_connection():
    conn = sqlite3.connect('adopcion.db')
    conn.row_factory = sqlite3.Row
    return conn

# Endpoint para agregar un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def agregar_usuario():
    nombre_usuario = request.json['nombre_usuario']
    ci = request.json['ci']

    conn = get_db_connection()
    cursor = conn.cursor()


    # Insertar el usuario en la tabla de usuarios
    cursor.execute('''
    INSERT INTO usuarios (nombre_usuario, ci)
    VALUES (?, ?)
    ''', (nombre_usuario, ci))

    conn.commit()
    conn.close()

    return jsonify({'mensaje': 'Usuario agregado con éxito'}), 201


# Endpoint para agregar una nueva mascota
@app.route('/mascotas', methods=['POST'])
def agregar_mascota():
    nombre_mascota = request.json['nombre_mascota']
    tipo_mascota = request.json['tipo_mascota']

    conn = get_db_connection()
    cursor = conn.cursor()


    # Insertar la mascota en la tabla de mascotas
    cursor.execute('''
    INSERT INTO mascotas (nombre_mascota, tipo_mascota)
    VALUES (?, ?)
    ''', (nombre_mascota, tipo_mascota))

    conn.commit()
    conn.close()

    return jsonify({'mensaje': 'Mascota agregada con éxito'}), 201

# Endpoint para adoptar una mascota
@app.route('/adoptar', methods=['POST'])
def adoptar():
    mascota_id = request.json['mascota_id']
    usuario_id = request.json['usuario_id']

    conn = get_db_connection()
    cursor = conn.cursor()

    # Insertar en la tabla de adopcion
    cursor.execute('''
    INSERT INTO adopcion (fecha_adopcion, usuario_id, mascota_id)
    VALUES (CURRENT_DATE, ?, ?)
    ''', (usuario_id, mascota_id))

    conn.commit()
    conn.close()

    return jsonify({'mensaje': 'Mascota adoptada con éxito'}), 201





if __name__ == '__main__':
    app.run(port=5000)
