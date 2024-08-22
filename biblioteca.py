#Clase biblioteca
class Biblioteca:
    #Constructor
    def __init__(self, idBiblioteca, nombreBiblioteca, ubicacion):
        self.__idBiblioteca = idBiblioteca
        self.__nombreBiblioteca = nombreBiblioteca
        self.__ubicacion = ubicacion
        self.__libros = []
        
    #Métodos getter's
    def getIdBiblioteca(self):
        return self.__idBiblioteca
    
    def getNombreBiblioteca(self):
        return self.__nombreBiblioteca
    
    def getUbicacion(self):
        return self.__ubicacion
    
    #Método para agregar un libro al catálogo de una nueva biblioteca
    def agregarNuevoLibro(self):
        pass
    
    #Método para mostrar el catalogo de libros de esa biblioteca
    def mostrarCatalogo(self):
        pass
    
    