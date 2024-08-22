#Importacion del archivo que contiene la implementacion de la clase sistemaBiblioteca
from sistemaBiblioteca import SistemaBiblioteca

#Clase principal Main
class Main:
    
    #Creacion de un objeto de tipo sistemaBiblioteca
    sistemaBiblioteca = SistemaBiblioteca()
    
    #Variable que controlare las veces que deba de aparecer el menu de opciones
    otro = True
    
    #Ciclo que estara mostrando el menu de opciones cada vez que se vaya a hacer una nueva operacion en el sistema
    while otro:
        
        #Menu de opciones
        print("\nMenu del sistema de la biblioteca 'La biblioteca del lector'")
        print("\nOpcion\tAccion a realizar")
        print("1\t\tAgregar libro al catalogo\n2\t\tAgregar usuario\n3\t\tAgregar biblioteca en convenio\n4\t\tDar de baja a un usuario\n5\t\tDar de baja un libro\n6\t\tCosultar catalogo de libros\n7\t\tCosultar lista de alumnos que estan en el sistema\n8\t\tConsultar catalogo de bibliotecas en convenio\n9\t\tSolicitar prestamo\n10\t\tConsultar libros que se encuentran en prestamo con los usuarios\n11\t\tConsultar estatus de un alumno\n12\t\tRegresar libro por parte de un usuario\n13\t\tSalir del sistema")
    
        #Se le pide al usuario que ingrese una opcion de las disponiblles
        opc = int(input("\nIngrese el numero de opcion de la accion que desea realizar: "))
        
        #Sentencia match (hace el funcionamiento de un estructura selectiva múltiple)
        match opc:
            
            #Agregar libro al catalogo de la biblioteca
            case 1:
                sistemaBiblioteca.agregarLibro()
            
            #Agregar un usuario a los servicios de la biblioteca
            case 2:
                sistemaBiblioteca.agregarUsuario()
            
            #Agregar una biblioteca en convenio
            case 3:
                sistemaBiblioteca.agregarBibliotecaConvenio()
            
            #Dar de baja a un usuario
            case 4:
                sistemaBiblioteca.darBajaUsuario()
            
            #Dar de baja un libro del catalogo de libros
            case 5:
                sistemaBiblioteca.darBajaLibro()
            
            #Consultar el catalogo de libros
            case 6:
                sistemaBiblioteca.mostrarCatalogoLibros()
            
            #Consular alumnos que estan dados de alta en el sistema de la biblioteca
            case 7:
                sistemaBiblioteca.mostrarAlumnosSistema()
            
            #Consultar las bibliotecas con las que se tiene convenio
            case 8:
                sistemaBiblioteca.mostrarBibliotecasConvenio()
            
            #Solicitar un prestamo de la misma biblioteca
            case 9:
                sistemaBiblioteca.solicitarPrestamoMiBiblioteca()
            
            #Consultar los libros que se encuentran en prestamo con los usuarios de la biblioteca
            case 10:
                sistemaBiblioteca.verLibrosPrestamo()
          
            #Metodo para consultar el estatus de un alumno            
            case 11:                
                sistemaBiblioteca.consultarEstatusAlumno()
                
            #Metodo para que un usuario de la biblioteca regrese un libro a la biblioteca
            case 12: 
                sistemaBiblioteca.regresarLibro()
            
            #Salir del sistema, y terminar la ejecucion del programa
            case 13:
                otro = False
                
            case _: 
                print("La opcion que se ingreso es incorrecta. Favor de introducir la opcion correspondiente")
    
    
    print("\nFin de la ejecucion del sistema")