import getpass
import os
import platform

#Declaramos las constantes del programa

adminUser = "admin@ventaspasajes777.com"
adminPassword = "admin"
codNovedad = int(100)
textoNovedad = str("NUEVA MODALIDAD DE TRANSPORTE")
fechaPublicacion = str("05/5/25")
fechaExpiracion = str("18/5/25")
codNovedad1 = int(101)
textoNovedad1 = str("FALLECIO EL PAPA")
fechaPublicacion1 = str("21/4/25")
fechaExpiracion1 = str("7/11/25")
codNovedad2 = int(102)
textoNovedad2 = str("EL GRUPO 6 SE SACO UN 10 EN EL TP :D")
fechaPublicacion2 = str("18/5/25")
fechaExpiracion2 = str("25/5/25")

def limpiar_consola():
    #"""Limpia la consola, adaptándose al sistema operativo."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
        
    
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
    salida = str("X")
    contArg = int(0)
    contChi = int(0)
    contBra = int(0)
    while(salida != "N"):
        codigoPais = str("A")
        salida = str("X")
        nombreAereolinea = str(input("ingrese el nombre de su aereolinea: "))
        codigoIATA = str(input("Ingrese el codigo IATA correspondiente: "))
        descripcionAereolinea = str(input("Ingrese una breve descripción: "))
        while codigoPais != "ARG" and codigoPais != "BRA" and codigoPais !="CHI": #Este while obliga a que el codigo de pais este bien ingresado
            codigoPais = str(input("ingrese el código de país correspondiente: ").upper())
            if codigoPais != "ARG" and codigoPais != "BRA" and codigoPais !="CHI":
                print("codigo no valido")
            
        if codigoPais == "ARG":
            contArg = contArg + 1
                
        elif codigoPais == "CHI":
            contChi = contChi + 1
                
        elif codigoPais == "BRA":
            contBra = contBra + 1
        
        while salida != "N" and salida != "S": #se usa para determinar si se busca agregar aereolineas o no
            salida = str(input("¿Desea seguir agregando aerolineas? S/N ").upper().strip())
            if salida != "N" and salida != "S":
                print("Carácter invalido, reingrese")
    print(f"la cantidad de aereolineas creadas en Argentina son, {contArg}, en Brasil son {contBra}, y en Chile son {contChi}")
#Submenu del gestión de Aerolinea (selección de menu)

def subMenu1():
    opc1 = int(1) #inicializo la variable en 1 para que el usuario ingrese al sistema.
    while (opc1 != 0):
        menu1()
        opc1 = int(input("Ingrese su opción: ")) #pido al usuario la opcion que desea visitar
        while (opc1 < 0 or opc1 > 3) : #si el usuario ingresa un número que no sea valido, se lo pedimos de nuevo
            opc1 = int(input("Ingreso invalido, reintente"))
        match opc1:
            case 1:limpiar_consola(),crearAerolinea()
            case 2:limpiar_consola(), cartel(), subMenu1()
            case 3:cartel(), subMenu1()
            case 0:limpiar_consola(),subMenuMain()
            
   
            
            

#Menu de Gestión de Novedades
def menu3():
    print("\n     ......Gestión de Novedades......")
    print("     1. Crear Novedad")
    print("     2. Modificar Novedad")
    print("     3. Eliminar Novedad")
    print("     4. Ver Novedades")
    print("     0. Volver")
    
def nov():
    global textoNovedad
    global fechaPublicacion
    global fechaExpiracion
    textoNovedad = str(input("Ingrese el texto de la novedad: "))
    fechaPublicacion = input("Ingrese la fecha de publicación: ")
    fechaExpiracion = input("Ingrese la fecha de expiración: ")



def nov1():
    global textoNovedad1 
    global fechaPublicacion1
    global fechaExpiracion1
    textoNovedad1 = str(input("Ingrese el texto de la novedad: "))
    fechaPublicacion1 = input("Ingrese la fecha de publicación: ")
    fechaExpiracion1 = input("Ingrese la fecha de expiración: ")

