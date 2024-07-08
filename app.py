from flask import Flask
from flask_cors import CORS



app = Flask (__name__)
# app.json.ensure_ascii = False

#r= que lo tome crudo, por si algun caracter que no va
#mi API es publica
cors = CORS(app, resources={r"/api-turismo/*": {"origins": "*"}})

#Importo las vistas
from componentes.vistas_api import *
from componentes.vistas_web import *
#@app.route('/')
#def inicio():
#    return "<h1>BIENVENIDOS A FLASK</h1>"


# if __name__ == '__main__':
#     app.run()