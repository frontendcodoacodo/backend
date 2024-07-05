#Vistas segun patron MVT (Model View Template)
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

from app import app
from componentes.modelos import Guia_turistica
from componentes.modelos import Guia
from componentes.modelos import Lugar_turistico



# ****** Inicio ******
@app.route('/')
def inicio():
    return render_template('inicio.html')

# ****** Modelos ******
@app.route('/guias_turisticas')
@app.route('/guias_turisticas/<mensaje>')
def guias_turisticas(mensaje=None):
    guias_turisticas = Guia_turistica.obtener()
    
    for guia_turistica in guias_turisticas:
        guia_turistica.lugar_turistico_id = Lugar_turistico.obtener('id', guia_turistica.lugar_turistico_id)
        guia = Guia.obtener('id', guia_turistica.guia_id)
        d_nom = guia.nombre
        guia_turistica.guia = f"{d_nom}"
    
    return render_template('./modelos/guias_turisticas.html', guias_turisticas=guias_turisticas, mensaje=mensaje)

@app.route('/guias')
@app.route('/guias/<mensaje>')
def guias(mensaje=None):
    guias = Guia.obtener()
    return render_template('./modelos/guias.html', guias=guias, mensaje=mensaje)



# ****** Detalle de registros y CRUD ******
tablas = {
    "guia": Guia,
    "guia_turistica": Guia_turistica
}

@app.route('/<id>/<tipo>/detalle')
def ver_detalle(id, tipo):
    return render_template("./modelos/crud/detalle.html", 
                           datos=tablas[tipo].obtener('id', id), 
                           tipo=tipo)

@app.route('/<id>/<tipo>/eliminar')
def eliminar(id, tipo):
    respuesta = tablas[tipo].eliminar(id)
    return redirect(url_for(tipo + "s", mensaje=respuesta))

@app.route('/<id>/<tipo>/modificar', methods=['POST'])
def modificar(id, tipo):
    
    if request.method == 'POST':
        datos = dict(request.form)
        datos['id'] = id
        respuesta = tablas[tipo].modificar(datos)
        
    return redirect(url_for(tipo + "s", mensaje=respuesta))

@app.route('/<tipo>/crear', methods=['GET', 'POST'])
def crear(tipo):
    
    if request.method == 'POST':
        datos = dict(request.form).values()
        nvo_registro = tablas[tipo](*list(datos))
        respuesta = nvo_registro.guardar_db()
        return redirect(url_for(tipo + "s", mensaje=respuesta))        
    
    modelo = tablas[tipo].campos[1:]  
    return render_template('./modelos/crud/crear.html', tipo=tipo, modelo=modelo)
    

# ****** API EdTech ****** **** API TURISMO****
@app.route('/api-turismo')
def api_docu():
    return render_template('./api-turismo/docu.html')

# ****** Manejo de URL incorrecta ******
@app.errorhandler(404)
def lanzar_error(error):
    return render_template("./404.html", ctx=error)
