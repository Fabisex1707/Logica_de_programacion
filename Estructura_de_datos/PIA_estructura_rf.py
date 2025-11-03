import sqlite3
from sqlite3 import Error, IntegrityError
import sys
from tabulate import tabulate
from CONEXIONBD import crear_base_de_datos_y_tablas
from datetime import datetime
import json
import os

def inicializar_base_de_datos():
    """
    Inicializa y verifica la base de datos del sistema.
    Crea una nueva base de datos con sus tablas si no existe.
    """
    DB_FILE="reservaciones.db"
    if os.path.exists(DB_FILE):
        print(f"{'*'*60}\n")
        print(f"Base de datos encontrada: {DB_FILE}")
        print(f"{'-'*60}\n")
    else:
        print(f"{'*'*60}\n")
        print(f"No se encontró la base de datos. Creando una nueva en: {DB_FILE}")
        print(f"{'-'*60}\n")
        crear_base_de_datos_y_tablas()

def insertar_cliente(nombre, apellidos):
    """
    Inserta un nuevo cliente en la tabla Clientes_registrados.

    Args:
        nombre (str): Nombre del cliente.
        apellidos (str): Apellidos del cliente.
    """
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
    """
    Inserta un nuevo salón en la tabla Salones_registrados.

    Args:
        nombre_salon (str): Nombre del salón.
        cupo (int): Capacidad máxima del salón.
    """
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
    """
    Solicita al usuario el nombre y apellidos para registrar un nuevo cliente.
    Realiza validaciones para asegurar que los campos no estén vacíos y sean alfabéticos.
    """
    print(f"\n{'*'*60}")
    print("\tVamos a registrar un nuevo cliente")
    print(f"{'-'*60}\n")
    
    while True:
        nombre_cliente = input("Escribe el nombre del cliente: ").strip().upper()

        if nombre_cliente == "":
            print(f"{'*'*60}\n")
            print("El nombre no puede estar vacío. Intenta de nuevo.\n")
            return 
        elif all(letra.isalpha() or letra.isspace() for letra in nombre_cliente):
            break
        else:
            print("El nombre no puede contener numeros ni caracteres especiales. intenta de nuevo.\n")
            continue

    while True:
        apellidos_cliente = input("Escribe los apellidos del cliente: ").strip().upper()
        if apellidos_cliente == "":
            print(f"{'*'*60}\n")
            print("Los apellidos no pueden estar vacíos. Intenta de nuevo.\n")
            return
        elif all(letra.isalpha() or letra.isspace() for letra in apellidos_cliente):
            break
        else:
            print("Los apellidos no puede contener numeros ni caracteres especiales. intenta de nuevo.\n")
            continue
    insertar_cliente(nombre_cliente, apellidos_cliente)


def registrar_salon():
    """
    Solicita al usuario el nombre y cupo para registrar un nuevo salón.
    Realiza validaciones para asegurar que los campos no estén vacíos y el cupo sea numérico.
    """
    print(f"\n{'*'*60}")
    print("\tVamos a registrar una nueva salon")
    print(f"{'-'*60}\n")
    while True:
        nombre_salon = input("Escribe el nombre del salon: ").strip().upper()
        if nombre_salon == "":
            print(f"{'*'*60}\n")
            print("El nombre no puede estar vacio. Intenta de nuevo.\n")
            return
        if all(letra.isalpha() or letra.isspace() for letra in nombre_salon):
            break
        else:
            print("Debes ingresar un nombre sin caracteres especiales o numeros!\n")
            continue
    while True:
        cupo = input("Escribe el cupo del salon: ").strip()
        if cupo == "":
            print(f"{'*'*60}\n")
            print("El cupo no puede quedar vacio. Intenta de nuevo.\n")
            return
        elif cupo.isdigit() and int(cupo) > 0:
            break
        else:
            print("El cupo debe ser un número entero positivo mayor a 0. Intenta de nuevo.\n")
            continue
    insertar_salon(nombre_salon, int(cupo))

def estado_turno(turno):
    """
    Convierte un valor de estado de turno (1/0 o True/False) a una cadena legible.

    Args:
        turno (int or bool): El estado del turno (1/True es disponible).

    Returns:
        str: "DISPONIBLE" o "NO DISPONIBLE".
    """
    return "DISPONIBLE" if turno else "NO DISPONIBLE"

def selccionar_salones_registrados():
    """
    Consulta y devuelve todos los salones de la tabla Salones_registrados.

    Returns:
        list: Una lista de tuplas con los datos de los salones, o lista vacía si hay error.
    """
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

