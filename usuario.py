#Clase usuario
class Usuario:
    #Constructor
    def __init__(self, matricula, nombre, apellido, trimestreActual):
        self.__matricula = matricula
        self.__nombre = nombre
        self.__apellido = apellido
        self.__trimestreActual = trimestreActual
        self.__numEjemplaresPrestamo = 0
        self.__adeudos = 0
        self.__librosPrestamo = [] #Aqui se guardaran los libros en prestamo que tenga el usuario
        
        
    #Métodos getter's
    def getMatricula(self):
        return self.__matricula
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getNumEjemplaresPrestamo(self):
        return self.__numEjemplaresPrestamo
    
    def getTrimestreActual(self):
        return self.__trimestreActual
    
    def getAdeudos(self):
        return self.__adeudos
    
    #Metodo que suma 1 al numero de ejemplares que tiene un usuario en prestamo
    def agregarLibroPrestamo(self):
        self.__numEjemplaresPrestamo = self.__numEjemplaresPrestamo + 1
    
