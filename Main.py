#MONGODB CON PYHTON 

from pymongo import MongoClient
from os import system

conectar = MongoClient('localhost')

db = conectar['Estudiante']
collection = db['registro']

def insertar():
    print("\nINSERTAR REGISTRO")
    identificacion = input("Ingrese identificacion: ")
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    nota1 = input("Ingrese nota 1: ")
    nota2 = input("Ingrese nota 2: ")
    collection.insert_one(
        {
            "Identificacion": identificacion,
            "Nombre": nombre,
            "Apellido": apellido,
            "Nota 1": nota1,
            "Nota 2": nota2
        }
    )
    print("\nREGISTRO INSERTADO...")

def eliminar():
    print("\nELIMINAR REGISTRO")
    aEliminar = input("Ingrese Identificacion: ")
    collection.delete_one(
        {
            "Identificacion": aEliminar
        }
    )
    print("\nREGISTRO ELIMINADO...")

def modificar():
    print("\nMODIFICAR REGISTRO")
    aModificar = input("Ingrese Identificacion: ")
    filter = (
        {
            "Identificacion": aModificar
        }
    )
    nuevoNot1 = input("Ingrese nuevo nota 1: ")
    nuevoNot2 = input("Ingrese nuevo nota 2: ")
    newValores = (
        {
            "$set": {"Nota 1": nuevoNot1, "Nota 2": nuevoNot2}
        }
    )
    collection.update_one(filter, newValores)
    print("\nREGISTRO MODIFICADO...")
    
def buscar():
    print("\nBUSCAR REGISTRO")
    aBuscar = input("Ingrese Identificacion: ")
    print("\nREGISTRO ENCONTRADO")
    encontrado = collection.find_one(
        {
            "Identificacion": aBuscar
            }
        )
    return print(encontrado)

def listar():
    registro = collection.find()
    for db in registro:
        print(db)
    return db

def menu():
    print("""MENU DE OPCIONES
        1. Insertar Registro
        2. Eliminar Registro
        3. Modificar Registro
        4. Consultar Registro
        5. Listar Registro
        6. SALIR""")

opcion = 0
while True:

    menu()

    opcion = input("Eliga una opcion: ")
    
    try:
        opcion = int(opcion)
    except ValueError:
        system("pause"); system("cls")

    if opcion is 1: 
        insertar()
        system("Pause"); system("cls")

    elif opcion is 2:
        eliminar()
        system("Pause"); system("cls")
    
    elif opcion is 3:
        modificar()
        system("Pause"); system("cls")
    
    elif opcion is 4:
        buscar()
        system("Pause"); system("cls")

    elif opcion is 5:
        listar()
        system("Pause"); system("cls")
    elif opcion is 6:
        break