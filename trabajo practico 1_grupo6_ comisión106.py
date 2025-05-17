#TRABAJO PRACTICO REALIZADO POR LOS ALUMNOS JOAQUIN DEMARCHI NICASTRO Y BAUTISTA FERNANDEZ SAINZ DE LA COMISION 106, GRUPO 6


import getpass
import os
import platform
import datetime

#Declaramos las constantes del programa

adminUser = "admin@ventaspasajes777.com" #String
adminPassword = "admin" #String

codNovedad = int(100)  #Entero
textoNovedad = str("NUEVA MODALIDAD DE TRANSPORTE") #String
fechaPublicacion = str("2025/05/05") #String
fechaExpiracion = str("2025/05/18") #String
codNovedad1 = int(101) #Entero
textoNovedad1 = str("texto novedad 1") #String
fechaPublicacion1 = str("2025/04/21") #String
fechaExpiracion1 = str("2025/11/07") #String
codNovedad2 = int(102) #Entero
textoNovedad2 = str("texto novedad 2") #String
fechaPublicacion2 = str("2025/05/18") #String
fechaExpiracion2 = str("2025/05/25") #String


def comprobacionFecha(fecha_str):
    try:
        datetime.datetime.strptime(fecha_str, "%Y/%m/%d")
        return True
    except ValueError:
        return False
    
def pedirFecha(mensaje):
    fecha_valida = False
    fecha = ""
    while not fecha_valida:
        fecha = input(mensaje)
        if comprobacionFecha(fecha):
            fecha_valida = True
        else:
            print("Fecha inválida. Debe tener formato yyyy/mm/dd y ser una fecha posible.")
    return fecha



def comprobacionLen(a,b):
    while len(a) > b or len(a) == 0:
        if len(a) > b :
            a = input(f"la cantidad maxima de caracteres es {b}, por favor reintente: ")
        elif len(a) == 0 :
            a = input("el espacio no puede estar vacío, por favor reintente: ")
            

    
#Limpia la consola, adaptándose al sistema operativo.
def limpiarConsola():
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
    may = 0
    aux = 0
    min = 0
    aux1 = 1000000
    salida = str("X") #character para que el while funcione
    contArg = int(0)
    contChi = int(0)
    contBra = int(0)
    while(salida != "N"):
        codigoPais = str("A")
        salida = str("X")
        nombreAereolinea = str(input("ingrese el nombre de su aereolinea: "))
        comprobacionLen(nombreAereolinea,100)
        codigoIATA = str(input("Ingrese el codigo IATA correspondiente: "))
        comprobacionLen(codigoIATA,3)
        descripcionAereolinea = str(input("Ingrese una breve descripción: "))
        comprobacionLen(descripcionAereolinea,200)
        while not (codigoPais == "ARG" or codigoPais == "BRA" or codigoPais == "CHI"): #Este while obliga a que el codigo de pais este bien ingresado
            codigoPais = str(input("ingrese el código de país correspondiente: ").upper())
            comprobacionLen(codigoPais,3)
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
                
        if aux < contArg:
            aux = contArg
            may = "Argentina"
                
        elif aux < contChi:
            aux = contChi
            may = "Chile"
                
        elif aux < contBra:
            aux = contBra
            may = "Brasil"
            
    if aux1 > contChi:
        aux1 = contChi
        min = "Chile"
                
    if aux1 > contArg:
        aux1 = contArg
        min = "Argentina"
                
    if aux1 > contBra:
        aux1 = contBra
        min = "Brasil"
                
    print(f"la cantidad de aereolineas creadas en Argentina son, {contArg}, en Brasil son {contBra}, y en Chile son {contChi}")
    print(f"el pais con mas aereolineas es {may}, con {aux} aereolineas, mientras el que menos es {min}, con {aux1} aereolineas")
    input("ingrese algo para continuar")
    limpiarConsola()
#Submenu del gestión de Aerolinea (selección de menu)

def subMenu1():
    global opc1
    opc1 = int(1) #inicializo la variable en 1 para que el usuario ingrese al sistema.
    while (opc1 != 0):
        menu1()
        opc1 = int(input("Ingrese su opción: ")) #pido al usuario la opcion que desea visitar
        while (opc1 < 0 or opc1 > 3) : #si el usuario ingresa un número que no sea valido, se lo pedimos de nuevo
            opc1 = int(input("Ingreso invalido, reintente"))
        match opc1:
            case 1:limpiarConsola(),crearAerolinea()
            case 2:limpiarConsola(), cartel(), subMenu1()
            case 3:cartel(), subMenu1()
            case 0:limpiarConsola(),subMenuMain()
            
   
            
            

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
    comprobacionLen(textoNovedad,200)
    fechaPublicacion = pedirFecha("ingrese la fecha de publicación(formato YYYY/MM/DD): ")
    comprobacionLen(fechaPublicacion,10)
    fechaExpiracion = pedirFecha("ingrese la fecha de expiración(formato YYYY/MM/DD): ")
    comprobacionLen(fechaExpiracion,10)



