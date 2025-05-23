class Vehiculo:
    def __init__(self,nombre,tipo):
        self.nombre = nombre
        self.tipo = tipo
        print("Se ha creado con exito el objeto")
    
    def __del__(self):
        print("Se ha eliminado el objeto")
        
class Persona:
    def __init__(self,nombre,edad,grado_estudio ):
        self.nombre = nombre
        self.edad = edad
        self.grado_estudio = grado_estudio

        
class profesor(Persona):
    def _init__(self,titulo,maestria,tarjetapofesional):
        self.maestria= maestria
        self.titulo= titulo
        self.tarjetapofesional= tarjetapofesional
    def dictar_clase(self,dictado):
        self.dictado = dictado       
class estudiante(Persona):
    def __init__(self,nombre,edad,nivel_Estudio,):
        self.nombre = nombre
        self.edad = edad
        self.nivel_Estudio = nivel_Estudio
    super
class trajador(estudiante):
    def __init__(self,empresa,años_experiencia):
        self.empresa = empresa
        self.años_experiencia = años_experiencia
class Asistente(estudiante,trajador):
    def __init__(self,jefe):
        self.jefe = jefe
    print(f"los atributos que posee el asistente son ")