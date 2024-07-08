import mysql.connector

#config de desarrollo local, establezco la conexion
# config_dev = {
#   'user': 'root',
#   'password': '',
#   'host': '127.0.0.1',
#   'database': 'turismo_db2',
# }

#datos de nuestro despliegue: pythonanywhere
config_prod = {
  'user': 'eviruel',
  'password': 'backend82',
  'host': 'eviruel.mysql.pythonanywhere-services.com',
  'database': 'eviruel$backend',
}

conexion = mysql.connector.connect(**config_prod)
