import mysql.connector

#config de desarrollo local, establezco la conexion
config_dev = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'turismo_db2',
}

#datos de nuestro despliegue: pythonanywhere, editar cuando tengamos
config_prod = {
  'user': 'ChToleCAC',
  'password': '2024CACPythonFS',
  'host': 'ChToleCAC.mysql.pythonanywhere-services.com',
  'database': 'ChToleCAC$default',
}

conexion = mysql.connector.connect(**config_dev)  