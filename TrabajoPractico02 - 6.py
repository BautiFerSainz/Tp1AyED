#TRABAJO PRACTICO REALIZADO POR LOS ALUMNOS JOAQUIN DEMARCHI NICASTRO, PABLO NORBERTO PEREZ, GUIDO MONTANA Y BAUTISTA FERNANDEZ SAINZ DE LA COMISION 106, GRUPO 3

import getpass
import os
import platform
import datetime
import random

#Declaramos las constantes del programa
clave = "0"
opc = 0
opc2 = 0
contArray = 0
codModificar = 0
vuelos = [[""]*5 for i in range (20)]
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
precioVuelos = [1101150.0, 550000.0, 800220.0, 670000.0, 1670000.0, 1250000.0,430000.0, 710100.0, 980000.0 , 1320000.0, 0.0, 0.0,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ,0.0 ]
vuelos= [[""]*6 for i in range(20)] #creamos una lista de listas, donde cada sublista representa un vuelo
#definimos algunos vuelos precargados
vuelos = [
    ["1","Aerolíneas Arg", "Buenos Aires", "Madrid", "2025/07/15", "08:30","A"],
    ["2","LATAM", "Santiago", "Lima", "2025/07/16", "10:15","A"],
    ["3","Sky Airline", "Miami", "Nueva York", "2025/08/18", "14:45","A"],
    ["4","LATAM", "Río Janeiro", "Buenos Aires", "2025/08/20", "22:30","A"],
    ["5","LATAM", "Lima", "Nueva York", "2025/08/22", "20:30","A"],
    ["6","Aerolíneas Arg", "Córdoba", "Barcelona", "2025/08/25", "09:15","A"],
    ["7","LATAM", "Montevideo", "Santiago", "2025/08/26", "06:00","B"],
    ["8","Sky Airline", "Buenos Aires", "San Pablo", "2025/08/28", "13:20","A"],
    ["9","LATAM", "San Pablo", "Quito", "2025/08/29", "15:00", "A"],
    ["10","Aerolíneas Arg", "Buenos Aires", "Roma", "2025/08/30", "19:45","A"],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
]

#Matriz de asientos
def generar_random():
    respuesta="R"
    num_generado=random.randint(0,3)
    if(num_generado==0):
        respuesta="L"
    elif(num_generado==1):
        respuesta="O"
    return respuesta

filaAsientos = [["L"]*7 for filas in range(len(vuelos)*40)]
filaAsientos = [[generar_random()]*7 for filas in range(len(vuelos)*40)]
for i in range(len(vuelos)*40):
    filaAsientos[i][3] = "-"

#Matriz de aerolineas

nombres = ["Aerolíneas Arg", "LATAM", "Sky Airline", "", ""]
codIATA = ["123", "231", "312", "", ""]
descripcion = ["asdasd", "dasdas", "dasdad", "", ""]
codPais = ["ARG", "CHI", "BRA", "", ""]
aereolineas = [nombres,codIATA,descripcion,codPais]

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
            limpiarConsola()
    return fecha



def comprobacionLen(a,b):
    while len(a) > b or len(a) == 0:
        if len(a) > b :
            a = input(f"La cantidad maxima de caracteres es {b}, por favor reintente: ")
        elif len(a) == 0 :
            a = input("El espacio no puede estar vacío, por favor reintente: ")
            

    
#Limpia la consola, adaptándose al sistema operativo.
def limpiarConsola():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
        
        

def validarFloat(x):
    f = True
    while f:
        try:
            x = float(input("Ingresa un número decimal: "))
            f = False  # Sale del bucle si la conversión es exitosa
        except ValueError:
            print("¡Error! Ingresa un número decimal válido.")
            
