#TRABAJO PRACTICO REALIZADO POR LOS ALUMNOS JOAQUIN DEMARCHI NICASTRO, PABLO NORBERTO PEREZ Y BAUTISTA FERNANDEZ SAINZ DE LA COMISION 106, GRUPO 6


import getpass
import os
import platform
import datetime

#Declaramos las constantes del programa
clave = "0"
opc = 0
opc2 = 0
contArray = 0
codModificar = 0
usuarios = []*10
contrasena = []*10
tipo = []*10
datos = []*3
codNovedad =[]*3
textoNovedad =[]*3
fechaPublicacion =[]*3
fechaExpiracion =[]*3
novedades =[]*4
precioVuelos = []*20
precioVuelos = ["$1.101.150", "$550.000", "$800.220", "$670.000", "$1.670.000", "$1.250.000","$430.000", "$710.100", "$980.000", "$1.320.000", "","","","","","","","","",""]
vuelos= [[""]*6 for i in range(20)] #creamos una lista de listas, donde cada sublista representa un vuelo
#definimos algunos vuelos precargados
vuelos = [
    ["1","Aerolíneas Arg", "Buenos Aires", "Madrid", "15/07/2025", "08:30"],
    ["2","LATAM", "Santiago", "Lima", "16/07/2025", "10:15"],
    ["3","Sky Airline", "Miami", "Nueva York", "18/08/2025", "14:45"],
    ["4","GOL", "Río Janeiro", "Buenos Aires", "20/08/2025", "22:30"],
    ["5","LATAM", "Lima", "Nueva York", "22/08/2025", "20:30"],
    ["6","Aerolíneas Arg", "Córdoba", "Barcelona", "25/08/2025", "09:15"],
    ["7","LATAM", "Montevideo", "Santiago", "26/08/2025", "06:00"],
    ["8","Sky Airline", "Buenos Aires", "San Pablo", "28/08/2025", "13:20"],
    ["9","GOL", "San Pablo", "Quito", "29/08/2025", "15:00"],
    ["10","Aerolíneas Arg", "Buenos Aires", "Roma", "30/08/2025", "19:45"],
    ["","","","","",""],
    ["","","","","",""],
    ["","","","","",""],
    ["","","","","",""],
    ["","","","","",""],
    ["","","","","",""],
    ["","","","","",""],
    ["","","","","",""],
    ["","","","","",""],
    ["","","","","",""],
]

#def CargaUsuario():
usuarios =["admin@ventaspasajes777.com","ceo1@ventaspasajes777.com","ceo2@ventaspasajes777.com","ceo3@ventaspasajes777.com","ceo4@ventaspasajes777.com", "ceo5@ventaspasajes777.com","usuario1@ventaspasajes777.com", "usuario2@ventaspasajes777.com","",""]
contrasena = ["admin123","ceo123","ceo456","ceo789","ceo101112","ceo131415","usuario123","usuario456","",""]
tipo =["administrador","ceo","ceo","ceo","ceo","ceo","usuario","usuario","usuario","usuario"]
datos = [usuarios, contrasena, tipo]

codNovedad = ["100","101","102"]
textoNovedad = ["NUEVA MODALIDAD DE TRANSPORTE", "NUEVO PAPA AMERICANO", "BAJA EN LOS IMPUESTOS MUNICIPALES"]
fechaPublicacion = ["2025/05/05","2025/05/05","2025/05/05"]
fechaExpiracion = ["2025/05/05","2025/05/05","2025/05/05"]
novedades = [codNovedad,textoNovedad,fechaPublicacion,fechaExpiracion]


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
    print("     4. Volver") 

#menu gestion de promociones ceo
def gestionPromociones():
    print("\n     ......Gestión de Promociones......")
    print("     1. Crear Promoción")
    print("     2. Modificar Promoción")
    print("     3. Eliminar Promoción")
    print("     4. Volver")
    
#menu gestion de reportes ceo
def gestionReportes():
    print("\n     ......Gestión de Reportes......")
    print("     1. Reporte de Ventas de mi Aerolínea")
    print("     2. Reporte de ocupación de Vuelos de mi Aerolínea ")
    print("     3. Volver")
    
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
def subMenuUsuario(opc):
    opc = int(1)
    while opc != 7:
        menuUsuario()
        opc = int(input("ingrese su opción: "))
        while opc < 0 or opc > 7 :
            opc = int(input("ingreso invalido, reingrese: "))
        match opc:
            case 1: limpiarConsola(),buscarVuelos()
            case 2: limpiarConsola(),cartel()
            case 3: limpiarConsola(),cartel()
            case 4: limpiarConsola(),cartel()
            case 5: limpiarConsola(),cartel()
            case 6: limpiarConsola(),cartel() 
            case 7: limpiarConsola()

