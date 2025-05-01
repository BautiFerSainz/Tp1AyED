import getpass

#Declaramos las constantes del programa

adminUser = "admin@ventaspasajes777.com"
adminPassword = "admin"



    
#Menu principal
def menu():
    print("\n......MENU PRINCIPAL......")
    print("1. Gestión de Aerolíneas")
    print("2. Aprobar/Denegar Promociones")
    print("3. Gestión de Novedades")
    print("4. Reportes")#
    print("5. Salir")

#Menu de Gestión de Aerolíneas
            
def menu1():
    print("\n     ......Gestión Aereolinea......")
    print("     1. Crear Aereolinea")
    print("     2. Modificar Aereolinea")
    print("     3. Eliminar aereolinea")
    print("     0. Volver")

#Submenu de creación de Aerolinea

def crearAerolinea():
    salida = chr("X")
    contArg = 0
    contChi = 0
    contBra = 0
    while(salida != "N"):
        nombreAereolinea = str(input(100)("ingrese el nombre de su aereolinea: "))
        codigoIATA = str(input(3)("Ingrese el codigo IATA correspondiente: "))
        descripcionAereolinea = str(input(200)("Ingrese una breve descripción: "))
        codigoPais = str(input()("ingrese el código de país correspondiente: "))
        while salida != "N" or salida != "S": #se usa para determinar si se busca agregar aereolineas o no
            salida = chr(input("¿Desea terminar de agregar aerolineas? S/N").upper().strip())
            if salida != "N" and salida != "S":
                print("Carácter invalido, reingrese")

#Submenu del gestión de Aerolinea (selección de menu)

def subMenu1():
    opc1 = int(1) #inicializo la variable en 1 para que el usuario ingrese al sistema.
    while (opc1 != 0):
        menu1()
        opc1 = int(input("Ingrese su opción: "))#pido al usuario la opcion que desea visitar
        while (opc1 < 0 or opc1 > 3) : #si el usuario ingresa un número que no sea valido, se lo pedimos de nuevo
            opc1 = int(input("Ingreso invalido, reintente"))
        match opc1:
            case 1:crearAerolinea()
            case 2:cartel(), subMenu1()
            case 3:cartel(), subMenu1()
            case 0:subMenuMain()
            
   
            
            

#Menu de Gestión de Novedades
def menu3():
    print("\n     ......Gestión de Novedades......")
    print("     1. Crear Novedad")
    print("     2. Modificar Novedad")
    print("     3. Eliminar Novedad")
    print("     4. Ver Novedades")
    print("     0. Volver")

#Menu de Reportes
def menu4():
    print("\n     ......Reportes......")
    print("     1. Reporte de ventas")
    print("     2. Reporte de vuelos")
    print("     3. Reporte de usuarios")
    print("     0. Volver")

#cartel de apartado en construcción
def cartel():
    print("En construcción, vuelva pronto!")

opc = 0
def subMenuMain():
    global opc
    while (opc == 0):
        menu()
        opc = int(input("Ingrese su opción: "))
    while (opc < 1 or opc > 5):
        opc = int(input("ingreso invalido, reintente"))
    match opc:
        case 1:subMenu1()
        case 2:cartel(), subMenuMain()
        case 3:menu3()
        case 4:cartel(), subMenuMain()
        case 5:
            print("Gracias por usar el sistema!")




def sistema():
    print("Bienvenidos al sistema de administración de aerolineas")
    intentos = int(0)
    global opc 
    while opc != 5 and intentos < 3:
        nombreUsuario = input("Ingrese su nombre de usuario: ").strip()
        contrasenaUsuario = getpass.getpass("Ingrese su contraseña: ").strip()
        if nombreUsuario == adminUser and contrasenaUsuario == adminPassword:
            #en este caso se activa el sistema
            print("Acceso concedido!")
            subMenuMain()
                              
        else:
            print("Acceso denegado, intentelo nuevamente")
            intentos = intentos + 1
                
    if opc == 5:
        print("El programa ha finalizado correctamente!")
        #se cierra voluntariamente
    else:
        print("3 intentos fallidos, cerrando el programa.")
        #se cierra por exceso de intentos

sistema()

#Falta hacer
#-Mostrar que codigo de pais tiene mas aerolineas y cual tiene menos.
#-Opción editar novedades
#-Opción mostrar novedades
#-Requerimiento nro 2
#
#
#
#
#
#
#
#