def validarCodigo():
    f = True
    while f:
        try:
            x = str()
            while len(x) > 5 or len(x) == 0:
                x = int(input(f"Ingresa un codigo de vuelo: "))
                while x < 0:
                    x = int(input(f"Codigo de vuelo invalido, ingrese nuevamente: "))
                    limpiarConsola()
                x = str(x)
                limpiarConsola()
                if len(x) > 5 :
                    print("Valor mayor al soportado, ingrese nuevamente:  ")
                elif len(str(x)) == 0 :
                    print("El espacio no puede estar vacío, por favor reintente: ")
            f = False  # Sale del bucle si la conversión es exitosa
        except ValueError:
            limpiarConsola()
            print("¡Error! Ingresa un valor válido.")
    return x


def validarEntero(funcionParametro):
    f = True
    while f :
        try:
            
            funcionParametro()
            x = int(input(f"Ingresa un valor: "))
            f = False  # Sale del bucle si la conversión es exitosa
            limpiarConsola()
        except ValueError:
            limpiarConsola()
            print("¡Error! Ingresa un valor válido.")
    return x
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
    print("3. Reservar Vuelos")
    print("4. Reservas")
    print("5. Ver Historial de Compras")
    print("6. Ver Novedades")
    print("7. Cerrar Sesión")
#en construccion
def subMenuUsuario(opc):
    while opc != 7:
        opc = validarEntero(menuUsuario)
        while opc < 0 or opc > 7:
            opc = validarEntero(menuUsuario)
        match opc:
            case 1: limpiarConsola(),buscarVuelos()
            case 2: limpiarConsola(),buscarAsientos()
            case 3: limpiarConsola(),cartel()
            case 4: limpiarConsola(),cartel()
            case 5: limpiarConsola(),cartel()
            case 6: limpiarConsola(),cartel()
            case 7: limpiarConsola()

def buscarVuelos():
    # Datos de vuelos
    # Encabezados
    headers = ["CÓDIGO", "AEROLÍNEA", "ORIGEN", "DESTINO", "FECHA", "HORA", "ESTADO", "PRECIO"]

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

#Buscar asientos

def imprimir_fila(fila):

    for pos in range (len(fila)):
        if(pos!=3):
            print("|   ",end="")
            print(fila[pos], end="")
            print("   |",end="")
        else:
            print("■■■■■■■",end="")
    print("")            
                
def imprimir_asientos(vuelo,i):
    print("\033[93m")  # Cambia el color a amarillo (código ANSI)
    print("   |    A      B      C   |PASILLO|   D      E      F   |")
    print("\033[92m")  # Cambia el color a amarillo (código ANSI)
    for fila in range (i*40,(i+1)*40):
        if(fila<10):
            num_fila="00"+str(fila)
        elif(fila<100):
            num_fila="0"+str(fila)
        else:
            num_fila=+fila
        print('\033[96m',end="")
        print(num_fila ,end="")
        print('\033[96m',end="")
        print("\033[0m",end="")   # Resetea el color

        imprimir_fila(vuelo[fila])

def buscarAsientos():
    #matriz de asientos
    f = True
    i = 0
    print("\n......Buscar Asientos......")
    print("Ingrese su número de vuelo:")
    codVuelo = input("Código de vuelo: ").strip()
    while f  and i < len(vuelos):
        if vuelos[i][0] == codVuelo:
            f = False
        else:
            i += 1
            
   
    if i >= len(vuelos):
        print("El vuelo no fue encontrado.")
    else:
        fecha = datetime.datetime.strptime(vuelos[i][4], "%Y/%m/%d")
        if fecha <= datetime.datetime.now():
            print("El vuelo ya ha pasado, no se pueden reservar asientos.")
        elif vuelos[i][6] == "B":
            print("El vuelo se encuentra cancelado, no se pueden reservar asientos.")
        else:
            inicioAsientos = i * 40
            imprimir_asientos(filaAsientos,i)
            
        
        
        
        

    

#Menu principal
def printMenuAdministrador():
    print("\n......MENU PRINCIPAL......")
    print("1. Gestión de Aerolíneas")
    print("2. Aprobar/Denegar Promociones")
    print("3. Gestión de Novedades")
    print("4. Reportes")
    print("5. Salir")