def buscarVuelos():
        # Datos de vuelos

    
    # Encabezados
    headers = ["CÓDIGO", "AEROLÍNEA", "ORIGEN", "DESTINO", "FECHA", "HORA", "PRECIO"]

    # Anchos de columnas (ajustados manualmente para que se vea prolijo)
    column_widths = [6, 15, 15, 15, 12, 8, 12]

    # Función para formatear una fila
    def format_row(row, widths):
        return " | ".join(str(item).ljust(width) for item, width in zip(row, widths))

    # Línea separadora
    def separator(widths):
        return "-+-".join("-" * w for w in widths)

    # Imprimir encabezado
    print("LISTADO DE VUELOS DISPONIBLES EN EL SISTEMA\n")
    print(format_row(headers, column_widths))
    print(separator(column_widths))

    # Imprimir filas
    for vuelo in vuelos:
        print(format_row(vuelo, column_widths))

    print("\nTotal de vuelos:", len(vuelos))

    

    

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
    
def nov(novedades, codModificar):
    i = 0
    flag = False
    while i != 3 and flag == False:
        if novedades[0][i] == codModificar:
            novedades [1][i] = input("ingrese el texto de la novedad: ")
            comprobacionLen(novedades[1][i],200)
            novedades [2][i] = pedirFecha("ingrese la fecha de publicación de la novedad")
            novedades [3][i] = pedirFecha("ingrese la fecha de expiración")
            flag =True



def modificarNovedades(novedades):
    salidaNov = str("X")
    while salidaNov != "N":
        codModificar = (input("ingrese el codigo a modificar (los codigos validos son 100, 101, 102.): "))
        while codModificar != "100" and codModificar != "101" and codModificar != "102":
            codModificar = (input("El número ingresado es invalido, reintente (los codigos validos son 100, 101, 102.): "))
        
        limpiarConsola()
        nov(novedades,codModificar)
                
        salidaNov = str(input("¿Desea modificar mas novedades? S/N ").upper().strip())
        while salidaNov != "N" and salidaNov != "S":
            limpiarConsola()
            salidaNov = input("Carácter invalido, reintente (S/N): ")
    
def verNovedades(novedades):
    print(f"   |{novedades[0][0]},|{novedades[1][0]},  |Publicado el: {novedades[2][0]},  |Expira el: {novedades[3][0]}   |")
    print(f"   |{novedades[0][1]},|{novedades[1][1]},  |Publicado el: {novedades[2][1]},  |Expira el: {novedades[3][1]}   |")
    print(f"   |{novedades[0][2]},|{novedades[1][2]},  |Publicado el: {novedades[2][2]},  |Expira el: {novedades[3][2]}   |")
    input("ingrese cualquier cosa para continuar")
    limpiarConsola()
    

#SubMenu de Gestión de novedades
def gestionNovedades(novedades):
    opc3 = int(1) #inicializo la variable en 1 para que el usuario ingrese al sistema.
    while (opc3 != 0):
        printGestionNovedades()
        opc3 = int(input("Ingrese su opción: ")) #pido al usuario la opcion que desea visitar
        while (opc3 < 0 or opc3 > 4) : #si el usuario ingresa un número que no sea valido, se lo pedimos de nuevo
            opc3 = int(input("Ingreso invalido, reintente: "))
        match opc3:
            case 1:limpiarConsola(),cartel()
            case 2:limpiarConsola(),modificarNovedades(novedades) #editar novedades
            case 3:limpiarConsola(),cartel()
            case 4:limpiarConsola(),verNovedades(novedades)    #ver novedades 
            case 0:limpiarConsola(),menuAdministrador(opc,novedades)

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

def menuAdministrador(opc,novedades):
    opc = 0
    while (opc == 0):
        printMenuAdministrador()
        opc = int(input("Ingrese su opción: "))
    while (opc < 1 or opc > 5):
        opc = int(input("ingreso invalido, reintente"))
    match opc:
        case 1:limpiarConsola(),subMenuGestionAereolineas(opc)
        case 2:limpiarConsola(), cartel(), menuAdministrador(opc,novedades)
        case 3:limpiarConsola(), gestionNovedades(novedades)
        case 4:limpiarConsola(),cartel(), menuAdministrador(opc,novedades)
        case 5:limpiarConsola()
        #queda vacio ya que si vale 5 se cierra el programa
        
def busquedaVuelos(contArray,vuelos):
    flag = False
    i = 0
    while flag == False:
        while i != contArray - 1:
            while vuelos[i][0] == vuelos[contArray][0]:
                vuelos[contArray][0] = input("Codigo ya usado, intente con uno nuevo: ")
                flag = True
            i += 1
        if flag == True:
            flag = False
        else:
            flag = True
        
        