def selccionar_clientes_registrados():
    """
    Consulta y devuelve todos los clientes de la tabla Clientes_registrados.

    Returns:
        list: Una lista de tuplas con los datos de los clientes, o lista vacía si hay error.
    """
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                            SELECT id_cliente,nombre_cliente,apellidos_cliente
                            FROM Clientes_registrados 
                            ORDER BY apellidos_cliente;""")
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

def selccionar_reservaciones():
    """
    Consulta y devuelve todos las reservaciones de la tabla reservaciones.

    Returns:
        list: Una lista de tuplas con los datos de las reservaciones, o lista vacía si hay error.
    """
    try:
        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM reservaciones;")
            reservaciones = cursor.fetchall()
            return reservaciones
    except Error as e:
        print(f"Error al obtener las reservaciones: {e}")
        return []
    except:
        print(f"Ocurrio un error inesperado de tipo: {sys.exc_info()[0]}")
        return []
    finally:
        if conn:
            conn.close()

def mostrar_clientes():
    """
    Obtiene y muestra en una tabla formateada la lista de clientes registrados,
    ordenados por apellidos.
    """
    clientes=selccionar_clientes_registrados()
    if clientes:
        print(f"{'*'*60}\n")
        print("Lista de clientes registrados:\n")
        print(tabulate(clientes, headers=["ID Cliente", "Nombre Cliente", "Apellidos Cliente"], tablefmt="fancy_grid"))
        print(f"{'-'*60}\n")
    else:
        print("No hay clientes registrados.")

def buscar_salon_por_id(id_salon):
    """
    Busca y devuelve los datos de un salón específico por su ID.

    Args:
        id_salon (str or int): El ID del salón a buscar.

    Returns:
        tuple: Los datos del salón si se encuentra, o None si no existe o hay error.
    """
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
    """
    Busca y devuelve los datos de un cliente específico por su ID.

    Args:
        id_cliente (str or int): El ID del cliente a buscar.

    Returns:
        tuple: Los datos del cliente si se encuentra, o None si no existe o hay error.
    """
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
    """
    Convierte una cadena de texto (formato MM-DD-YYYY) a un objeto date.

    Args:
        fecha_str (str): La fecha en formato "MM-DD-YYYY".

    Returns:
        datetime.date: El objeto date si la conversión es exitosa, o None si el formato es incorrecto.
    """
    try:
        fecha_date = datetime.strptime(fecha_str, "%m-%d-%Y").date()
        return fecha_date
    except ValueError:
        print(f"{'*'*60}\n")
        print("Formato de fecha incorrecto. Usa MM-DD-YYYY.\n")
        print(f"{'-'*60}\n")
        return None
    

def mostrar_disponibilidad_de_salon_por_fecha(fecha_iso):
    """
    Consulta y muestra una tabla con la disponibilidad de todos los salones
    para una fecha específica, indicando qué turnos están libres u ocupados.

    Args:
        fecha_iso (str): La fecha a consultar (formato "MM-DD-YYYY").

    Returns:
        list: Los resultados crudos de la consulta (incluyendo disponibilidad)
              o None si no hay salones o hay un error.
    """
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
            AND r.estado_reservacion = 'Activa'
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
    finally:
        if conn:
            conn.close()

def insertar_reservacion(id_cliente, nombre_cliente, nombre_evento, id_salon, nombre_salon, fecha_reservacion, turno):
    """
    Inserta una nueva reservación en la tabla 'reservaciones'.
    Maneja errores de integridad (ej. duplicados).

    Args:
        id_cliente (int): ID del cliente.
        nombre_cliente (str): Nombre del cliente.
        nombre_evento (str): Nombre del evento.
        id_salon (int): ID del salón.
        nombre_salon (str): Nombre del salón.
        fecha_reservacion (str): Fecha (MM-DD-YYYY).
        turno (str): Turno ('Matutino', 'Vespertino', 'Nocturno').
    """
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

def consultar_reservaciones_por_fecha():
    """
    Consulta y muestra reservaciones activas por fecha.

    Funcionalidad:
    - Formato fecha: MM-DD-YYYY (usa fecha actual si no se especifica)
    - Muestra reporte tabular ordenado por salón y turno
    - Permite exportar a JSON
    """
    reservaciones=selccionar_reservaciones()
    if reservaciones:
        pass
    else:
        print(f"{'*'*60}\n")
        print("No hay reservaciones registradas.\n")
        return
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
                id_salon, nombre_salon, fecha_reservacion, turno, estado_reservacion
                FROM reservaciones
                WHERE fecha_reservacion = ? AND estado_reservacion = 'Activa'
                ORDER BY id_salon, turno;
            """, (fecha_entrada,))
            filas = cursor.fetchall()
    except Error as e:
        print(f"Error al consultar la base de datos: {e}")
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
        id_salon, nombre_salon, fecha_reservacion, turno, estado_reservacion) = fila

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
            "Turno": turno,
            "Estado_Reservacion": estado_reservacion
        })

    tbl_formato_correcto=tabulate(
        tabla_para_mostrar,
        headers=["Sala","Cliente","Evento","Turno"],
        tablefmt="simple"
    )
    
    print(tbl_formato_correcto.replace("-", "*"))

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
    """
    Modifica el nombre de un evento en una reservación activa.

    Proceso:
    - Busca eventos por rango de fechas
    - Permite selección por folio
    - Actualiza nombre en base de datos

    Validaciones: formato fecha, existencia del evento, nombre válido
    """
    try:
        reservaciones=selccionar_reservaciones()
        if reservaciones:
            pass
        else:
            print(f"{'*'*60}\n")
            print("No hay reservaciones registradas.\n")
            return
        print(f"{'*'*60}")
        print("Vamos a editar el nombre de una reservación")
        print(f"{'-'*60}\n")    
        while True:
            fecha_inicio_str = input("Ingresa la fecha de inicio (MM-DD-YYYY): ").strip()
            fecha_fin_str = input("Ingresa la fecha de fin (MM-DD-YYYY): ").strip()

            if fecha_inicio_str == "" or fecha_fin_str == "":
                print("No se permite dejar el rango de fechas vacío.")
                return

            try:
                fecha_inicio = datetime.strptime(fecha_inicio_str, "%m-%d-%Y")
                fecha_fin = datetime.strptime(fecha_fin_str, "%m-%d-%Y")
                break
            except ValueError:
                print("Formato de fecha inválido. Usa MM-DD-YYYY.")
                continue

        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id_reservacion, nombre_evento, fecha_reservacion
                FROM reservaciones
                WHERE fecha_reservacion BETWEEN ? AND ? AND estado_reservacion = 'Activa'
                ORDER BY id_reservacion;
            """, (fecha_inicio_str, fecha_fin_str))
            eventos = cursor.fetchall()

        if not eventos:
            print("No hay eventos registrados en ese rango de fechas.")
            return

        print(tabulate(eventos, headers=["Folio", "Nombre Evento", "Fecha"], tablefmt="fancy_grid"))

        while True:
            folio_str = input("\nIngresa el folio del evento a modificar o Enter para cancelar: ").strip()
            if folio_str == "":
                print(f"{'*'*60}\n")
                print("Operación cancelada por el usario.\n")
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
                WHERE id_reservacion = ? AND estado_reservacion = 'Activa';
            """, (nuevo_nombre, folio))
            conn.commit()
        print(f"\nEvento actualizado exitosamente a: {nuevo_nombre}")
    except sqlite3.Error as e:
        print(f"Error al acceder a la base de datos: {e}")
    except Exception:
        print(f"Ocurrió un error inesperado: {sys.exc_info()[0]}")    