#Menu de Gestión de Aerolíneas
            
def gestionAerolinea():
    print("\n     ......Gestión Aereolinea......")
    print("     1. Crear Aereolinea")
    print("     2. Modificar Aereolinea")
    print("     3. Eliminar aereolinea")
    print("     0. Volver")

#Se fija cuantas aerolineas tiene cada código de país, devuelve un arrya con la cantidad de aerolíneas de ARG, CHI, BRA respectivamente

def cantidadesAerolíneas():
    cantidades = [0, 0, 0]  # [ARG, CHI, BRA]
    cantidadARG = 0
    cantidadCHI = 0
    cantidadBR = 0
    pos = 0
    while pos < len(aereolineas[3]):
        match aereolineas[3][pos]:
            case "ARG":
                cantidadARG += 1
            case "CHI":
                cantidadCHI += 1
            case "BRA":
                cantidadBR += 1
        pos += 1
    cantidades[0] = cantidadARG
    cantidades[1] = cantidadCHI
    cantidades[2] = cantidadBR
    return cantidades

def posicionMayor(lista):
    mayor = lista[0]
    pos = 0
    for i in range(1, len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
            pos = i
    return pos

def posicionMenor(lista):
    menor = lista[0]
    pos = 0
    for i in range(1, len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            pos = i
    return pos
    
#toma una posición 1,2,3 y determina a que país le corresponde
def pais(pos):
    respuesta=""
    if(pos==0):
        respuesta="ARG"
    elif(respuesta==1):
        respuesta="CHI"
    else:
        respuesta="BRA"
    return respuesta


#Submenu de creación de Aerolinea
def crearAerolinea():
    i = 0
    aux1 = 5
    flag = True
    salida = str("X") #character para que el while funcione
    while salida != "N":
        while flag and i < 5:
            if aereolineas[0][i] == "":
                codigoPais = str("A")
                salida = str("X")
                aereolineas[0][i] = str(input("ingrese el nombre de su aereolinea: "))
                comprobacionLen(aereolineas[0][i],100)
                aereolineas[1][i] = str(input("Ingrese el codigo IATA correspondiente: "))
                comprobacionLen(aereolineas[1][i],3)
                aereolineas[2][i] = str(input("Ingrese una breve descripción: "))
                comprobacionLen(aereolineas[2][i],200)
                while not (aereolineas[3][i] == "ARG" or aereolineas[3][i] == "BRA" or aereolineas[3][i] == "CHI"): #Este while obliga a que el codigo de pais este bien ingresado
                    aereolineas[3][i] = str(input("Ingrese el código de país correspondiente (ARG, CHI, BRA) ").upper())
                    comprobacionLen(codigoPais,3)
                    if aereolineas[3][i] != "ARG" and aereolineas[3][i] != "BRA" and aereolineas[3][i] !="CHI":
                        print("Código no valido")
                    
                print("DEBUG:",aereolineas)
                while salida != "N" and salida != "S": #se usa para determinar si se busca agregar aereolineas o no
                    salida = str(input("¿Desea seguir agregando aerolineas? S/N ").upper().strip())
                    if salida != "N" and salida != "S":
                        print("Carácter invalido, reingrese")
                        
                if salida == "N":
                    flag = False
                        
            else:
                i += 1
            
            if i == 5:
                print("Esta todo lleno, no es posible agregar más aerolíneas")
                salida="N"
                        

    cant = cantidadesAerolíneas()
    mayor_pos = posicionMayor(cant)
    menor_pos = posicionMenor(cant)
    print(f"La cantidad de aerolíneas creadas en Argentina son {cant[0]}, en Brasil son {cant[2]}, y en Chile son {cant[1]}.")
    print(f"El país con más aerolíneas es {pais(mayor_pos)}, con {cant[mayor_pos]} aerolíneas, mientras que el que menos tiene es {pais(menor_pos)}, con {cant[menor_pos]} aerolíneas.")

    input("Ingrese algo para continuar: ")
    limpiarConsola()
#Submenu del gestión de Aerolinea (selección de menu)

def subMenuGestionAereolineas(opc):
    opc = 1  # Valor inicial cualquiera diferente de 0
    while opc != 0:
        opc = validarEntero(gestionAerolinea)  # Asumo que gestionAerolinea() devuelve el menú
        match opc:
            case 1:
                limpiarConsola()
                crearAerolinea()
            case 2:
                cartel()                
            case 3:
                cartel()

            case 0:
                limpiarConsola()
                menuAdministrador(opc, novedades)
        if(opc<-1 or opc>3):
            print("Opción no válida")

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
    while i != 3 and not flag:
        if novedades[0][i] == codModificar:
            novedades [1][i] = input("Ingrese el texto de la novedad: ")
            comprobacionLen(novedades[1][i],200)
            novedades [2][i] = pedirFecha("Ingrese la fecha de publicación de la novedad: ")
            novedades [3][i] = pedirFecha("Ingrese la fecha de expiración: ")
            flag =True



def modificarNovedades(novedades):
    salidaNov = str("X")
    while salidaNov != "N":
        codModificar = (input("Ingrese el codigo a modificar (los codigos validos son 100, 101, 102.): "))
        while codModificar != "100" and codModificar != "101" and codModificar != "102":
            limpiarConsola()
            codModificar = (input("El número ingresado es invalido, reintente (los codigos validos son 100, 101, 102.): "))
        limpiarConsola()
        nov(novedades,codModificar)
                
        salidaNov = str(input("¿Desea modificar mas novedades? S/N: ").upper().strip())
        while salidaNov != "N" and salidaNov != "S":
            limpiarConsola()
            salidaNov = input("Carácter invalido, reintente (S/N): ")
    
def verNovedades(novedades):
    print(f"   |{novedades[0][0]},|{novedades[1][0]},  |Publicado el: {novedades[2][0]},  |Expira el: {novedades[3][0]}   |")
    print(f"   |{novedades[0][1]},|{novedades[1][1]},  |Publicado el: {novedades[2][1]},  |Expira el: {novedades[3][1]}   |")
    print(f"   |{novedades[0][2]},|{novedades[1][2]},  |Publicado el: {novedades[2][2]},  |Expira el: {novedades[3][2]}   |")
    input("Ingrese cualquier cosa para continuar: ")
    limpiarConsola()
    

#SubMenu de Gestión de novedades
def gestionNovedades(novedades):
    opc3 = int(1) #inicializo la variable en 1 para que el usuario ingrese al sistema.
    while (opc3 != 0):
        opc3 = validarEntero(printGestionNovedades)
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
        opc = validarEntero(printMenuAdministrador)
    while opc <= 0 or opc > 5:
        opc = validarEntero(printMenuAdministrador)
    match opc:
        case 1:limpiarConsola(),subMenuGestionAereolineas(opc)
        case 2:limpiarConsola(), cartel(), menuAdministrador(opc,novedades)
        case 3:limpiarConsola(), gestionNovedades(novedades)
        case 4:limpiarConsola(),cartel(), menuAdministrador(opc,novedades)
        case 5:limpiarConsola()
        #queda vacio ya que si vale 5 se cierra el programa
        
def busquedaVuelos(contArray,vuelos):
    flag = False
    while not flag:
        i = 0
        while i != contArray:
            while vuelos[i][0] == vuelos[contArray][0]:
                print("El codigo de vuelo ya existe, ingrese otro codigo.")
                vuelos[contArray][0] = validarCodigo()
                flag = True
            i += 1 
        if flag:
            flag = False
        else:
            flag = True
            print("Codigo de vuelo aceptado.")
            
#Función para crear un vuelo
def crearVuelo(vuelos,precioVuelos):
    contArray = 0
    flag1 = True
    rta = ""
    rta = input("Desea ver los vuelos ya cargados? S/N: ").upper().strip()
    while rta != "S" and rta != "N":
        rta = input("Ingreso invalido, reingrese su respuesta S/N: ").upper().strip()
    if rta == "S":
        buscarVuelos()
    while contArray < 20 and flag1 :
        while contArray < len(vuelos) and vuelos[contArray][0] != "":
            contArray += 1
        if contArray < len(vuelos):
            vuelos[contArray][0] = validarCodigo()
            busquedaVuelos(contArray,vuelos)
            flag = True
            while flag: #aseguramos que la aereolinea cargada en el vuelo sea una anteriormente aceptada por el sistema
                vuelos[contArray][1] = input("Ingrese el nombre de su aerolinea: ")
                limpiarConsola()
                i = 0
                while i != 5 and vuelos[contArray][1] != aereolineas[0][i]:
                    i += 1
                if i == 5: 
                    print("Aerolinea no valida.")
                    limpiarConsola()
                else:
                    flag = False
            vuelos[contArray][2] = input("Ingrese origen del vuelo: ")
            limpiarConsola()
            vuelos[contArray][3] = input("Ingrese destino del vuelo: ")
            limpiarConsola()
            vuelos[contArray][4] = pedirFecha("Ingrese la fecha de salida: ")
            limpiarConsola()
            vuelos[contArray][5] = input("Ingrese hora de salida: ")
            limpiarConsola()
            print("Ingrese el precio: ")
            precioVuelos[contArray] = validarEntero(limpiarConsola)
            vuelos[contArray][6] = "A"
            salida = input("¿Desea cargar más vuelos? S/N: ").upper().strip()
            while salida != "N" and salida != "S":
                salida = input("Ingreso no valido, ingrese S para si, N para no: ").upper().strip()
                limpiarConsola()
            if salida == "N":
                flag1 = False
        else:
            print("Se alcanzo el limite de vuelos creados.")


def modificarVuelo(vuelos, precioVuelos):
    opc = "S"
    f = True
    while f:
        codVuelo = validarCodigo()
        i = 0
        while i < 20 and f:
            if vuelos[i][0] == codVuelo and vuelos[i][6]  == "A":
                while opc == "S":
                    f = False
                    opcion = input("Ingrese un campo a modificar: (Nombre/Origen/Destino/Fecha/Hora/Precio): ")
                    limpiarConsola()
                    while opcion != "Fecha" and opcion != "Nombre" and opcion != "Origen" and opcion != "Destino" and opcion != "Hora" and opcion != "Precio":
                        print("El campo ingresado no existe.")
                        limpiarConsola()
                        opcion = input("Ingrese un campo a modificar (Nombre/Origen/Destino/Fecha/Hora/Precio): ")

                    match opcion:
                        case "Nombre":
                            vuelos[i][1] = input("Ingrese el nuevo nombre de su aerolinea: ")
                            limpiarConsola()

                        case "Origen":
                            vuelos[i][2] = input("Ingrese el nuevo origen del vuelo: ")
                            limpiarConsola()

                        case "Destino":
                            vuelos[i][3] = input("Ingrese el nuevo destino del vuelo: ")
                            limpiarConsola()

                        case "Fecha":
                            vuelos[i][4] = pedirFecha("Ingrese la nueva fecha de salida: ")
                            limpiarConsola()

                        case "Hora":
                            vuelos[i][5] = input("Ingrese la nueva hora de salida: ")
                            limpiarConsola()

                        case "Precio":
                            precioVuelos[i] = input("Ingrese el nuevo precio del vuelo: ")
                            limpiarConsola()

                    opc = input("Desea modificar algun otro campo? S/N: ")
                    while opc != "S" and opc != "N":
                        x = input("Opcion invalida, ingrese nuevamente: ")


            elif vuelos[i][6]  == "B":
                x = input("Desea darlo de alta?: ")
                while x != "S" and x != "N":
                    x = input("Opcion invalida, ingrese nuevamente: ")
                if x == "S":
                    vuelos[i][6] = "A"
                else:
                    ("No se ha podido modificar el vuelo.")
            else:
                i += 1
    if i == 20:
        print("No fue encontrado.")
        
    menugestionVuelos(opc2)

def eliminarVuelo(vuelos):

    f = True
    codVuelo = validarCodigo()
    i = 0
    while i < 20 and f:
        if vuelos[i][0] == codVuelo:
            f = False
            opc = input("Codigo de vuelo encontrado, esta seguro que quiere darlo de baja? S/N: ")
            while opc != "S" and opc != "N":
                opc = input("Codigo de vuelo invalido, ingrese nuevamente. S/N :")
            if vuelos[i][6]  == "A":    
                if opc == "S":
                    vuelos[i][6] = "B"
                    print("El vuelo se ha dado de baja correctamente.")
            else:
                print("El vuelo ingresado ya esta dado de baja.")              
        else:
            i += 1 
    if i == 20:
        print("Vuelo ingresado no existe.")



def menugestionVuelos(opc2):
    opc2 = int(1)
    while opc2 != 4:
        opc2 = validarEntero(gestionVuelos)
        while opc2 < 0 or opc > 4:
            opc2 = validarEntero(gestionVuelos)
        match opc2:
            case 1: limpiarConsola(), crearVuelo(vuelos,precioVuelos) 
            case 2: limpiarConsola(), modificarVuelo(vuelos,precioVuelos)
            case 3: limpiarConsola(), eliminarVuelo(vuelos)
            case 4: limpiarConsola(), subMenuCeo(opc, opc2)


def subMenuCeo(opc, opc2,):
    opc = int(1)
    while opc != 4:
        opc = validarEntero(menuCeo)
        while opc < 0 or opc > 4:
            opc = validarEntero(menuCeo)
        match opc:
            case 1: limpiarConsola(), menugestionVuelos(opc2)
            case 2: limpiarConsola(), cartel(),subMenuCeo(opc,opc2)
            case 3: limpiarConsola(),cartel(),subMenuCeo(opc,opc2)
            case 4: limpiarConsola()
    

def inicioSesion(opc, opc2):
    intentos = int(0)
    salida = "S"
    while salida == "S" and intentos < 3:
        nombreUsuario = input("Ingrese su nombre de usuario: ").strip()
        limpiarConsola()
        comprobacionLen(nombreUsuario,100)
        flagNombre= False
        i= 0
        while not flagNombre and i < 10:
            if datos[0][i] == nombreUsuario:
                flagNombre = True
            else:
                i += 1
        contrasenaUsuario = getpass.getpass("Ingrese su contraseña: ").strip()
        limpiarConsola()
        comprobacionLen(contrasenaUsuario,15)
        flagContra= False
        if i != 10 and datos[1][i] == contrasenaUsuario:
                flagContra = True
        if flagContra and flagNombre :
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
                    
                
            salida = input("Desea seguir con el programa? S/N: ").upper()
            while salida != "N" and salida != "S":
                limpiarConsola()
                salida = input("Caracter no valido, reintente (S/N): ")
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
    inicioSesion(opc, opc2)
    
def sistema(opc, clave, opc2):
    print("Bienvenidos al sistema de administración de aerolineas")
    clave = input("¿Desea iniciar sesion o registrarse? (1 para incio de sesión / 2 para registrarse): ")
    while clave != "1" and clave != "2":
        clave = input("¿Desea iniciar sesion o registrarse? (1 para incio de sesión / 2 para registrarse): ")
        if clave != "1" and clave != "2":
            limpiarConsola()
            print("Codigo invalido, reintente")
            
    if clave == "1":
        inicioSesion(opc, opc2)
    else:
        registro(opc)
    
    


    

sistema(opc, clave, opc2)