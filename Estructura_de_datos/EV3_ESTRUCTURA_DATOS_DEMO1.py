import sqlite3
from sqlite3 import Error
import sys
from tabulate import tabulate
from CONEXIONBD import crear_base_de_datos_y_tablas

def registrar_cliente(nombre, apellidos):
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Clientes_registrados (nombre_cliente, apellidos_cliente) VALUES (?, ?);", (nombre, apellidos))
            print(f"Cliente {nombre} {apellidos} registrado exitosamente con el id: {cursor.lastrowid}.")
    except Error as e:
        print(f"Error al registrar el cliente: {e}")
    except:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
    finally:
        conn.close()

def registrar_sala(nombre_salon, cupo):
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Salones_registrados (id_Salon, nombre_salon, cupo, turno_matutino, turno_vespertino, turno_nocturno) VALUES (?, ?);", (nombre_salon, cupo))
            print(f"{'*'*60}")
            print(f"--Salon {nombre_salon} registrado exitosamente con el id: {cursor.lastrowid}.--")
            print(f"{'-'*60}\n")
    except Error as e:
        print(f"Error al registrar el cliente: {e}")
    except:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
    finally:
        conn.close()


def main():
    crear_base_de_datos_y_tablas()
    while True:
        print(f"{'*'*60}")
        print("Sistema de registro de clientes\n")
        print(f"{'-'*60}\n")
        print("1. Registrar un nuevo cliente")
        print("2. registrar una nueva sala")
        print("3. hacer una reservacion") 
        print("4. salir\n")
        opcion = input("Que opcion eliges? ")
        if opcion == "4":
            print("saliendo del sistema...")
            break
        elif opcion == "1":
            print(f"\n{'*'*60}")
            print("\tVamos a registrar un nuevo cliente")
            print(f"{'-'*60}\n")

            nombre_cliente = input("Escribe el nombre del cliente: ").strip().upper()
            apellidos_cliente = input("Escribe los apellidos del cliente: ").strip().upper()

            if nombre_cliente == "" or apellidos_cliente == "":
                print("Debes ingresar un nombre y apellidos validos!")
                continue
            elif all(letra.isalpha() or letra.isspace() for letra in nombre_cliente) and all(letra.isalpha() or letra.isspace() for letra in apellidos_cliente):
                registrar_cliente(nombre_cliente, apellidos_cliente)
            else:
                print("Debes ingresar un nombre y apellidos validos!")
                continue

if __name__ == "__main__":
    main()