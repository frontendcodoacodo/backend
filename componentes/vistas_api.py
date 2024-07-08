#Vistas para la arquitectura API REST
from flask import jsonify
from flask import render_template
from flask import request

from app import app
from componentes.modelos import Lugar_turistico
from componentes.modelos import Actividad
from componentes.modelos import Guia_turistica
from componentes.modelos import Guia

@app.route("/api-turismo/guias_turisticas", methods=['GET'])
def api_guias_turisticas():
    guias_turisticas = Guia_turistica.obtener()
    datos = [guia_turistica.__dict__ for guia_turistica in guias_turisticas]

    for dato in datos:
        t_id = dato['lugar_turistico_id']
        dato["lugar_turistico"] = Lugar_turistico.obtener('id', t_id).__dict__["lugar_turistico"]
        dato['guia'] = Guia.obtener('id', dato['guia_id']).__dict__

        del dato["lugar_turistico_id"]
        del dato['guia_id']

    return jsonify(datos)

@app.route("/api-turismo/lugar_turisticos", methods=['GET'])
def api_lugar_turisticos():
    lugar_turisticos = Lugar_turistico.obtener()
    datos = [lugar_turistico.__dict__ for lugar_turistico in lugar_turisticos]

    for dato in datos:
        dato["actividad"] = Actividad.obtener('id', dato["actividad_id"]).__dict__["actividad"]


        del dato["actividad_id"]

    return jsonify(datos)

@app.route("/api-turismo/guias", methods=['GET'])
def api_guias():
    guias = Guia.obtener()
    datos = [guia.__dict__ for guia in guias]
    return jsonify(datos)

@app.route("/api-turismo/guia_turistica/<id>/detalle", methods=['GET'])
def api_detalle_guia_turistica(id):
    guia_turistica = Guia_turistica.obtener('id', id)
    return jsonify(guia_turistica.__dict__)

