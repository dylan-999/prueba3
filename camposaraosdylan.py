
import os
import time 
import numpy


numpy.zeros = ((2,5),int)

lista_ruts = []
lista_nombres = []
lista_identificador_unicos = []
lista_nombres_mascotas = []
lista_cantidad_dias = []



def mostrar_menu_mascotas():
    os.system('clear')
    print("""MENÚ
    1.GRABAR
    2.BUSCAR
    3.RETIRARSE
    4.SALIR""")
    
def validar_opcion_menu():
    while True:
        try:
            opc = int(input("INGRESE UNA OPCION DEL MENU: "))
            if opc in(1,2,3,4):
                return opc
            else:
                print("ERROR! OPCIÓN INCORRECTA ")
        except:
            print("ERROR! DEBE INGRESAR UN NUMERO ENTERO")


def mostrar_hotel_mascotas():
    os.system('clear')
    print("\tVER HOTEL MASCOTAS\n")
    contador = 1
    for x in range(2):
        print(f"casillas para {(x+1)*2} mascotas: ",end=" ")
        for y in range(2):
            print(f"casillas {contador}:mascotas {[x][y]} ", end=" ")
            contador += 1
        print("\n")
        time.sleep(2)


def validar_rut():
        while True:
            try:
                rut = int(input("INGRESE RUT(SIN PUNTOS NI DIGITO VERIFICADOR): "))
                if rut >= 1000000 and rut <= 99999999:
                    return rut
                else:
                    print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
            except:
                print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")



def validar_nombre_dueño():
        while True:
            nombre = input("INGRESE SU NOMBRE: ")
            if len(nombre.strip()) >= 3 and nombre.isalpha():
                return nombre
            else:
                print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")


def validar_identificador_mascota():
        while True:
            try:
                identificador = int(input("INGRESE IDENTIFICADOR DE SU MASCOTA: "))
                if identificador >= 1 and 999999999:
                    return identificador
                else:
                    print("ERROR! NUMERO IDENTIFICADOR NO ENCONTRADO")
            except:
                print("ERROR DEBE INGRESAR UN NUMERO ENTERO")


def validar_nombre_mascota():
        while True:
            nombre_mascota = input("INGRESE EL NOMBRE DE SU MASCOTA: ")
            if len(nombre_mascota.strip()) >= 3 and nombre_mascota.isalpha():
                return nombre_mascota
            else:
                print("ERROR! EL NOMBRE DE SU MASCOTA DEBE TENER AL MENOS 3 LETRAS!")



def validar_cantidad_dias_permanece_mascota():
        while True:
            try:
                cantidad_dias = int(input("INGRESE LA CANTIDAD DE DIAS QUE PERMANECERA SU MASCOTA: "))
                if cantidad_dias >=1 and 1000:
                    return cantidad_dias
                else:
                    print("ERROR! CANTIDAD DE DIAS NO DISPONIBLE ")
            except:
                print("ERROR! DEBE INGRESAR UN NUMERO ENTERO ")



def validar_buscar_mascota():
    while True:
        try:
            rut = int(input("INGRESE RUT PARA BUSCAR SU MASCOTA(SIN PUNTOS NI DIGITO VERIFICADOR: )"))
            if rut >= 1000000 and rut <= 99999999:
                    return rut
            else:
                    print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
                print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")

        while True:
            try:
                casilla = int(input("INGRESE NUMERO DE CASILLA: "))
                if casilla in(casilla):
                    return casilla
                else:
                    print("ERROR! NUMERO DE MESA NO ENCONTRADA")
            except:
                    print("ERROR! DEBE INGRESAE UN NUMERO ENTERO ")

def validar_total_pago():
      while True:
        try:
            rut = int(input("INGRESE RUT PARA SABER SU PAGO DEL HOTEL DE MASCOTAS(SIN PUNTOS NI DIGITO VERIFICADOR: )"))
            if rut >= 1000000 and rut <= 99999999:
                    return rut
            else:
                    print("ERROR! EL RUT DEBE ESTAR ENTRE 1000000 y 99999999!")
        except:
                print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")



        while True:
            try:
                salir = input("DESEA SALIR DEL HOTEL (SI/NO): ")
                if salir in("SI/NO"):
                    break 
                else:
                    print("ERROR! OPCION INCORRECTA")
            except:
                 print("GRACIAS POR ASISTIR AL HOTEL DE MASCOTAS! ADIOS ")

            
        
        


  

        


     


   


    
         
        
         
     









   


