import sqlite3
from sqlite3 import Error, IntegrityError
import sys
from tabulate import tabulate
from CONEXIONBD import crear_base_de_datos_y_tablas
from datetime import datetime
import json
import os


def insertar_cliente(nombre, apellidos):
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
        if conn:
            conn.close()

def insertar_salon(nombre_salon, cupo):
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Salones_registrados (nombre_salon, cupo) VALUES (?, ?);", (nombre_salon, cupo))
            print(f"{'*'*60}\n")
            print(f"--salon {nombre_salon} registrada exitosamente con el id: {cursor.lastrowid}.--")
            print(f"{'-'*60}\n")
    except Error as e:
        print(f"Error al registrar el salon: {e}")
    except:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
    finally:
        conn.close()

def registrar_cliente():
    print(f"\n{'*'*60}")
    print("\tVamos a registrar un nuevo cliente")
    print(f"{'-'*60}\n")
    
    while True:
        nombre_cliente = input("Escribe el nombre del cliente: ").strip().upper()

        if nombre_cliente == "":
            print("El nombre no puede estar vacío. Intenta de nuevo.\n")
            continue
        elif all(letra.isalpha() or letra.isspace() for letra in nombre_cliente):
            break
        else:
            print("El nombre no puede contener numeros ni caracteres especiales. intenta de nuevo.\n")
            continue

    while True:
        apellidos_cliente = input("Escribe los apellidos del cliente: ").strip().upper()
        if apellidos_cliente == "":
            print("Los apellidos no pueden estar vacíos. Intenta de nuevo.\n")
            continue
        elif all(letra.isalpha() or letra.isspace() for letra in apellidos_cliente):
            break
        else:
            print("El nombre no puede contener numeros ni caracteres especiales. intenta de nuevo.\n")
            continue
    insertar_cliente(nombre_cliente, apellidos_cliente) 
    print(f"\n Cliente registrado: {nombre_cliente} {apellidos_cliente}\n")


def registrar_salon():
    print(f"\n{'*'*60}")
    print("\tVamos a registrar una nueva salon")
    print(f"{'-'*60}\n")
    while True:
        nombre_salon = input("Escribe el nombre del salon: ").strip().upper()
        if nombre_salon == "":
            print("El nombre no puede estar vacio. Intenta de nuevo.\n")
            continue
        if all(letra.isalpha() or letra.isspace() for letra in nombre_salon):
            break
        else:
            print("Debes ingresar un nombre de salon y cupo validos!\n")
            continue
    while True:
        cupo = input("Escribe el cupo del salon: ").strip()
        if cupo == "":
            print("El cupo no puede quedar vacio. Intenta de nuevo.\n")
            continue
        elif cupo.isdigit():
            break
        else:
            print("El cupo debe ser un número entero positivo. Intenta de nuevo.\n")
            continue
    insertar_salon(nombre_salon, int(cupo))

def estado_turno(turno):
    return "DISPONIBLE" if turno else "NO DISPONIBLE"

def selccionar_salones_registrados():
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Salones_registrados;")
            salones = cursor.fetchall()
            return salones
    except Error as e:
        print(f"Error al obtener los salones: {e}")
        return []
    except:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
        return []
    finally:
        if conn:
            conn.close()

def mostrar_salones():
    salones=selccionar_salones_registrados()
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


def selccionar_clientes_registrados():
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Clientes_registrados;")
            clientes = cursor.fetchall()
            return clientes
    except Error as e:
        print(f"Error al obtener los clientes: {e}")
        return []
    except:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
        return []
    finally:
        if conn:
            conn.close()

def mostrar_clientes():
    clientes=selccionar_clientes_registrados()
    if clientes:
        print(f"{'*'*60}\n")
        print("Lista de clientes registrados:\n")
        print(tabulate(clientes, headers=["ID Cliente", "Nombre Cliente", "Apellidos Cliente"], tablefmt="fancy_grid"))
        print(f"{'-'*60}\n")
    else:
        print("No hay clientes registrados.")

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
    try:
        fecha_date = datetime.strptime(fecha_str, "%m-%d-%Y").date()
        return fecha_date
    except ValueError:
        print("Formato de fecha incorrecto. Usa MM-DD-YYYY.")
        return None
    

def mostrar_disponibilidad_de_salon_por_fecha(fecha_iso):
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
                return reservaciones
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
        if conn:
            conn.close()

'''se agrega bucle while para verificar que los datos sean correctos.
Que se cumplan con los parametros requeridos 
y que se repita el pedirel a el usuario los datos hasta que sean registrados de forma correcta'''

