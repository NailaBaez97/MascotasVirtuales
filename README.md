# MASCOTASVIRTUALES

## Descripción

MASCOTAS VIRTUALES es un sistema de microservicios que permite gestionar la adopción de mascotas, su alimentación y el rastreo de su felicidad. Cada microservicio está diseñado para cumplir una función específica y se comunican entre sí a través de API REST.

## Estructura del Proyecto
MASCOTASVIRTUALES
| |- adopcion
    | - adopcion.db 
    | - app.py 
    | - modelos.py
    | - requirements.txt
|- servicio_alimentos 
    | - instance 
      | - Alimentacion.db 
  | - app.py 
  | - config.py 
  | - models.py 
  | - routes.py
  | - requirements.txt 
|- felicidad 
  | - app.py 
  | - config.py 
  | - models.py 
  | - routes.py 
  | - requirements.txt
|- mascotas-env

## Microservicios

### 1. Adopción

- *Descripción*: Gestiona la adopción de mascotas, permitiendo registrar usuarios y mascotas, así como llevar un historial de adopciones.
- *Base de Datos*: Utiliza SQLite (adopcion.db).
- *Endpoints*:
  - POST /usuarios: Agregar un nuevo usuario.
  - POST /mascotas: Agregar una nueva mascota.
  - POST /adoptar: Adoptar una mascota.

### 2. Servicio de Alimentos

- *Descripción*: Registra las alimentaciones de las mascotas y permite consultar la última alimentación de una mascota.
- *Base de Datos*: Utiliza SQLAlchemy para gestionar la base de datos (Alimentacion.db).
- *Endpoints*:
  - POST /alimento: Registrar la alimentación de una mascota.
  - GET /ultima_alimentacion/<int:mascota_id>: Obtener la última alimentación de una mascota.

### 3. Servicio de Felicidad

- *Descripción*: Evalúa la felicidad de una mascota en función de la última alimentación.
- *Base de Datos*: Utiliza SQLAlchemy para extraer la ultima alimentacion(Alimentacion.db).
- *Endpoints*:
  - GET /felicidad/<int:mascota_id>: Consultar la felicidad de una mascota.

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <url_del_repositorio>
   cd MASCOTASVIRTUALES
Crea un entorno virtual e instale las dependencias:
cd mascotas-env
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

1 - Inicia el servicio de adopción:
python3 adopcion/app.py

2 -  Inicia el servicio de alimentos:
python3 servicio_alimentos/app.py

3 - python3 felicidad/app.py

## Los servicios estarán disponibles en los siguientes puertos:

    Adopción: http://localhost:5000
    Alimentos: http://localhost:5001
    Felicidad: http://localhost:5002

Pruebas

Puedes probar los endpoints usando herramientas como Postman o Thunder Client.

Notas:

    Asegúrate de que todos los servicios estén corriendo para que se puedan comunicar entre sí.
    Modifica las configuraciones de la base de datos según sea necesario para tu entorno.