def crearvuelo(vuelos,precioVuelos):
    contArray = 0
    while contArray < len(vuelos) and vuelos[contArray][0] != "":
        contArray += 1
    flag1 = True
    rta = ""
    rta = input("Desea ver los vuelos ya cargados? S/N").upper().strip()
    while rta != "S" and rta != "N":
        rta = input("Ingreso invalido, reingrese su respuesta S/N").upper().strip()
    if rta == "S":
        buscarVuelos()
    while contArray < 20 and flag1 == True:
            flag1 == True
            vuelos[contArray][0] = input("Ingrese el  código de la aerolínea: ")
            busquedaVuelos(contArray,vuelos)
            vuelos[contArray][1] = input("Ingrese el  nombre de su aerolinea: ")
            vuelos[contArray][2] = input("Ingrese origen del vuelo: ")
            vuelos[contArray][3] = input("Ingrese destino del vuelo: ")
            vuelos[contArray][4] = pedirFecha("ingrese la fecha:")
            vuelos[contArray][5] = input("Ingrese hora de salida: ")
            precioVuelos[contArray]= input("Ingrese el precio de su vuelo: ")
            salida = input("¿Desea cargar más vuelos? S/N: ").upper().strip()
            while salida != "N" and salida != "S":
                salida = input("ingreso no valido, ingrese S para si, N para no: ").upper().strip()
            if salida == "N":
                flag1 = False
    if contArray == 20:
        print("Se alcanzo el limite de vuelos creados.")








def menugestionVuelos(opc2):
    opc2 = int(1)
    while opc2 != 4:
        gestionVuelos()
        opc2 = int(input("Ingrese una opción: "))
        while opc2 < 0 or opc2 > 4:
            opc2 = int(input("ingreso invalido, reingrese: "))
        match opc2:
            case 1: limpiarConsola(), crearvuelo(vuelos,precioVuelos)
            case 2: limpiarConsola(), #modificarvuelo()
            case 3: limpiarConsola(), #eliminarvuelo()
            case 4: limpiarConsola()


def subMenuCeo(opc, opc2):
    opc = int(1)
    while opc != 4:
        menuCeo()
        opc = int(input("ingrese su opción: "))
        while opc < 0 or opc > 4:
            opc = int(input("ingreso invalido, reingrese: "))
        match opc:
            case 1: limpiarConsola(), menugestionVuelos(opc2)
            case 2: limpiarConsola(), cartel(),subMenuCeo(opc)
            case 3: limpiarConsola(),cartel(),subMenuCeo(opc)
            case 4: limpiarConsola()
    

def inicioSesion(opc, opc2):
    intentos = int(0)
    salida = "S"
    while salida == "S" and intentos < 3:
        nombreUsuario = input("Ingrese su nombre de usuario: ").strip()
        comprobacionLen(nombreUsuario,100)
        flagNombre= False
        i= 0
        while flagNombre == False and i!= 10:
            if datos[0][i] == nombreUsuario:
                flagNombre = True
            else:
                i += 1
        contrasenaUsuario = getpass.getpass("Ingrese su contraseña: ").strip()
        comprobacionLen(contrasenaUsuario,15)
        flagContra= False
        i= 0
        while flagContra == False and i!= 10:
            if datos[1][i] == contrasenaUsuario:
                flagContra = True
            else:
                i += 1        
        if flagContra == True and flagNombre == True :
            #en este caso se activa el sistema
            match datos[2][i]:
                case "administrador":
                    limpiarConsola()
                    print("Acceso concedido!")
                    menuAdministrador(opc,novedades)
                    
                case "ceo":
                    limpiarConsola()
                    print("Acceso concedido!")
                    subMenuCeo(opc, opc2)
                    
                case "usuario":
                    limpiarConsola()
                    print("Acceso concedido!")
                    subMenuUsuario(opc)
                    
                
            salida = input("desea seguir con el programa? S/N: ").upper()
            comprobacionLen(salida, 1)
            while salida != "N" and salida != "S":
                salida = input("caracter no valido, reintente (S/N): ")
                comprobacionLen(salida,1)
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
    if datos[0][8] == "":
        datos[0][8] = input("Ingrese su nombre de usuario: ").strip()
        cont = 8
    elif datos[0][9] == "":
        datos[0][9] = input("Ingrese su nombre de usuario: ").strip()
        cont = 9
    else:
        print("No se pueden registrar más usuarios, el sistema está lleno.")
        
    comprobacionLen(datos[0][cont],100)
    datos[1][cont] = getpass.getpass("Ingrese su contraseña: ").strip()
    comprobacionLen(datos[1][cont],15)
    print("Registro exitoso!")
    limpiarConsola()
    inicioSesion(opc)
    
def sistema(opc, clave, opc2):
    print("Bienvenidos al sistema de administración de aerolineas")
    clave = input("¿Desea iniciar sesion o registrarse? (1 para incio de sesión / 2 para registrarse: )")
    while clave != "1" and clave != "2":
        clave = input("¿Desea iniciar sesion o registrarse? (1 para incio de sesión / 2 para registrarse: )")
        if clave != "1" and clave != "2":
            print("codigo invalido, reintente")
            
    if clave == "1":
        inicioSesion(opc, opc2)
    else:
        registro(opc)
    
    

sistema(opc, clave, opc2)
