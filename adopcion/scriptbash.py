import sqlite3

# Conectar a la base de datos
conexion = sqlite3.connect("adopcion.db")
cursor = conexion.cursor()

# Consulta para obtener adopciones con información de usuario y mascota
cursor.execute('''
SELECT a.adopcion_id, u.nombre_usuario, m.nombre_mascota, a.fecha_adopcion
FROM adopcion a
JOIN usuarios u ON a.usuario_id = u.usuario_id
JOIN mascotas m ON a.mascota_id = m.mascota_id
''')

# Obtener resultados
adopciones = cursor.fetchall()

# Mostrar resultados
for adopcion in adopciones:
    print(f'Adopción ID: {adopcion[0]}, Usuario: {adopcion[1]}, Mascota: {adopcion[2]}, Fecha de adopción: {adopcion[3]}')

# Cerrar conexión
conexion.close()
