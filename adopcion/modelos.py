import sqlite3

conexion=sqlite3.connect("adopcion.db")
cursor = conexion.cursor()

# Crear la tabla de usuarios
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    usuario_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_usuario VARCHAR(50) NOT NULL,
    ci INTEGER NOT NULL UNIQUE
)
''')

# Tabla de mascotas (sin cambios)
cursor.execute('''
CREATE TABLE IF NOT EXISTS mascotas (
    mascota_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre_mascota TEXT NOT NULL,
    tipo_mascota TEXT NOT NULL
)
''')

# Tabla de adopcion (corrigiendo la redundancia)
cursor.execute('''
CREATE TABLE IF NOT EXISTS adopcion (
    adopcion_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fecha_adopcion DATE NOT NULL,
    usuario_id INTEGER,
    mascota_id INTEGER,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(usuario_id),
    FOREIGN KEY (mascota_id) REFERENCES mascotas(mascota_id)
)
''')

conexion.commit()       
conexion.close()