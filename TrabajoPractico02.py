#TRABAJO PRACTICO REALIZADO POR LOS ALUMNOS JOAQUIN DEMARCHI NICASTRO, PABLO NORBERTO PEREZ Y BAUTISTA FERNANDEZ SAINZ DE LA COMISION 106, GRUPO 6


import getpass
import os
import platform
import datetime

#Declaramos las constantes del programa
clave = "0"
adminUser = "admin" #String
adminPassword = "admin" #String
opc = 0
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

#def CargaUsuario():
usuarios =["admin@ventaspasajes777.com","ceo1@ventaspasajes777.com","ceo2@ventaspasajes777.com","ceo3@ventaspasajes777.com","ceo4@ventaspasajes777.com", "ceo5@ventaspasajes777.com","usuario1@ventaspasajes777.com", "usuario2@ventaspasajes777.com","",""]
contrasena = ["admin123","ceo123","ceo456","ceo789","ceo101112","ceo131415","usuario123","usuario456","",""]
tipo =["administrador","ceo","ceo","ceo","ceo","ceo","usuario","usuario","usuario","usuario"]
array = [usuarios, contrasena, tipo]


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
        


#menu gestion de vuelos ceo
def gestionVuelos():
    print("\n     ......Gestión de Vuelos......")
    print("     1. Crear Vuelo")
    print("     2. Modificar Vuelo")
    print("     3. Eliminar Vuelo")
    print("     0. Volver") 

#menu gestion de promociones ceo
def gestionPromociones():
    print("\n     ......Gestión de Promociones......")
    print("     1. Crear Promoción")
    print("     2. Modificar Promoción")
    print("     3. Eliminar Promoción")
    print("     0. Volver")
    
#menu gestion de reportes ceo
def gestionReportes():
    print("\n     ......Gestión de Reportes......")
    print("     1. Reporte de Ventas de mi Aerolínea")
    print("     2. Reporte de ocupación de Vuelos de mi Aerolínea ")
    print("     0. Volver")
    
#menu ceo  
def menuCeo():
    print("\n......Menu Principal CEO......")
    print("1. Gestión de Vuelos")
    print("2. Gestion de Promociones")
    print("3. Gestión de Reportes")
    print("4. Cerrar sesion")

#Menu de usuario
def menuUsuario():
    print("\n......Menu Principal......")
    print("1. Buscar Vuelos")
    print("2. Buscar Asientos")
    print("3. Reservar Vueloss")
    print("4. Reservas")
    print("5. Ver Historial de Compras")
    print("6. Ver Novedades")
    print("7. Cerrar Sesión")
#en construccion

#def BuscarVuelos():

    

    

#Menu principal
def printMenuAdministrador():
    print("\n......MENU PRINCIPAL......")
    print("1. Gestión de Aerolíneas")
    print("2. Aprobar/Denegar Promociones")
    print("3. Gestión de Novedades")
    print("4. Reportes")#
    print("5. Salir")

#Menu de Gestión de Aerolíneas
            
def gestionAerolinea():
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
            codigoPais = str(input("ingrese el código de país correspondiente (ARG, CHI, BRA) ").upper())
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

def subMenuGestionAereolineas (opc):
    global opc1
    opc1 = int(1) #inicializo la variable en 1 para que el usuario ingrese al sistema.
    while (opc1 != 0):
        gestionAerolinea()
        opc1 = int(input("Ingrese su opción: ")) #pido al usuario la opcion que desea visitar
        while (opc1 < 0 or opc1 > 3) : #si el usuario ingresa un número que no sea valido, se lo pedimos de nuevo
            opc1 = int(input("Ingreso invalido, reintente"))
        match opc1:
            case 1:limpiarConsola(),crearAerolinea()
            case 2:limpiarConsola(), cartel(), subMenuGestionAereolineas(opc)
            case 3:cartel(), subMenuGestionAereolineas(opc)
            case 0:limpiarConsola(),menuAdministrador(opc)
            
    

            

#Menu de Gestión de Novedades

def printGestionNovedades():
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
        codModificar = (input("ingrese el codigo a modificar (los codigos validos son 100, 101, 102.): "))
        while codModificar != 100 or codModificar != 101 or codModificar != 102:
            codModificar = (input("El número ingresado es invalido, reintente (los codigos validos son 100, 101, 102.): "))
            
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
def gestionNovedades():
    opc3 = int(1) #inicializo la variable en 1 para que el usuario ingrese al sistema.
    while (opc3 != 0):
        printGestionNovedades()
        opc3 = int(input("Ingrese su opción: ")) #pido al usuario la opcion que desea visitar
        while (opc3 < 0 or opc3 > 4) : #si el usuario ingresa un número que no sea valido, se lo pedimos de nuevo
            opc3 = int(input("Ingreso invalido, reintente: "))
        match opc3:
            case 1:limpiarConsola(),cartel()
            case 2:limpiarConsola(),modificarNovedades() #editar novedades
            case 3:limpiarConsola(),cartel()
            case 4:limpiarConsola(),verNovedades()    #ver novedades 
            case 0:limpiarConsola(),menuAdministrador(opc)