def consultar_reservaciones_por_fecha():
    while True:
        fecha_entrada = input("¿Para qué fecha deseas consultar la reservacion? (MM-DD-YYYY): ").strip()
        if fecha_entrada == "": 
            fecha_entrada= datetime.today().strftime("%m-%d-%Y")

        try:
            fecha_dt = datetime.strptime(fecha_entrada, "%m-%d-%Y").date()
            break
        except ValueError:
            print("Formato de fecha inválido. Intenta de nuevo (MM-DD-YYYY).")

    try:
        with sqlite3.connect("reservaciones.db") as conexion:
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT id_reservacion, id_cliente, nombre_cliente, nombre_evento,
                id_salon, nombre_salon, fecha_reservacion, turno
                FROM reservaciones
                WHERE fecha_reservacion = ?;
            """, (fecha_entrada,))
            filas = cursor.fetchall()
    except sqlite3.Error as error_bd:
        print(f"Error al consultar la base de datos: {error_bd}")
        return

    print("\n" + "*" * 70)
    print(f"** REPORTE DE RESERVACIONES PARA EL DÍA {fecha_entrada} **")
    print("*" * 70)

    if not filas:
        print("No hay reservaciones para esa fecha.")
        print("*" * 70)
        print("*************** FIN DEL REPORTE ***************\n")
        return
    
    tabla_para_mostrar = []
    lista_para_json = []
    for fila in filas:
        (id_reservacion, id_cliente, nombre_cliente, nombre_evento,
        id_salon, nombre_salon, fecha_reservacion, turno) = fila

        tabla_para_mostrar.append([
            id_salon,
            nombre_cliente,
            nombre_evento,
            turno
        ])

        lista_para_json.append({
            "ID_Salon": id_salon,
            "Nombre_Cliente": nombre_cliente,
            "Evento": nombre_evento,
            "Turno": turno
        })

    print(tabulate(
        tabla_para_mostrar,
        headers=["Sala","Cliente","Evento","Turno"],
        tablefmt="grid"
    ))

    while True:
        respuesta_exportar = input("\n¿Desea exportar el reporte a JSON? (s/n): ").strip().lower()
        if respuesta_exportar in ("s", "n"):
            break
        print("Respuesta inválida. Escriba 's' o 'n'.")

    if respuesta_exportar == "s":
        nombre_archivo_reporte = "reporte_reservaciones.json"
        try:
            with open(nombre_archivo_reporte, "w") as archivo_reporte:
                json.dump(lista_para_json, archivo_reporte, ensure_ascii=False, indent=4)
            print(f"\nReporte exportado a '{nombre_archivo_reporte}'.")
        except Exception as error_fichero:
            print(f"No se pudo exportar el reporte: {error_fichero}")

    print("*" * 70)
    print("*************** FIN DEL REPORTE ***************\n")

def editar_nombre_reservacion():
    while True:
        try:
            print(f"{'*'*60}")
            print("Vamos a editar el nombre de una reservación")
            print(f"{'-'*60}\n")

            fecha_inicio_str = input("Ingresa la fecha de inicio (MM-DD-YYYY): ").strip()
            fecha_fin_str = input("Ingresa la fecha de fin (MM-DD-YYYY): ").strip()

            try:
                fecha_inicio = datetime.strptime(fecha_inicio_str, "%m-%d-%Y")
                fecha_fin = datetime.strptime(fecha_fin_str, "%m-%d-%Y")
            except ValueError:
                print("Formato de fecha inválido. Usa MM-DD-YYYY.")
                return

            if fecha_inicio == "" or fecha_fin == "":
                print("No se permite dejar el rango de fechas vacío.")
                continue

            with sqlite3.connect("reservaciones.db") as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id_reservacion, nombre_evento, fecha_reservacion, nombre_salon, turno
                    FROM reservaciones
                    WHERE fecha_reservacion BETWEEN ? AND ?
                    ORDER BY fecha_reservacion;
                """, (fecha_inicio_str, fecha_fin_str))
                eventos = cursor.fetchall()

            if not eventos:
                print("No hay eventos registrados en ese rango de fechas.")
                return

            print(tabulate(eventos, headers=["Folio", "Nombre Evento", "Fecha", "Nombre Salon", "Turno"], tablefmt="fancy_grid"))

            while True:
                folio_str = input("\nIngresa el folio del evento a modificar o Enter para cancelar: ").strip()
                if folio_str == "":
                    print("Operación cancelada.")
                    return

                if not folio_str.isdigit():
                    print("Solo se admiten números enteros. Intenta de nuevo.")
                    continue

                folio = int(folio_str)
                evento_seleccionado = next((evento for evento in eventos if evento[0] == folio), None)

                if evento_seleccionado is None:
                    print("El ID ingresado no pertenece al rango mostrado. Intenta de nuevo.")
                else:
                    break

            while True:
                nuevo_nombre = input(f"Escribe el nuevo nombre para el evento '{evento_seleccionado[1]}': ").strip().upper()
                if nuevo_nombre == "":
                    print("El nombre del evento no puede estar vacío. Intenta de nuevo.")
                elif nuevo_nombre.isdigit():
                    print("El nombre del evento no puede contener solo números. Intenta de nuevo.")
                else:
                    break

            with sqlite3.connect("reservaciones.db") as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    UPDATE reservaciones
                    SET nombre_evento = ?
                    WHERE id_reservacion = ?;
                """, (nuevo_nombre, folio))
                conn.commit()

            print(f"\nEvento actualizado exitosamente a: {nuevo_nombre}")


        except sqlite3.Error as e:
            print(f"Error al acceder a la base de datos: {e}")
        except Exception:
            print(f"Ocurrió un error inesperado: {sys.exc_info()[0]}")

def registrar_reservacion():
    print(f"{'*'*60}")
    print("Registrar una nueva reservacion")
    print(f"{'-'*60}\n")
    hay_clientes=selccionar_clientes_registrados()
    hay_salones=selccionar_salones_registrados()

    if hay_clientes and hay_salones:
        pass
    else:
        print("No hay clientes O salones registrados. Por favor, registra clientes y salones antes de hacer una reservacion.\n")
        return None
    
    mostrar_clientes()

    while True:
        id_cliente = input("Escribe el id del cliente: ").strip()
        cliente_encontrado = buscar_cliente_por_id(id_cliente)

        if cliente_encontrado is None:
            print("El id del cliente no existe.\n")
            salir=input("¿Deseas salir del proceso de reservacion? (s/n): ").strip().lower()
            if salir == 's':
                return None
            continue
        break
    nombre_cliente = cliente_encontrado[1]

    while True:
        str_fecha_reservacion = input("Escribe la fecha de la reservacion (MM-DD-YYYY): ").strip()
        fecha_reservacion_dt = str_fecha_a_date(str_fecha_reservacion)

        if fecha_reservacion_dt is None:
            continue
        
        fecha_actual = datetime.today().date()
        print(fecha_actual)
        diferencia = (fecha_reservacion_dt - fecha_actual).days
        
        if diferencia < 2:
            print("Error: No puedes hacer tu reservación, debe ser con dos días de anticipación!\n")
            continue
        
        dia_semana = fecha_reservacion_dt.strftime("%A")
        if dia_semana in ("Domingo", "Sunday"):
            print("Error: No puedes hacer tu reservación los domingos, elija el siguiente dia lunes!\n")
            continue
        
        break

    while True:        
        datos_salon_de_una_fecha = mostrar_disponibilidad_de_salon_por_fecha(str_fecha_reservacion)
        id_salon = input("Escribe el id del salon: ").strip()
        salon_encontrado = buscar_salon_por_id(id_salon)

        if salon_encontrado is None:
            print("El id del salon no existe.\n")
            continue
        break
    
    nombre_salon = salon_encontrado[1]
    
    while True:
        turno = input("Escribe el turno (Matutino, Vespertino, Nocturno): ").strip().capitalize()

        if turno not in ['Matutino', 'Vespertino', 'Nocturno']:
            print("Turno invalido. Debe ser Matutino, Vespertino o Nocturno.\n")
            continue
        
        turno_disponible = False
        for dato in datos_salon_de_una_fecha:
            if str(dato[0]) == id_salon:
                if dato[9:12]==(0,0,0):
                    print("\nNingun turno esta disponible para este salon en la fecha seleccionada.\n")
                    return None
                elif turno == 'Matutino' and dato[9] == 0:
                    print("\nEl turno Matutino no esta disponible para este salon en la fecha seleccionada.\n")
                    break
                elif turno == 'Vespertino' and dato[10] == 0:
                    print("\nEl turno Vespertino no esta disponible para este salon en la fecha seleccionada.\n")
                    break
                elif turno == 'Nocturno' and dato[11] == 0:
                    print("\nEl turno Nocturno no esta disponible para este salon en la fecha seleccionada.\n")
                    break
                else:
                    turno_disponible = True
                    break
        
        if turno_disponible:
            break

    while True:            
        nombre_evento = input("Escribe el nombre del evento: ").strip().upper()
        if nombre_evento == "":
            print("El nombre del evento no puede estar vacio.\n")
            continue
        break

    insertar_reservacion(id_cliente, nombre_cliente, nombre_evento, id_salon, nombre_salon, str_fecha_reservacion, turno)
            
def main():
    crear_base_de_datos_y_tablas()
    while True:
        print(f"{'*'*60}")
        print("Sistema para el registro de salas de coworking\n")
        print(f"{'-'*60}\n")
        print("1. Hacer una reservacion")
        print("2. Editar nombre de reservacion")
        print("3. Consultar reservaciones por fecha")
        print("4. Registrar un nuevo cliente")
        print("5. Registrar un nuevo salon")
        print("6. Salir\n")
        
        opcion = input("Que opcion eliges? ")
        if opcion == "6":
            print("saliendo del sistema...")
            break
        elif opcion == "1":
            registrar_reservacion()
        elif opcion == "2":
            editar_nombre_reservacion()
        elif opcion == "3":
            consultar_reservaciones_por_fecha()
        elif opcion == "4":
            registrar_cliente()
        elif opcion == "5":
            registrar_salon()
        else:
            print("Opcion invalida. Intenta de nuevo.\n")


if __name__ == "__main__":
    main()