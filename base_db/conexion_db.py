import mysql.connector

#config de desarrollo local, establezco la conexion
config_dev = {
  'user': 'root',
  'password': '',
  'host': '127.0.0.1',
  'database': 'turismo_db2',
}

#datos de nuestro despliegue: pythonanywhere
config_prod = {
  'user': 'juampaCaC',
  'password': 'prueba1234',
  'host': 'juampaCaC.mysql.pythonanywhere-services.com',
  'database': 'juampaCaC$turismo_db2024',
}

conexion = mysql.connector.connect(**config_dev)  