def nov1():
    global textoNovedad1 
    global fechaPublicacion1
    global fechaExpiracion1
    textoNovedad1 = str(input("Ingrese el texto de la novedad: "))
    comprobacionLen(textoNovedad1,200)
    fechaPublicacion1 = pedirFecha("ingrese la fecha de publicación(formato YYYY/MM/DD): ")
    comprobacionLen(fechaPublicacion1,10)
    fechaExpiracion1 = pedirFecha("ingrese la fecha de expiración(formato YYYY/MM/DD): ")
    comprobacionLen(fechaExpiracion1,10)

def nov2():
    global textoNovedad2
    global fechaPublicacion2
    global fechaExpiracion2 
    textoNovedad2 = str(input("Ingrese el texto de la novedad: "))  
    comprobacionLen(textoNovedad2,200)
    fechaPublicacion2 = pedirFecha("ingrese la fecha de publicación(formato YYYY/MM/DD): ")
    comprobacionLen(fechaPublicacion2,10)
    fechaExpiracion2 = pedirFecha("ingrese la fecha de expiración(formato YYYY/MM/DD): ")
    comprobacionLen(fechaExpiracion2,10)



def modificarNovedades():
    salidaNov = str("X")
    while salidaNov != "N":
        codModificar = int(input("ingrese el codigo a modificar (los codigos validos son 100, 101, 102.): "))
        while codModificar < 100 or codModificar > 102:
            codModificar = int(input("El número ingresado es invalido, reintente (los codigos validos son 100, 101, 102.): "))
            
        match codModificar:
            case 100: limpiarConsola(), nov()
            case 101: limpiarConsola(), nov1()
            case 102: limpiarConsola(), nov2()
            
        salidaNov = str(input("¿Desea modificar mas novedades? S/N ").upper().strip())
        while salidaNov != "N" and salidaNov != "S":
            limpiarConsola()
            salidaNov = input("Carácter invalido, reintente (S/N): ")
    
def verNovedades():
    print(f"   |{codNovedad},|{textoNovedad},  |Publicado el: {fechaPublicacion},  |Expira el: {fechaExpiracion}   |")
    print(f"   |{codNovedad1},|{textoNovedad1}, |Publicado el: {fechaPublicacion1}, |Expira el: {fechaExpiracion1}  |")
    print(f"   |{codNovedad2},|{textoNovedad2}, |Publicado el: {fechaPublicacion2}, |Expira el: {fechaExpiracion2}  |")
    input("ingrese cualquier cosa para continuar")
    limpiarConsola()
    

#SubMenu de Gestión de novedades
def subMenu3():
    opc3 = int(1) #inicializo la variable en 1 para que el usuario ingrese al sistema.
    while (opc3 != 0):
        menu3()
        opc3 = int(input("Ingrese su opción: ")) #pido al usuario la opcion que desea visitar
        while (opc3 < 0 or opc3 > 4) : #si el usuario ingresa un número que no sea valido, se lo pedimos de nuevo
            opc3 = int(input("Ingreso invalido, reintente: "))
        match opc3:
            case 1:limpiarConsola(),cartel()
            case 2:limpiarConsola(),modificarNovedades() #editar novedades
            case 3:limpiarConsola(),cartel()
            case 4:limpiarConsola(),verNovedades()    #ver novedades 
            case 0:limpiarConsola(),subMenuMain()

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
        case 1:limpiarConsola(),subMenu1()
        case 2:limpiarConsola(), cartel(), subMenuMain()
        case 3:limpiarConsola(), subMenu3()
        case 4:limpiarConsola(),cartel(), subMenuMain()
        case 5:limpiarConsola()
        #queda vacio ya que si vale 5 se cierra el programa




def sistema():
    print("Bienvenidos al sistema de administración de aerolineas")
    intentos = int(0)
    global opc 
    while opc != 5 and intentos < 3:
        nombreUsuario = input("Ingrese su nombre de usuario: ").strip()
        comprobacionLen(nombreUsuario,100)
        contrasenaUsuario = getpass.getpass("Ingrese su contraseña: ").strip()
        comprobacionLen(contrasenaUsuario,8)
        if nombreUsuario == adminUser and contrasenaUsuario == adminPassword:
            #en este caso se activa el sistema
            limpiarConsola()    
            print("Acceso concedido!")           
            subMenuMain()

                              
        else:
            print("Acceso denegado, intentelo nuevamente")
            intentos = intentos + 1            
    if opc == 5:
        limpiarConsola()
        print("Gracias por usar el sistema!")
        print("El programa ha finalizado correctamente!")
        #se cierra voluntariamente
    else:
        limpiarConsola()
        print("3 intentos fallidos, cerrando el programa.")
        #se cierra por exceso de intentos

sistema()

#Falta hacer
#-revisar nombres de variables
#-identificar tipos de variables en comentario
#
#