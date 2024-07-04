class Tabla:
    
    # Creación de la tabla
    def __init__(self, nombre, conexion, campos):
        self.tabla = nombre
        self.conexion = conexion
        self.campos = campos
    
    # *** CRUD ***
    # creador/constructor de instancias subclase
    def crear(self, valores, de_bbdd=False):
        if de_bbdd:
            # del modelo --> args = (valores) # (())
            for campo, valor in zip(self.campos, *valores):
                setattr(self, campo, valor)
        else:
            for campo, valor in zip(self.campos[1:], valores):
                setattr(self, campo, valor)
    
    def guardar_db(self):
        # campos_q = "('campo_2', ..... 'campo_n')"
        campos_q = str(self.campos[1:]).replace("'", "`")
        # values_q = "(%s, ..... %s )" #como cant de campos
        values_q = f"({'%s, ' * (len(self.campos)-2)} %s)"
        consulta = (f"INSERT INTO {self.tabla} {campos_q} "
                    f"VALUES {values_q};")
        datos = tuple(vars(self).values())
        rta_db = self.__conectar(consulta, datos)
        
        if rta_db:
            return 'Creación exitosa.'
        
        return 'No se pudo crear el registro.'
            
    #Lectura
    @classmethod
    def obtener(cls, campo=None, valor=None):
        
        if campo == None or valor == None:
            consulta = ("SELECT * " 
                       f"FROM {cls.tabla};")
            resultado = cls.__conectar(consulta)
        else:
            consulta = ("SELECT * " 
                       f"FROM {cls.tabla} "
                       f"WHERE {campo} = %s;")
            resultado = cls.__conectar(consulta, (valor,))
        
        return resultado
     
     #Eliminacion
    @classmethod
    def eliminar(cls, id):
        consulta = (f"DELETE FROM {cls.tabla} WHERE id = %s ;")
        rta_db = cls.__conectar(consulta, (id,))
        
        if rta_db:
            return 'Eliminación exitosa.'
            
        return 'No se pudo eliminar el registro.'
        
    #Modificacion
    @classmethod
    def modificar(cls, registro):
        #type(registro) = dictionary
        
        update_q = f"UPDATE {cls.tabla} "
        set_q = 'SET'
        
        id = registro.pop('id')
        id = int(id) if type(id) != int else id
        
        for c in list(registro.keys()):
            set_q += f' {c} = %s,'
        # SET nombre = %s, dni = %s
        set_q = set_q[0:-1]       
        # SET nombre = %s, dni = %s # saca la ultima coma
        where_q = f" WHERE id = %s;"
        consulta = update_q + set_q + where_q    
        nvos_datos = *list(registro.values()), id
        rta_db = cls.__conectar(consulta, nvos_datos)
        
        if rta_db:   
            return 'Modificación exitosa.'
        
        return 'No se pudo modificar el registro.'


    # *** Metodo en comun en CRUD (encapsulado) ***
    @classmethod        
    def __conectar(cls, consulta, datos=None):
        
        try:
            cursor = cls.conexion.cursor()
        except Exception as e:
            cls.conexion.connect()
            cursor = cls.conexion.cursor()
        
        if consulta.startswith('SELECT'):
            
            if datos != None:
                cursor.execute(consulta, datos)
            else:
                cursor.execute(consulta)
            
            rta_db = cursor.fetchall()
            
            # Lista por comprensión
            if rta_db != []:
                resultado = [cls(registro, de_bbdd=True) \
                                for registro in rta_db]
                
                if len(resultado) == 1:
                    resultado = resultado[0]
                    
            else:
                resultado = False          
            
            cls.conexion.close()
        
        else:
            
            try:
                cursor.execute(consulta, datos)
                cls.conexion.commit()    
                cls.conexion.close()
                resultado = True
            except Exception as e:
                resultado = False
            
        return resultado