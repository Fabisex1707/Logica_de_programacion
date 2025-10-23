import sqlite3
from sqlite3 import Error, IntegrityError
import sys
from tabulate import tabulate
from CONEXIONBD import crear_base_de_datos_y_tablas

def registrar_cliente(nombre, apellidos):
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Clientes_registrados (nombre_cliente, apellidos_cliente) VALUES (?, ?);", (nombre, apellidos))
            print(f"{'*'*60}\n")
            print(f"--Cliente {nombre} {apellidos} registrado exitosamente con el id: {cursor.lastrowid}.--")
            print(f"{'-'*60}\n")
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
            cursor.execute("INSERT INTO Salones_registrados (nombre_salon, cupo) VALUES (?, ?);", (nombre_salon, cupo))
            print(f"{'*'*60}\n")
            print(f"--Sala {nombre_salon} registrado exitosamente con el id: {cursor.lastrowid}.--")
            print(f"{'-'*60}\n")
    except Error as e:
        print(f"Error al registrar el cliente: {e}")
    except:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
    finally:
        conn.close()

def estado_turno(turno):
    return "DISPONIBLE" if turno else "NO DISPONIBLE"

def mostrar_salones():
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Salones_registrados;")
            salones = cursor.fetchall()
            salones_disponibles = []
            for salon in salones:
                salones_disponibles.append(salon[0:3] + (estado_turno(salon[3]), estado_turno(salon[4]), estado_turno(salon[5])))
            if salones_disponibles:
                print(f"{'*'*60}\n")
                print("Lista de salones registrados:\n")
                print(tabulate(salones_disponibles, headers=["ID Salon", "Nombre Salon", "Cupo", "Turno Matutino", "Turno Vespertino", "Turno Nocturno"], tablefmt="fancy_grid"))
                print(f"{'-'*60}\n")
            else:
                print("No hay salones registrados.")
    except Error as e:
        print(f"Error al obtener los salones: {e}")
    except:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
    finally:
        if conn:
            conn.close()
def mostrar_clientes():
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Clientes_registrados;")
            clientes = cursor.fetchall()
            if clientes:
                print(f"{'*'*60}\n")
                print("Lista de clientes registrados:\n")
                print(tabulate(clientes, headers=["ID Cliente", "Nombre Cliente", "Apellidos Cliente"], tablefmt="fancy_grid"))
                print(f"{'-'*60}\n")
            else:
                print("No hay clientes registrados.")
    except Error as e:
        print(f"Error al obtener los clientes: {e}")
    except:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
    finally:
        if conn:
            conn.close()

def mostrar_reservaciones():
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reservaciones;")
            reservaciones = cursor.fetchall()
            if reservaciones:
                print(f"{'*'*60}\n")
                print("Lista de reservaciones registradas:\n")
                print(tabulate(reservaciones, headers=["ID Reservacion", "ID Cliente", "Nombre Cliente", "Nombre Evento", "ID Salon", "Nombre Salon", "Fecha Reservacion", "Turno"], tablefmt="fancy_grid"))
                print(f"{'-'*60}\n")
            else:
                print("No hay reservaciones registradas.")
    except Error as e:
        print(f"Error al obtener las reservaciones: {e}")
    except:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
    finally:
        if conn:
            conn.close()    

def buscar_salon_por_id(id_salon):
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Salones_registrados WHERE id_salon = ?;", (id_salon,))
            salon = cursor.fetchone()
            return salon
    except Error as e:
        print(f"Error al buscar el salon: {e}")
        return None
    except:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
        return None
    finally:
        if conn:
            conn.close()

def buscar_cliente_por_id(id_cliente):
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Clientes_registrados WHERE id_cliente = ?;", (id_cliente,))
            cliente = cursor.fetchone()
            return cliente
    except Error as e:
        print(f"Error al buscar el cliente: {e}")
        return None
    except:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
        return None
    finally:
        if conn:
            conn.close()

def str_fecha_a_date(fecha_str):
    from datetime import datetime
    try:
        fecha_date = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        return fecha_date
    except ValueError:
        print("Formato de fecha incorrecto. Usa YYYY-MM-DD.")
        return None
    

