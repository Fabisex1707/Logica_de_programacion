import sqlite3
from sqlite3 import Error
import sys
from tabulate import tabulate

def crear_base_de_datos_y_tablas():
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()

            #activar llave foraneas
            cursor.execute("PRAGMA foreign_keys = ON;")

            #creacion de tabla clientes
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Clientes_registrados (
                    id_Cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_cliente TEXT NOT NULL,
                    apellidos_cliente TEXT NOT NULL
                )
            """)

            #creacion de tabla salones
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Salones_registrados (
                    id_Salon INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre_salon TEXT NOT NULL,
                    cupo INTEGER NOT NULL,
                    turno_matutino TEXT NOT NULL,
                    turno_vespertino TEXT NOT NULL,
                    turno_nocturno TEXT NOT NULL
                )
            """)

            #creacion de tabla reservaciones
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS reservaciones (
                    id_reservacion INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_cliente INTEGER NOT NULL,
                    nombre_cliente TEXT NOT NULL,
                    nombre_evento TEXT NOT NULL,
                    id_sala INTEGER NOT NULL,
                    nombre_salon TEXT NOT NULL,
                    fecha_reservacion TEXT NOT NULL,
                    turno TEXT NOT NULL,
                    FOREING KEY (id_cliente) REEFRENCES Clientes_registrados (id_Cliente) ON DELETE CASCADE,
                    FOREING KEY (id_sala) REEFRENCES Salones_registrados (id_Salon) ON DELETE CASCADE,
                    UNIQUE (id_sala, fecha_reservacion, turno)
                )
            """)
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
    except:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
    finally:
        conn.close()

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
            cursor.execute("INSERT INTO Salones_registrados (id_Salon, nombre_salon, cupo, turno_matutino, turno_vespertino, turno_nocturno) VALUES (?, ?);", (nombre, apellidos))
            print(f"Cliente {nombre} {apellidos} registrado exitosamente con el id: {cursor.lastrowid}.")
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