def registrar_reservacion():
    """
    Gestiona el registro de una nueva reservación.

    Validaciones principales:
    - Existencia de clientes y salones
    - Fecha futura (mínimo 2 días)
    - No reservaciones en domingo
    - Disponibilidad de salón y turno
    """
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
        id_salon = input("Escribe el id del salon o enter para cancelar la operacion: ").strip()
        if id_salon == "":
            print(f"{'*'*60}\n")
            print("Operación de reservacion cancelada por el usuario.\n")
            return None
        
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

def actualizar_estado_reservacion():
    """
    Cancela una reservación existente.

    Requisitos:
    - Cancelación con 2 días de anticipación
    - Selección por rango de fechas y folio
    - Confirmación explícita
    - Solo reservaciones activas
    """
    try:
        reservaciones=selccionar_reservaciones()
        if reservaciones:
            pass
        else:
            print(f"{'*'*60}\n")
            print("No hay reservaciones registradas.\n")
            return
        print(f"{'*'*60}")
        print("Vamos a cancelar una reservación")
        print(f"{'-'*60}\n")
        while True:
            fecha_inicio_str = input("Ingresa la fecha de inicio (MM-DD-YYYY): ").strip()
            fecha_fin_str = input("Ingresa la fecha de fin (MM-DD-YYYY): ").strip()

            if fecha_inicio_str == "" or fecha_fin_str == "":
                print(f"{'*'*60}\n")
                print("No se permite dejar el rango de fechas vacío.\n")
                return

            try:
                fecha_inicio = datetime.strptime(fecha_inicio_str, "%m-%d-%Y").date()
                fecha_actual = datetime.today().date()
                diferencia = (fecha_inicio - fecha_actual).days
                if diferencia < 2:
                    print(f"{'*'*60}\n")
                    print("Error: No puedes cancelar la reservación, debe ser con dos días de anticipación!\n")
                    return
                fecha_fin = datetime.strptime(fecha_fin_str, "%m-%d-%Y").date()
            except ValueError:
                print(f"{'*'*60}\n")
                print("\tFormato de fecha inválido. Usa MM-DD-YYYY.\n")
                print(f"{'*'*60}\n")
                continue

            if fecha_inicio == "" or fecha_fin == "":
                print("No se permite dejar el rango de fechas vacío.")
                continue
            else:
                break

        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id_reservacion, nombre_evento, fecha_reservacion
                FROM reservaciones
                WHERE fecha_reservacion BETWEEN ? AND ? AND estado_reservacion = 'Activa'
                ORDER BY id_reservacion;
            """, (fecha_inicio_str, fecha_fin_str))
            eventos = cursor.fetchall()

        if eventos:
            pass
        else:
            print(f"{'*'*60}\n")
            print("No hay eventos registrados en ese rango de fechas.\n")
            return

        print(tabulate(eventos, headers=["Folio", "Nombre Evento", "Fecha"], tablefmt="fancy_grid"))

        while True:
            folio_str = input("\nIngresa el folio del evento a cancelar o Enter para cancelar la operacion: ").strip()
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
            print(tabulate([evento_seleccionado], headers=["Folio", "Nombre Evento", "Fecha"], tablefmt="fancy_grid"))
            cancelar = input(f"Quieres cancelar el evento '{evento_seleccionado[1]}? (s/n)': ").strip().upper()
            if cancelar == "":
                print("\nRespuesta no puede estar vacia. Intenta de nuevo.\n")
            elif cancelar.isdigit():
                print("\nEl nombre del evento no puede contener solo números. Intenta de nuevo.\n")
            elif cancelar not in ['S', 'N']:
                print("\nRespuesta inválida. Debe ser 's' o 'n'. Intenta de nuevo.\n")
            elif cancelar == 'S':
                break
            else:
                print("Operación de cancelación abortada por el usuario.")
                print(f"{'-'*60}\n")
                return   

        with sqlite3.connect("reservaciones.db") as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE reservaciones
                SET estado_reservacion = ?
                WHERE id_reservacion = ? AND estado_reservacion = 'Activa';
            """, ('Cancelada', folio))
            conn.commit()

        print(f"\nEvento cancelado exitosamente: {evento_seleccionado[1]}")
    except Error as e:
        print(f"Error al acceder a la base de datos: {e}")
    except Exception:
        print(f"Ocurrió un error inesperado: {sys.exc_info()[0]}")
            
def main():
    """
    Punto de entrada principal del sistema de reservaciones.
    
    Menú: Reservar, Editar, Consultar, Cancelar, 
          Registrar Cliente/Salón, Salir
    """
    inicializar_base_de_datos()
    while True:
        print(f"{'*'*60}")
        print("Sistema para el registro de salas de coworking\n")
        print(f"{'-'*60}\n")
        print("1. Hacer una reservacion")
        print("2. Editar nombre de reservacion")
        print("3. Consultar reservaciones por fecha")
        print("4. Cancelar una reservacion")
        print("5. Registrar un nuevo cliente")
        print("6. Registrar un nuevo salon")
        print("7. Salir\n")
        
        opcion = input("Que opcion eliges? ")
        if opcion == "7":
            print("saliendo del sistema...")
            break
        elif opcion == "1":
            registrar_reservacion()
        elif opcion == "2":
            editar_nombre_reservacion()
        elif opcion == "3":
            consultar_reservaciones_por_fecha()
        elif opcion == "4":
            actualizar_estado_reservacion()
        elif opcion == "5":
            registrar_cliente()
        elif opcion == "6":
            registrar_salon()
        else:
            print("Opcion invalida. Intenta de nuevo.\n")


if __name__ == "__main__":
    main()