def mostrar_disponibilidad_de_sala_por_fecha(fecha_iso):
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cur = conn.cursor()
            sql = """
            SELECT
                s.id_salon,
                s.nombre_salon,
                s.cupo,
                s.turno_matutino,
                s.turno_vespertino,
                s.turno_nocturno,
                MAX(CASE WHEN r.turno = 'Matutino' THEN 1 ELSE 0 END) AS reservado_matutino,
                MAX(CASE WHEN r.turno = 'Vespertino' THEN 1 ELSE 0 END) AS reservado_vespertino,
                MAX(CASE WHEN r.turno = 'Nocturno' THEN 1 ELSE 0 END) AS reservado_nocturno,
                CASE WHEN s.turno_matutino = 1 AND MAX(CASE WHEN r.turno = 'Matutino' THEN 1 ELSE 0 END) = 0 THEN 1 ELSE 0 END AS disponible_matutino,
                CASE WHEN s.turno_vespertino = 1 AND MAX(CASE WHEN r.turno = 'Vespertino' THEN 1 ELSE 0 END) = 0 THEN 1 ELSE 0 END AS disponible_vespertino,
                CASE WHEN s.turno_nocturno = 1 AND MAX(CASE WHEN r.turno = 'Nocturno' THEN 1 ELSE 0 END) = 0 THEN 1 ELSE 0 END AS disponible_nocturno
            FROM Salones_registrados s
            LEFT JOIN reservaciones r
            ON s.id_salon = r.id_salon
            AND r.fecha_reservacion = ?
            GROUP BY s.id_salon, s.nombre_salon, s.cupo, s.turno_matutino, s.turno_vespertino, s.turno_nocturno
            ORDER BY s.id_salon;
            """
            cur.execute(sql, (fecha_iso,))
            reservaciones = cur.fetchall()
            salones_disponibles = []
            for reservacion in reservaciones:
                salones_disponibles.append(reservacion[0:3] + (estado_turno(reservacion[9]), estado_turno(reservacion[10]), estado_turno(reservacion[11])))
            if salones_disponibles:
                print(f"{'*'*60}\n")
                print("Lista de salones registrados:\n")
                print(tabulate(salones_disponibles, headers=["ID Salon", "Nombre Salon", "Cupo", "Turno Matutino", "Turno Vespertino", "Turno Nocturno"], tablefmt="fancy_grid"))
                print(f"{'-'*60}\n")
                return None
            else:
                print("No hay salones registrados.")
                return None
    except Error as e:
        print(f"Error al verificar disponibilidad: {e}")
        return None
    except:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
        return None

def insertar_reservacion(id_cliente, nombre_cliente, nombre_evento, id_salon, nombre_salon, fecha_reservacion, turno):
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO reservaciones (id_cliente, nombre_cliente, nombre_evento, id_salon, nombre_salon, fecha_reservacion, turno)
                VALUES (?, ?, ?, ?, ?, ?, ?);
            """, (id_cliente, nombre_cliente, nombre_evento, id_salon, nombre_salon, fecha_reservacion, turno))
            print(f"{'*'*60}\n")
            print(f"--Reservacion para el evento {nombre_evento} registrada exitosamente con el id: {cursor.lastrowid}.--")
            print(f"{'-'*60}\n")
    except IntegrityError:
        print("Error: La reservacion no se pudo registrar porque el salon ya esta reservado para esa fecha y turno.")
    except Error as e:
        print(f"Error al registrar la reservacion: {e}")
    except:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
    finally:
        conn.close()

def registrar_reservacion():
    print(f"{'*'*60}")
    print("Registrar una nueva reservacion")
    print(f"{'-'*60}\n")
    mostrar_clientes()
    id_cliente = input("Escribe el id del cliente: ").strip()
    cliente_encontrado = buscar_cliente_por_id(id_cliente)
    if cliente_encontrado is None:
        print("El id del cliente no existe.")
        return
    nombre_cliente = cliente_encontrado[1]
    str_fecha_reservacion = input("Escribe la fecha de la reservacion (YYYY-MM-DD): ").strip()
    fecha_reservacion_dt=str_fecha_a_date(str_fecha_reservacion)
    if fecha_reservacion_dt is None:
        return
    mostrar_disponibilidad_de_sala_por_fecha(str_fecha_reservacion)
    id_salon = input("Escribe el id del salon: ").strip()
    salon_encontrado = buscar_salon_por_id(id_salon)
    if salon_encontrado is None:
        print("El id del salon no existe.")
        return
    nombre_salon = salon_encontrado[1]
    turno = input("Escribe el turno (Matutino, Vespertino, Nocturno): ").strip().capitalize()
    if turno not in ['Matutino', 'Vespertino', 'Nocturno']:
        print("Turno invalido. Debe ser Matutino, Vespertino o Nocturno.")
        return
    nombre_evento = input("Escribe el nombre del evento: ").strip().upper()
    if nombre_evento == "":
        print("El nombre del evento no puede estar vacio.")
        return
    insertar_reservacion(id_cliente, nombre_cliente, nombre_evento, id_salon, nombre_salon, str_fecha_reservacion, turno)
        




def main():
    crear_base_de_datos_y_tablas()
    while True:
        print(f"{'*'*60}")
        print("Sistema de registro de clientes\n")
        print(f"{'-'*60}\n")
        print("1. Registrar un nuevo cliente")
        print("2. registrar una nueva sala")
        print("3. mostrar salones registrados")
        print("4. hacer una reservacion")
        print("5. mostrar estado de reservaciones") 
        print("6. salir\n")
        opcion = input("Que opcion eliges? ")
        if opcion == "6":
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
        elif opcion == "2":
            print(f"\n{'*'*60}")
            print("\tVamos a registrar una nueva sala")
            print(f"{'-'*60}\n")

            nombre_salon = input("Escribe el nombre del salon: ").strip().upper()
            cupo = input("Escribe el cupo del salon: ").strip()

            if nombre_salon == "" or cupo == "":
                print("Debes ingresar un nombre de salon y cupo validos!")
                continue
            elif all(letra.isalpha() or letra.isspace() for letra in nombre_salon) and cupo.isdigit():
                registrar_sala(nombre_salon, int(cupo))
            else:
                print("Debes ingresar un nombre de salon y cupo validos!")
                continue
        elif opcion == "3":
            mostrar_salones()
        elif opcion == "4":
            registrar_reservacion()
        elif opcion == "5":
            mostrar_reservaciones()

if __name__ == "__main__":
    main()