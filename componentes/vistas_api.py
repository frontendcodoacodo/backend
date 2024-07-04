#Vistas para la arquitectura API REST
from flask import jsonify

from app import app
from componentes.modelos import Actividad

@app.route('/api-turismo/actividades')
def mostrar_actividades():
    actividades = Actividad.obtener()
    datos = [vars(actividad) for actividad in actividades]
    return jsonify(datos)