#Clase Prestamo
class Prestamo:
    #Constructor
    def __init__(self, idAlumno, idLibro, nombreLibro, numPaginasLibro, inicioPrestamo, finPrestamo, tipoPrestamo):
        self.__idAlumno = idAlumno
        self.__idLibro = idLibro
        self.__nombreLibro = nombreLibro
        self.__numPaginasLibro = numPaginasLibro
        self.__inicioPrestamo = inicioPrestamo
        self.__finPrestamo = finPrestamo
        self.__tipoPrestamo = tipoPrestamo
        
        
    #Métodos getter's
    def getIdAlumno(self):
        return self.__idAlumno
    
    def getIdLibro(self):
        return self.__idLibro
    
    def getNombreLibro(self):
        return self.__nombreLibro
    
    def getNumPaginasLibro(self):
        return self.__numPaginasLibro
    
    def getInicioPrestamo(self):
        return self.__inicioPrestamo
    
    def getFinPrestamo(self):
        return self.__finPrestamo

    def getTipoPrestamo(self):
        return self.__tipoPrestamo
    
    