#Menu de Reportes
def printReportes():
    print("\n     ......Reportes......")
    print("     1. Reporte de ventas")
    print("     2. Reporte de vuelos")
    print("     3. Reporte de usuarios")
    print("     0. Volver")

#cartel de apartado en construcción
def cartel():
    mensaje = " EN CONSTRUCCIÓN... "
    borde = "+" + "-" * (len(mensaje) + 2) + "+"
    cuerpo = "| " + mensaje + " |"
    
    print("\033[93m")  # Cambia el color a amarillo (código ANSI)
    print(borde)
    print(cuerpo)
    print(borde)
    print("\033[0m")   # Resetea el color

def menuAdministrador(opc):
    opc = 0
    while (opc == 0):
        printMenuAdministrador()
        opc = int(input("Ingrese su opción: "))
    while (opc < 1 or opc > 5):
        opc = int(input("ingreso invalido, reintente"))
    match opc:
        case 1:limpiarConsola(),subMenuGestionAereolineas(opc)
        case 2:limpiarConsola(), cartel(), menuAdministrador(opc)
        case 3:limpiarConsola(), gestionNovedades()
        case 4:limpiarConsola(),cartel(), menuAdministrador(opc)
        case 5:limpiarConsola()
        #queda vacio ya que si vale 5 se cierra el programa
        

   
def subMenuCeo(opc):
    opc = int(1)
    while opc != 4:
        menuCeo()
        opc = int(input("ingrese su opción: "))
        while opc < 0 or opc > 4:
            opc = int(input("ingreso invalido, reingrese: "))
        match opc:
            case 1: limpiarConsola(), gestionVuelos()
            case 2: limpiarConsola(), cartel(),subMenuCeo(opc)
            case 3: limpiarConsola(),cartel(),subMenuCeo(opc)
            case 4: limpiarConsola()
    


def inicioSesion(opc):
    intentos = int(0)
    salida = True
    while salida == True and intentos < 3:
        nombreUsuario = input("Ingrese su nombre de usuario: ").strip()
        comprobacionLen(nombreUsuario,100)
        flagNombre= False
        i= 0
        while flagNombre == False and i!= 10:
            if array[0][i] == nombreUsuario:
                flagNombre = True
            else:
                i += 1
        contrasenaUsuario = getpass.getpass("Ingrese su contraseña: ").strip()
        comprobacionLen(contrasenaUsuario,8)
        flagContra= False
        i= 0
        while flagContra == False and i!= 10:
            if array[1][i] == contrasenaUsuario:
                flagContra = True
            else:
                i += 1        
        if flagContra == True and flagNombre == True :
            #en este caso se activa el sistema
            match array[2][i]:
                case "administrador":
                    limpiarConsola()
                    print("Acceso concedido!")
                    menuAdministrador(opc)
                    salida = False
                case "ceo":
                    limpiarConsola()
                    print("Acceso concedido!")
                    subMenuCeo(opc)
                    salida = False
                case "usuario":
                    limpiarConsola()
                    print("Acceso concedido!")
                    menuUsuario(opc)
                    salida = False
        else:
            print("Acceso denegado, intentelo nuevamente")
            intentos = intentos + 1            

    if intentos == 3:
        limpiarConsola()
        print("3 intentos fallidos, cerrando el programa.")
        #se cierra por exceso de intentos
    else:
        limpiarConsola()
        print("Gracias por usar el sistema!")
        print("El programa ha finalizado correctamente!")
        #se cierra voluntariamente
    

def registro(opc):
    cont = 0
    if usuarios[8] == "":
        usuarios[8] = input("Ingrese su nombre de usuario: ").strip()
        cont = 8
    elif usuarios[9] == "":
        usuarios[9] = input("Ingrese su nombre de usuario: ").strip()
        cont = 9
    else:
        print("No se pueden registrar más usuarios, el sistema está lleno.")
        
    comprobacionLen(usuarios[cont],100)
    contrasena[cont] = getpass.getpass("Ingrese su contraseña: ").strip()
    print("Registro exitoso!")
    limpiarConsola()
    inicioSesion(opc)
    
def sistema(opc, clave):
    print("Bienvenidos al sistema de administración de aerolineas")
    clave = input("¿Desea iniciar sesion o registrarse? (1 para incio de sesión / 2 para registrarse: )")
    while clave != "1" and clave != "2":
        clave = input("¿Desea iniciar sesion o registrarse? (1 para incio de sesión / 2 para registrarse: )")
        if clave != "1" and clave != "2":
            print("codigo invalido, reintente")
            
    if clave == "1":
        inicioSesion(opc)
    else:
        registro(opc)
    
    

sistema(opc, clave)
