from base_db.conexion_db import conexion as conexion
from base_db.tabla_db import Tabla

        
class Guia_turistica(Tabla):
    
    tabla = 'guia_turistica'
    conexion = conexion
    campos = ('id', 'lugar_turistico_id', 'fecha_inicio', 'fecha_cierre', 'guia_id', 'cupo')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)
        
class Guia(Tabla):
    
    tabla = 'guia'
    conexion = conexion
    campos = ('id', 'nombre', 'dni')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)
        
class Lugar_turistico(Tabla):
    
    tabla = 'lugar_turistico'
    conexion = conexion
    campos = ('id', 'nombre', 'actividad_id', 'descripcion')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)
        
class Actividad(Tabla):
    
    tabla = 'actividad'
    conexion = conexion
    campos = ('id', 'actividad')
    
    def __init__(self, *args, de_bbdd=False):
        super().crear(args, de_bbdd)

