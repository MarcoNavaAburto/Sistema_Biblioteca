#Se declara la librería datetime para guardar las fechas que se hacen los prestámos y las fechas de las devoluciones
import datetime
#Importacion del archivo que contiene la implementacion de la clase Libro
from libro import Libro
#Importacion del archivo que contiene la implementacion de la clase usuario, esto para poder ocupar la clase y los metodos de la misma
from usuario import Usuario
#Importacion del archivo que contiene la implementacion de la clase usuario, esto para poder ocupar la clase y los metodos de la misma
from biblioteca import Biblioteca
#Importacion del archivo que contiene la implementacion de la clase Prestam, esto para poder acceder a las funciones de la misma
from prestamo import Prestamo

#Clase sistemaBiblioteca
class SistemaBiblioteca():
    #Constructor
    def __init__(self):
        self.__catalogoLibros = [] #Se guardan los libros que estan en el sistema de la biblioteca
        self.__bibliotecasConvenio = [] #Se guarda la información de las bibliotecas con las que se tiene un convenio
        self.__usuarios = [] #Se guarda la lista de los usuarios que forman parte de los servicios que ofrece la biblioteca
        self.__librosPrestamosUsuarios = [] #Aqui se guardara la informacion de los libros que esten en préstamo
        #self.__ejemplaresEncontrados = [] #Ayuda en la función de dar de baja a un libro
        self.__ejemplaresDisponiblesLista = [] #Ayuda en el caso de uso de prestamos de un libro, guarda los ejemplares disponibles de algún título
        


    #Méotodo para agregar un libro al catalogo
    def agregarLibro(self):    
        #Variable contador que ira contando el numero de ejemplares de un libro que se han guardado
        contador = 1
        
        #Se solicita la informacion de libro que se guardara, asi como el identificador que se le asiganara a cada libro
        numEjemplares = int(input("\nIngrese el numero de ejemplares que se agregaran al catalogo: "))
        titulo = input("Ingrese el titulo del libro: ")
        titulo = titulo.capitalize()
        numPaginas = int(input("Ingrese el numero de paginas que tiene el libro: "))
        
        #Ciclo que ira agregando los libros al catalogo
        while contador<=numEjemplares:
            #Se solicita al usuario que ingrese el ID que se le asignara al libro
            idLibro = int(input(f"Ingrese el ID que se le asignara al libro {contador} con el titulo {titulo}: "))
            
            #Funcion que retorna si el ID que se ingreso es un ID valido y no repetido para que pueda ser usado como un nuevo ID en un libro
            valido = self.__validarIdLibro(idLibro)
            
            if valido:
                #Creación de un objeto de tipo libro
                libro = Libro(idLibro, titulo, numEjemplares, numPaginas)
            
                #Se agrega el libro al catalogo de libros de la biblioteca
                self.__catalogoLibros.append(libro)
            
                #Se incrementa el contador para poder ingresar el identificador del siguiente ejemplar
                contador = contador + 1
                
            else:
                print(f"El id {idLibro} ya se encuentra ocupado. Favor de ingresar un nuevo ID")
            
        #Mensaje de exito al usuario
        print("\nLos libros se agregaron exitosamente al catalogo")
   
    
    #Funcion que validad que un identificador pueda ser asignado a un libro que se vaya a registrar al catalogo de los libros de la biblioteca
    def __validarIdLibro(self, idLibro):
        validar = True
        
        #Recorriendo la lista para validad el ID que se desea asignar
        for libro in self.__catalogoLibros:
            if libro.getIdLibro() == idLibro:
                validar = False
                break
        
        return validar
    
        
    #Método para agregar usuarios a los servicios de la biblioteca
    def agregarUsuario(self):
        #Solicitar la informacion al usuario
        matricula = int(input("\nIngrese el numero de matricula del alumno: "))
        
        #Variable que guardara el valor para indicar que si se puede registrar ese alumno porque no hay matriculas repetidas
        valido = self.__validarMatriculaAlumno(matricula)
        
        if valido:  
            nombre = input("Ingrese el nombre del alumno: ")
            apellido = input("Ingrese el apellido del alumno: ")
            trimestreActual = int(input("Ingrese el trimestre actual del alumno: "))
        
            #Creacion de un objeto de tipo usuario
            usuario = Usuario(matricula, nombre, apellido, trimestreActual)
        
            #Se agrega el usuario nuevo a la lista de los usuarios de la biblioteca
            self.__usuarios.append(usuario)
            
            #Se indica que el usuario fue ingresado correctamente
            print("\nEl usuario fue ingresado correctamente")
            
        else:
            print(f"\nNo se pudo agregar al usuario porque la matricula {matricula} ya se encuentra registrada en la lista de usuarios")
            print("Sera redireccionado al menu principal del menu de opciones, en caso de agregar un nuevo usuario tendra que ingresar una matricula valida")

    
    #Metodo que retorna si hay matriculas repetidas o no en la lista de usuarios del sistema
    def __validarMatriculaAlumno(self, matricula):
        #Variable booleana que guarda el valor de True en caso de que se puede usar la matricula, o False en caso de que no se pueda usar porque ya hay repeticiones
        validar = True
        
        #Se recorre la lista de usuarios para revisar que no haya repeticiones
        for usuario in self.__usuarios:
            if usuario.getMatricula() == matricula:
                validar = False
                break
            
        return validar
            
            

    #Método para agregar una biblioteca con la que se va a tener un convenio
    def agregarBibliotecaConvenio(self):
        #Se le solicita la información al usuario
        idBiblioteca = int(input("\nIngrese el ID de la biblioteca: "))
        
        #Variable que guarda el valor en caso de que el ID que se vaya a querer asignar este disponible
        valido = self.__validarIdBiblioteca(idBiblioteca)
        
        if valido:
            nombreBiblioteca = input("Ingrese el nombre de la biblioteca: ")
            ubicacion = input("Ingrese la ubicacion de la biblioteca: ")
        
            #Se crea un objeto de tipo biblioteca
            biblioteca = Biblioteca(idBiblioteca, nombreBiblioteca, ubicacion)
        
            #Se agrega la biblioteca a la lista de las bibliotecas con las que se tiene convenio
            self.__bibliotecasConvenio.append(biblioteca)
        else:
            print("\nNo se puede registrar el convenio porque el ID que se le quiere asignar a la biblioteca ya se encuentra ocupado por otra biblioteca")
            print("Sera redireccionado al menu principal de la biblioteca. En caso de querer repetir la operacion tiene que ingresar otro ID diferente")
            
        
    def __validarIdBiblioteca(self, idBiblioteca):
        valido = True
        
        #Se revisa que el ID que se quiere asignar no este asignado a otra biblioteca
        for biblioteca in self.__bibliotecasConvenio:
            if biblioteca.getIdBiblioteca() == idBiblioteca:
                valido = False
                break
        
        return valido
    
    
    #Metodo para dar de baja a un usuario
    def darBajaUsuario(self):
        
        #Se verifica que haya alumnos en el sistema, de lo contrario no tiene chiste borrar a alguien del sistema sino hay quien este registrado
        if len(self.__usuarios) == 0:
            
            print("\nNo hay ningun usuario que forma parte del sistema, por lo que no es necesario dar de baja a alguien")
            return
        
        #En caso de que haya alumnos en el sistema, se sigue el procedimiento correspondiente para eliminarlos
        else:
            #Se solicita el identificador del usuario(la matricula del alumno)
            idUsuario = int(input("\nIngrese la matricula del usuario que quiere borrar del sistema: "))
            #Se declara una variable bandera que indicara cuando el id haya sido encontrado
            encontrado = False
        
            #Se recorre la lista en busca del id que se desea encontrar
            for usuario in self.__usuarios:
                #Si el id es encontrado con la variable bandera se indica que si se encontro el id a dar de baja y se borra el usuario
                if idUsuario == usuario.getMatricula():
                    encontrado = True
                    self.__usuarios.remove(usuario)
                    break
                
            #Si el usuario fue encontrado, se le indica al usuario que se borro exitosamente al alumno
            if encontrado:
                print(f"El usuario con matricula {idUsuario} fue borrado exitosamente")
            #En caso de que no haya sido encontrado se le indica al administrador que el alumno 
            else:
                print(f"No existe un usuario con la matricula {idUsuario}")
         
    
         
    #Metodo para dar de baja a un libro del catalogo del sistema
    def darBajaLibro(self):
        #Se verifica que haya libros en el sistema, esto para que tenga sentido hacer una baja de algun libro
        if len(self.__catalogoLibros) != 0:
            #Se le pide al usuario que ingrese el identificador del libro
            idLibro = int(input("\nIngrese el ID del libro que desea dar de baja del sistema: "))
            #Se declara una variable de tipo bool que guarda el valor de false, suponiendo que el libro no se encuentra en el catalogo
            encontrado = False
            nombreLibro = ""
            
            #Se recorre el catalogo de libros
            for libro in self.__catalogoLibros:
                #Se compara el ID que se esta buscando con el del libro que en ese momento se esta buscando en la lista
                if idLibro == libro.getIdLibro():
                    #Si el libro se encuentra se cambia el valor de la variable encontrado de false a true, eso quiere decir que el libro fue encontrado
                    encontrado = True
                    
                    #Se revisa cuantos ejemplares hay sobre ese libro para en caso de que haya más de 1, hacer la actualización correspondiente
                    if libro.getNumEjemplares()>1:
                        #Se guarda el nombre del libro para poder identificar a los demas ejemplares
                        nombreLibro = libro.getTitulo()
                        #Se manda a una funcion el numero de ejemplares del libro para actualizar el numero de ejemplares
                        self.__actualizarEjemplaresMenos(nombreLibro)
                    
                    #Se borra el libro del catalogo de libros de la biblioteca
                    self.__catalogoLibros.remove(libro)
                    break
               
            #Si el libro fue encontrado se le indica al usuario que el libro fue encontrado y fue dado de baja del sistema
            if encontrado:
                print(f"\nEl libro con ID {idLibro} ha sido dado de baja del sistema")
            #Si el libro no se encontro en el catalogo del sistema se le indica al usuario que no hay ningún libro que tenga ese ID que ingreso hace un momento
            else:
                print(f"\nEl libro con ID {idLibro} no fue encontrado en el catalogo")
            
            
            if nombreLibro != "":
                print("\nLa informacion del libro queda como sigue\n")
                for libro in self.__catalogoLibros:
                    if nombreLibro == libro.getTitulo():
                        print(f"\nTitulo del libro: {libro.getTitulo()}\nNumero de ejemplares: {libro.getNumEjemplares()}\nNumero de paginas: {libro.getNumPaginas()}\n\nLa informacion de cada ejemplar esta de la siguiente manera")
                        self.__imprimirDisponibles(nombreLibro)
          
                        break          
        #En caso de que no haya libros se le indica al usuario
        else:
            print("\nNo hay libros en el sistema, por lo que no es necesario hacer ninguna baja de algun libro")
                
    
    #Metodo para saber los ejemplares de un libro y si estan disponibles o no
    def __imprimirDisponibles(self, nombreLibro):
        print(f"\nInformacion del libro\nTitulo del libro: {nombreLibro}")
        for libro in self.__catalogoLibros:
            if nombreLibro == libro.getTitulo():
                print(f"\nId del libro: {libro.getIdLibro()}\nEstado del libro: {libro.getEstado()}\n")
                
                #Si el libro esta disponible se agrega a la lista de los ejemplares disponibles de un libro
                if libro.getEstado() == "Disponible":
                    self.__ejemplaresDisponiblesLista.append(libro)
                
                    
                
     
                
    #Metodo para actualizar el numero de ejemplares de un libro del sistema de la biblioteca
    def __actualizarEjemplaresMenos(self, nombreLibro):
        for libro in self.__catalogoLibros:
            if nombreLibro == libro.getTitulo():
   
                libro.actualizarMenos()
    
    
    
    #Metodo para consultar el catalogo de libros de la biblioteca
    def mostrarCatalogoLibros(self):
        #Se revisa que haya libros en el sistema, en caso de que no haya libros en el catalogo se manda el mensaje correspondiente
        if len(self.__catalogoLibros) != 0:
            print("\nLos libros que estan en el catalogo de la biblioteca son los siguientes: ")
            for libro in self.__catalogoLibros:
                print(f"\nID del libro: {libro.getIdLibro()}\nTitulo del libro: {libro.getTitulo()}\nNumero de ejemplares: {libro.getNumEjemplares()}\nNumero de paginas: {libro.getNumPaginas()}\nEstado del libro: {libro.getEstado()}")
        else:
            print("\nNo hay libros en el catalogo del sistema")
            
    
            
    #Mostrar alumnos que estan dados de alta en el sistema de la biblioteca
    def mostrarAlumnosSistema(self):
        #Se revisa que haya alumnos en el sistema de la biblioteca, en caso de que no haya usuarios registrados en el sistema de la biblioteca se manda el mensaje correspondiente
        if len(self.__usuarios) != 0:
            for usuario in self.__usuarios:
                print(f"\nMatricula del alumno: {usuario.getMatricula()}\nNombre: {usuario.getNombre()}\nApellido del alumno: {usuario.getApellido()}\nLibros que tiene en prestamo el alumno: {usuario.getNumEjemplaresPrestamo()}\nTrimestre en el que deberia de estar inscrito: {usuario.getTrimestreActual()}\nNumero de libros que no ha devolvio en la fecha estipulada: {usuario.getAdeudos()}\n")
        else:
            print("\nNo hay usuarios registrados en el sistema de la biblioteca")
    
    
        
    #Metodo para mostrar la lista de las bibliotecas con las que se tiene un convenio
    def mostrarBibliotecasConvenio(self):
        #Se revisa que haya bibliotecas con las que se tenga convenio, dependiendo el caso se manda la informacion o el mensaje correspondiente
        if len(self.__bibliotecasConvenio) != 0:
            print("\nInformacion de las bibliotecas con las que se tiene convenio")
            for biblioteca in self.__bibliotecasConvenio:
                print(f"\nID de la biblioteca: {biblioteca.getIdBiblioteca()}\nNombre: {biblioteca.getNombreBiblioteca()}\nUbicacion: {biblioteca.getUbicacion()}")
        else:
            print("\nNo hay bibliotecas en convenio")
                        
            
    #Metodo para solicitar el prestamo de un libro que esta dentro del catalogo de la biblioteca
    def solicitarPrestamoMiBiblioteca(self):
        #Bandera que indicara si hay algun libro con el ID que haya ingresado el usuario
        b = False
        #Se le indica al usuario que indique la forma en que quiere buscar al libro
        print("\nMenu de busquedas")
        print("\nOpcion\tTipo de busqueda\n1\t\tBusqueda por identificador del libro\n2\t\tBusqueda por nombre del libro")
        
        #Se solicita ingrese la opcion que desea
        opc = int(input("\nIngrese el numero de la opcion por la cual decide seguir el proceso de prestamo: "))
        
        #Entra a los diferentes casos y se procede segpun corresponda
        if opc == 1:
            #Se solicita el ID del libro
            idLibro = int(input("\nIngrese el id del libro: "))
            
            #Se busca si existe un libro con el ID que se ingreso hace un momento
            for libro in self.__catalogoLibros:
                if libro.getIdLibro() == idLibro:
                    #Se hace la obtencion del titulo del libro
                    tituloLibro = libro.getTitulo()
                    #Con la variable de bandera se indica que si se encontro dicho ID
                    b = True
                    self.__ejemplaresDisponiblesFuncion(tituloLibro)
                    break
            
            #Con el valor de la bandera como True, se llama a otra función para completar el prestamo del libro 
            if b:
                self.__seguirPrestamo()
            else:
                print(f"\nEn el sistema no hay ningun libro registrado con el ID {idLibro}")
                
                
        elif opc == 2:
            #Se solicita el nombre del libro
            nombreLibro = input("\nIngrese el nombre del libro: ")
            
            #Se cambia la primera letra de la cadena a mayusculas y las demas se pasan a minusculas
            nombreLibro = nombreLibro.capitalize()
            
            for libro in self.__catalogoLibros:
                if libro.getTitulo() == nombreLibro:
                    b = True
                    #Se llama a la función que imprime la informacion de los ejemplares de un libro
                    self.__ejemplaresDisponiblesFuncion(nombreLibro)
            
            if b:
                self.__seguirPrestamo()
            else:
                print(f"\nEn el catalogo de libros no hay ningun libro con el titulo de '{nombreLibro}'")
            
        else:
            print("\nFavor de ingresar una opcion valida, sera redireccionado al menu principal de la biblioteca")
        
       
    #Metodo para saber los ejemplares de un libro y si estan disponibles o no (Este método se ejecuta cuando se solicita el prestamo de un libro)
    def __ejemplaresDisponiblesFuncion(self, nombreLibro):
        print(f"\nInformacion del libro\nTitulo del libro: {nombreLibro}")
        
        #Imprime la informacion del libro sin importar si su estado es disponible o en prestamo
        for libro in self.__catalogoLibros:
            if nombreLibro == libro.getTitulo():
                print(f"\nId del libro: {libro.getIdLibro()}\nEstado del libro: {libro.getEstado()}\n")
                    
                #Si el libro esta disponible se agrega a la lista de los ejemplares disponibles de un libro
                if libro.getEstado() == "Disponible":
                    self.__ejemplaresDisponiblesLista.append(libro)
                    
    
    #Metodo auxiliar para poder seguir con el caso de uso del prestamo de un libro
    def __seguirPrestamo(self):
        alumnoEncontrado = False
        
        #Si ningun libro esta disponible se manda el mensaje correspondiente de que estan en prestamo
        if len(self.__ejemplaresDisponiblesLista) == 0:   
            print("Todos los ejemplares estan en prestamo. Por lo que no se puede hacer el prestamo del libro deseado")
        
        else:
            #Se continua con el prestamo de un ejemplar
            print("Si se puede realizar el prestamo")
            
            #Se piden los datos necesarios
            idLibroPrestamo = int(input("\nIngrese el ID del libro que este disponible y que quiere pedir para prestamo: "))
            matriculaAlumno = int(input("Ingrese la matricula del usuario: "))
            
            #En busqueda de la informacion del usuario que quiere solicitar el prestamo
            for usuario in self.__usuarios:
                if usuario.getMatricula() == matriculaAlumno:
                    alumnoEncontrado = True
                    if usuario.getNumEjemplaresPrestamo() < 5 and usuario.getAdeudos() == 0: 
                        self.__completarPrestamo(idLibroPrestamo, usuario)
                        #Se hace el prestamo
                    else:
                        print(f"\nEl alumno con matricula {usuario.getMatricula()} tiene libros que no ha devuelto. \nPuede tener como maximo 5 libros en prestamo simultaneamente")
                        print(f"Numero de ejemplares que tiene en prestamo: {usuario.getNumEjemplaresPrestamo()}")
                        print(f"Numero de libros que tiene en adeudo: {usuario.getAdeudos()}\n")
            
            #En caso de que el alumno no se encuentre en la lista de usuarios de la biblioteca se despliega el siguiente mensaje
            if alumnoEncontrado == False:
                print(f"\nEl alumno con matricula {matriculaAlumno} no se encuentra como usuario de los servicios de la biblioteca")
                
            self.__ejemplaresDisponiblesLista.clear() #Limpia la lista para que cuando no haya libros en el catalogo, la lista no quede con libros que ya no estan en el catalogo
        
    
    #Metodo que ayuda a completar el prestamo a un usuario de la biblioteca
    def __completarPrestamo(self, idLibroPrestamo, usuario):
        for libro in self.__catalogoLibros:
            if libro.getIdLibro() == idLibroPrestamo:
                self.__prestarLibro(libro, idLibroPrestamo, usuario)
                
    
    #Método para prestar el libro
    def __prestarLibro(self, libro, idLibroPrestamo, usuario):
        print("\nOpcion\tTipo de prestamo\tDuracion")
        print("1\t\tPrestamo regular\t2 semanas\n2\t\tPrestamo rapido\t\t2 dias")
        
        tipoPrestamo = int(input("\nIngrese la opcion del tipo de prestamo que desea hacer: "))
        
        if tipoPrestamo == 1 or tipoPrestamo == 2:
            if tipoPrestamo == 1:
                #Se indica el tipo de prestamo y el tiempo que dura el prestamo en cantidad de dias
                prestamoTipo = "Prestamo regular"
                dias = 14
                
            if tipoPrestamo == 2:
                #Se indica el tipo de prestamo y el tiempo que dura el prestamo en cantidad de dias
                prestamoTipo = "Prestamo rapido"
                dias = 2
            
            #Fecha actual incluyendo la hira exacta en cuanto se ejecuta la línea de código de abajo
            fecha = datetime.datetime.now()
            #Fecha sin la hora, es decir solo el día, mes y año
            inicioPrestamo = fecha.date()
            
            #Se pone la fecha de fin de prestamo
            finPrestamo = inicioPrestamo + datetime.timedelta(dias)
            
            #Se crea un objeto de tipo prestamo, que es el que guardara la informacion del prestamo del libro
            prestamo = Prestamo(usuario.getMatricula(), idLibroPrestamo, libro.getTitulo(), libro.getNumPaginas(), inicioPrestamo, finPrestamo, prestamoTipo)
            
            #Se agrega el prestamo a la lista de prestamos de libros hacia los usuarios
            self.__librosPrestamosUsuarios.append(prestamo)
            
            #Se le indica al libro que ya esta en prestamo, y la variable prestamo indica si es prestamo regular o prestamo rapido
            libro.setEstado(prestamoTipo)
            
            #Se actualiza el numero de ejemplares en prestamo que tiene el usuario
            usuario.agregarLibroPrestamo()
            
            #Se indica que el prestamo se ha realizado con exito
            print("\nEl prestamo se ha realizado con exito")
            
        else:
            print("\nDebe de ingresar una opcion valida. Sera redireccionado al menu principal del sistema")
            
            
    
    #Metodo para ver los libros que estan en prestamo
    def verLibrosPrestamo(self):
        if len(self.__librosPrestamosUsuarios) != 0:
            print("\nInformacion de los libros que estan en prestamo")
            for prestamo in self.__librosPrestamosUsuarios:
                print(f"\nID del alumno que tiene el libro: {prestamo.getIdAlumno()}\nID del libro que se encuentra en prestamo: {prestamo.getIdLibro()}\nNombre del libro: {prestamo.getNombreLibro()}\nNumero de paginas del libro: {prestamo.getNumPaginasLibro()}\nFecha de inicio de prestamo: {prestamo.getInicioPrestamo()}\nFecha de fin del prestamo: {prestamo.getFinPrestamo()}\nTipo de prestamo: {prestamo.getTipoPrestamo()}\n")
        else:
            print("\nNo hay libros en prestamo hacia los usuarios de la biblioteca")            


    #Metodo para consultar el estatus de un alumno
    def consultarEstatusAlumno(self):
        #Variable que servira como bandera
        encontrado = False
        
        #Se le solicita la informacion del alumno
        matricula = int(input("\nIngrese la matricula del alumno: "))

        #Se busca al usuario en la lista de usuarios de la biblioteca
        for usuario in self.__usuarios:
            if usuario.getMatricula() == matricula:
                encontrado = True
                print(f"\nMatricula: {usuario.getMatricula()}\nNombre: {usuario.getNombre()}\nApellido: {usuario.getApellido()}\nNumero de ejemplares que tiene en prestamo: {usuario.getNumEjemplaresPrestamo()}\nNumero de adeudos: {usuario.getAdeudos()}\n")
                
        #En caso de que no haya sido encontrado se indica que no fue encontrado y sera redireccionado al menu principal
        if encontrado == False:
            print(f"\nEl alumno con {matricula} no se encuentra como usuario de la biblioteca. Sera redireccionado al menu principal de la biblioteca")
            
            
    #Metodo para que un usuario regrese un libro a la biblioteca        
    def regresarLibro(self):
        #Variable bandera que servira para saber si el libro se encuentra en el catalogo
        encontrado = False

        #Se verifica si hay libros en prestamo, de lo contrario no tiene caso regresar un libro que no se tiene en estado de prestado
        if len(self.__librosPrestamosUsuarios) == 0:
            
            print("\nNo hay libros en prestamo. Por lo que no hay libros que regresar")
            
            return 
        
        else:
            
            #Se pide el identificador del libro
            idLibro = int(input("\nIngrese el ID del libro: "))
        
            #Se recorre el catalogo de libros en busca del libro para regresarlo
            for libro in self.__catalogoLibros:
                if libro.getIdLibro() == idLibro:
                    #Se cambia el valor de la variable bandera
                    encontrado = True
                    #Se pone que el estado sera disponible
                    estado = "Disponible"
                    #Se cambia el estado del libro a disponible
                    libro.setEstado(estado)
                
                    #Se borra el libro de la lista de libros que estan en prestamo
                    for libroPrestamo in self.__librosPrestamosUsuarios:
                        if libroPrestamo.getIdLibro() == idLibro:
                            self.__librosPrestamosUsuarios.remove(libroPrestamo)
                    
                
        #Mensaje en caso de que el ID del libro que se ingreso no haya sido encontrado        
        if encontrado == False:
            print(f"\nEl libro con id : {idLibro} no fue encontrado en la lista de los libros que estan en prestamos en la biblioteca")
        else:
            print("\nLa devolucion del libro se ha logrado con exito\n")
    