def nov2():
    global textoNovedad2
    global fechaPublicacion2
    global fechaExpiracion2 
    textoNovedad2 = str(input("Ingrese el texto de la novedad: "))
    fechaPublicacion2 = input("Ingrese la fecha de publicación: ")
    fechaExpiracion2 = input("Ingrese la fecha de expiración: ")



def modificarNovedades():
    salidaNov = str("X")
    while salidaNov != "N":
        codModificar = int(input("ingrese el codigo a modificar (los codigos validos son 100, 101, 102.): "))
        while codModificar < 100 or codModificar > 102:
            codModificar = int(input("El número ingresado es invalido, reintente (los codigos validos son 100, 101, 102.): "))
            
        match codModificar:
            case 100: limpiar_consola(), nov()
            case 101: limpiar_consola(), nov1()
            case 102: limpiar_consola(), nov2()
            
        salidaNov = str(input("¿Desea modificar mas novedades? S/N ").upper().strip())
        while salidaNov != "N" and salidaNov != "S":
            limpiar_consola()
            salidaNov = input("Carácter invalido, reintente (S/N): ")
    
def verNovedades():
    print(f"{codNovedad}, {textoNovedad},Publicado el: {fechaPublicacion},Expira el: {fechaExpiracion}")
    print(f"{codNovedad1}, {textoNovedad1},Publicado el: {fechaPublicacion1},Expira el: {fechaExpiracion1}")
    print(f"{codNovedad2}, {textoNovedad2},Publicado el: {fechaPublicacion2},Expira el: {fechaExpiracion2}")
    

#SubMenu de Gestión de novedades
def subMenu3():
    opc3 = int(1) #inicializo la variable en 1 para que el usuario ingrese al sistema.
    while (opc3 != 0):
        menu3()
        opc3 = int(input("Ingrese su opción: ")) #pido al usuario la opcion que desea visitar
        while (opc3 < 0 or opc3 > 4) : #si el usuario ingresa un número que no sea valido, se lo pedimos de nuevo
            opc3 = int(input("Ingreso invalido, reintente: "))
        match opc3:
            case 1:limpiar_consola(),cartel()
            case 2:limpiar_consola(),modificarNovedades() #editar novedades
            case 3:limpiar_consola(),cartel()
            case 4:limpiar_consola(),verNovedades()    #ver novedades 
            case 0:limpiar_consola(),subMenuMain()

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
    opc = 0
    while (opc == 0):
        menu()
        opc = int(input("Ingrese su opción: "))
    while (opc < 1 or opc > 5):
        opc = int(input("ingreso invalido, reintente"))
    match opc:
        case 1:limpiar_consola(),subMenu1()
        case 2:limpiar_consola(), cartel(), subMenuMain()
        case 3:limpiar_consola(), subMenu3()
        case 4:limpiar_consola(),cartel(), subMenuMain()
        case 5:limpiar_consola()
        #queda vacio ya que si vale 5 se cierra el programa




def sistema():
    print("Bienvenidos al sistema de administración de aerolineas")
    intentos = int(0)
    global opc 
    while opc != 5 and intentos < 3:
        nombreUsuario = input("Ingrese su nombre de usuario: ").strip()
        contrasenaUsuario = getpass.getpass("Ingrese su contraseña: ").strip()
        if nombreUsuario == adminUser and contrasenaUsuario == adminPassword:
            #en este caso se activa el sistema
            limpiar_consola()    
            print("Acceso concedido!")           
            subMenuMain()

                              
        else:
            print("Acceso denegado, intentelo nuevamente")
            intentos = intentos + 1            
    if opc == 5:
        limpiar_consola()
        print("Gracias por usar el sistema!")
        print("El programa ha finalizado correctamente!")
        #se cierra voluntariamente
    else:
        limpiar_consola()
        print("3 intentos fallidos, cerrando el programa.")
        #se cierra por exceso de intentos

sistema()

#Falta hacer
#-acomodar los limpiar_consola
#-len
#-revisar nombres de variables
#
#
#
#