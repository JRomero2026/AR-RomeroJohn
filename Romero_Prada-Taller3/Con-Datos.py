# Importa la librería csv para leer archivos separados por delimitadores (; ,)
import csv

# Importa la librería json para convertir datos a formato JSON
import json

# Importa la librería os para trabajar con rutas y archivos del sistema operativo
import os

# Importa la librería para crear y manipular estructuras XML
import xml.etree.ElementTree as ET


# -------------------------------------------------------------------
# Ruta donde se encuentra almacenado el archivo Usuarios.csv
# La letra r indica que es una cadena de texto sin interpretar las "\"
# -------------------------------------------------------------------
RUTA = r"D:\Documents\GESTION DE REDES\VI trimestre\Automatizacion\Taller-3\Usuarios.csv"


# ===================================================================
# FUNCIÓN: obtener_datos()
# Objetivo: Leer el archivo CSV y almacenar la información en una lista
# ===================================================================
def obtener_datos():

    # Crea una lista vacía donde se guardarán los registros
    datos = []

    # Abre el archivo CSV en modo lectura utilizando codificación latin-1
    with open(RUTA, "r", encoding="latin-1") as archivo:

        # Lee el archivo utilizando ";" como separador de columnas
        lector = csv.DictReader(archivo, delimiter=";")

        # Recorre cada fila del archivo CSV
        for fila in lector:

            # Agrega cada fila (diccionario) a la lista datos
            datos.append(fila)

    # Retorna la lista con todos los registros
    return datos


# ===================================================================
# FUNCIÓN: mostrar_csv()
# Objetivo: Mostrar la información del CSV en forma de tabla
# ===================================================================
def mostrar_csv():

    # Obtiene todos los datos del archivo CSV
    datos = obtener_datos()

    # Imprime el título de la tabla
    print("\n================================================================     INFORMACIÓN DE USUARIOS     ==============================================================================\n")

    # Imprime los nombres de las columnas con un ancho fijo para alinearlas
    print(f"{'Cuenta':<8} {'Nombres':<12} {'Apellidos':<12} {'Cargo':<12} {'Dependencia':<15} {'Oficina':<10} {'Telefono':<15} {'Email':<20} {'Compañia':<10} {'Ciudad':<15} {'Estado':<10}")

    # Imprime una línea separadora
    print("-" * 175)

    # Recorre cada usuario almacenado en la lista
    for usuarios in datos:

        # Imprime los datos de cada usuario organizados en columnas
        print(
            f"{usuarios['Cuenta']:<8}"
            f"{usuarios['Nombres']:<12}"
            f"{usuarios['Apellidos']:<15}"
            f"{usuarios['Cargo']:<15}"
            f"{usuarios['Dependencia']:<15}"
            f"{usuarios['Oficina']:<10}"
            f"{usuarios['Telefono']:<15}"
            f"{usuarios['Email']:<30}"
            f"{usuarios['Compañia']:<8}"
            f"{usuarios['Ciudad']:<15}"
            f"{usuarios['Estado']:<10}"
        )


# ===================================================================
# FUNCIÓN: mostrar_xml()
# Objetivo: Convertir la información del CSV a formato XML y mostrarla
# ===================================================================
def mostrar_xml():

    # Obtiene los datos del archivo CSV
    datos = obtener_datos()

    # Crea el nodo principal llamado Usuarios
    raiz = ET.Element("Usuarios")

    # Recorre cada usuario del archivo
    for usuario in datos:

        # Crea un nodo hijo llamado Usuario
        nodo_usuario = ET.SubElement(raiz, "Usuario")

        # Recorre cada campo del usuario
        for clave, valor in usuario.items():

            # Crea una etiqueta XML con el nombre del campo
            campo = ET.SubElement(nodo_usuario, clave)

            # Asigna el valor correspondiente a la etiqueta
            campo.text = valor

    # Convierte toda la estructura XML en una cadena de texto
    xml = ET.tostring(raiz, encoding="unicode")

    # Imprime el título
    print("\n===== INFORMACIÓN EN FORMATO .XML =====\n")

    # Muestra el contenido XML generado
    print(xml)


# ===================================================================
# FUNCIÓN: mostrar_json()
# Objetivo: Convertir la información del CSV a formato JSON
# ===================================================================
def mostrar_json():

    # Obtiene los datos del archivo CSV
    datos = obtener_datos()

    # Imprime el título
    print("\n===== INFORMACIÓN EN FORMATO .JSON =====\n")

    # Convierte la lista de usuarios a formato JSON
    # indent=4 organiza el texto con sangría
    # ensure_ascii=False permite mostrar caracteres como ñ y tildes
    print(json.dumps(datos, indent=4, ensure_ascii=False))


# ===================================================================
# MENÚ PRINCIPAL DEL PROGRAMA
# ===================================================================

# while True mantiene el menú ejecutándose hasta que el usuario decida salir
while True:

    # Muestra el título del menú
    print("\n====================================")
    print("      TALLER 3 AUTOMATIZACIÓN")
    print("====================================")

    # Muestra las opciones disponibles
    print("1. Mostrar información CSV")
    print("2. Mostrar información XML")
    print("3. Mostrar información JSON")
    print("4. Salir")

    print("====================================")

    # Solicita al usuario seleccionar una opción
    opcion = input("Seleccione una opción: ")

    # Si la opción es 1, llama la función mostrar_csv()
    if opcion == "1":
        mostrar_csv()

    # Si la opción es 2, llama la función mostrar_xml()
    elif opcion == "2":
        mostrar_xml()

    # Si la opción es 3, llama la función mostrar_json()
    elif opcion == "3":
        mostrar_json()

    # Si la opción es 4, finaliza el programa
    elif opcion == "4":
        print("\nPrograma finalizado.")
        break

    # Si el usuario ingresa una opción diferente, muestra un mensaje de error
    else:
        print("\nOpción no válida.")