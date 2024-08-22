#clase libro
class Libro:
    #Constructor
    def __init__(self, idLibro, titulo, numEjemplares, numPaginas):
        self.__idLibro = idLibro
        self.__titulo = titulo
        self.__numEjemplares = numEjemplares
        self.__numPaginas = numPaginas
        self.__estado = "Disponible"
        
    #Metodos setter
    def setEstado(self, estado):
        self.__estado = estado
        
    #Métodos getter's
    def getIdLibro(self):
        return self.__idLibro
    
    def getTitulo(self):
        return self.__titulo
    
    def getNumEjemplares(self):
        return self.__numEjemplares
    
    def getNumPaginas(self):
        return self.__numPaginas
    
    def getEstado(self):
        return self.__estado
    
    #Método para actualizar el numero de ejemplares de un libro que hay en el catalogo
    
    #Aumentar el numero de ejemplares de un libro
    def actualizarMas(self):
        pass
    
    #Decrementar el numero de ejemplares de un libro de la biblioteca
    def actualizarMenos(self):
        self.__numEjemplares = self.__numEjemplares - 1
    
    