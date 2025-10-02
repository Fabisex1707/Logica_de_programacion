from tabulate import tabulate
import datetime

def convertir_str_a_date():
    """
    Solicita al usuario una fecha en formato DD/MM/YYYY y la convierte a un objeto date.
    Si el usuario presiona Enter sin escribir nada, retorna False para cancelar la operación.
    """
    while True:
        str_fecha_evento = input("Escribe la fecha de tu evento (DD/MM/YYYY) o [Enter] para cancelar la operacion: ")
        if str_fecha_evento.strip() == '':
            return False
        try:
            fecha_reservacion = datetime.datetime.strptime(str_fecha_evento, "%d/%m/%Y").date()
            return fecha_reservacion
        except:
            print("El formato de la fecha es invalido, digitela de nuevo!")
            continue

def registrar_cliente(diccionario_cliente: dict):
    """
    Registra un nuevo cliente en el diccionario de clientes.
    Valida que el nombre y apellidos no estén vacíos y no contengan números.
    """
    while True:
        
        nombre = input("Dame un nombre o nombres a registrar: ").strip().capitalize()
        apellido = input("Dame tus apellidos a registrar: ").strip().capitalize()

        if nombre.strip()=='' or (not (all(letra.isalpha() or letra.isspace() for letra in nombre.upper()))):
            print("No se puede poner el nombre(s) en blanco o con numeros!")
            continue
        elif apellido.strip()=='' or (not (all(letra.isalpha() or letra.isspace() for letra in apellido.upper()))):
            print("No se puede poner el Apellido(s) en blanco o con numeros!")
            continue

        id = max(diccionario_cliente.keys(), default= 0) +1
        diccionario_cliente[id] = {
        "Nombre": nombre,
        "Apellidos": apellido
        }
        print("Se ha registrado correctamente al cliente.\n")
        mostrar_datos_clientes(diccionario_cliente)
        break


def registrar_salon(diccionario_salones: dict):
    """
    Registra un nuevo salón en el diccionario de salones.
    Solicita nombre, cupo y disponibilidad de turnos, valida los datos y agrega el salón.
    """
    while True:
        nombre_salon = input("\nEscribe el nombre del salón a registrar o [Enter] para cancelar: ").strip()
        if not nombre_salon:
            print("\n--AVISO: Operación cancelada.--")
            break
        elif nombre_salon.strip()=='' or (not (all(letra.isalpha() or letra.isspace() for letra in nombre_salon.upper()))):
            print("El nombre del salon solo debe contener letras!")
            continue

        cupo_str = input(f"Escribe el cupo para el salón '{nombre_salon}': ").strip()
        if not cupo_str.isdigit() or int(cupo_str) <= 0:
            print("\nError: El cupo debe ser un número entero y mayor que cero.")
            print(f"{'-'*60}")
            continue
            
        cupo = int(cupo_str)

            # Solicita la disponibilidad de cada turno
        print("\nAhora define la disponibilidad de los turnos:")
        turnos_disponibles = {}
        for turno in ["Matutino", "Vespertino", "Nocturno"]:
            while True:
                respuesta = input(f"¿El turno {turno} estará disponible? (1: Sí / 2: No): ").strip()
                if respuesta == '1':
                    turnos_disponibles[turno] = True
                    break
                elif respuesta == '2':
                    turnos_disponibles[turno] = False
                    break
                else:
                    print("Error: Por favor, introduce solo '1' para Sí o '2' para No.")
            
            # Genera un nuevo ID para el salón y lo agrega al diccionario
        id_salon = max(diccionario_salones.keys(), default=0) + 1
        diccionario_salones[id_salon] = {
            "Nombre_salon": nombre_salon,
            "Cupo": cupo,
            "Turno": turnos_disponibles
        }

        print(f"\n¡El salón '{nombre_salon}' se ha registrado correctamente con el ID {id_salon}!")
        mostrar_datos_salon(diccionario_salones)

        continuar = input("¿Deseas registrar otro salón? (1: Sí / Otro: No): ")
        if continuar != '1':
            break

def mostrar_datos_clientes(diccionario_clientes: dict):
    """
    Muestra todos los clientes registrados en formato de tabla ordenada por apellidos.
    """
    lista_clientes_con_orden = []
    for id_cliente, datos in diccionario_clientes.items():
        lista_clientes_con_orden.append([datos["Apellidos"], datos["Nombre"], id_cliente])
    lista_clientes_con_orden.sort(key=lambda index_lista: index_lista[0])
    print(tabulate(lista_clientes_con_orden, headers=["Apellidos", "Nombre Cliente", "Id Cliente"], tablefmt="fancy_grid"))

def estado_turno(valor: bool):
    """
    Devuelve 'Disponible' si el valor es True, de lo contrario 'No disponible'.
    """
    return "Disponible" if valor else "No disponible"

def mostrar_datos_salon(diccionario_salones: dict):
    """
    Muestra todos los salones registrados en formato de tabla, incluyendo el estado de cada turno.
    """
    lista_salas_con_orden = []
    for id_sala, datos in diccionario_salones.items():
        lista_salas_con_orden.append([
            id_sala,
            datos["Nombre_salon"],
            datos["Cupo"],
            estado_turno(datos["Turno"]["Matutino"]),
            estado_turno(datos["Turno"]["Vespertino"]),
            estado_turno(datos["Turno"]["Nocturno"])
        ])
    lista_salas_con_orden.sort(key=lambda index_lista: index_lista[0])
    print(tabulate(lista_salas_con_orden, headers=["Id de la sala", "Nombre de la sala", "Cupo", "Turno matutino", "Turno Vespertino", "Turno Nocturno"], tablefmt="fancy_grid"))

def buscar_cliente(diccionario_clientes: dict):
    """
    Permite buscar y seleccionar un cliente por su ID.
    Si el cliente no existe, da la opción de salir o volver a intentar.
    """
    while True:
        mostrar_datos_clientes(diccionario_clientes)
        try:
            id_cliente_registrado = int(input("Escribe tu numero de cliente: "))
        except:
            print("\nDebes de ingresar un numero entero!")
            print(f"\n{'-'*60}")
            continue

        if id_cliente_registrado not in diccionario_clientes.keys():
            print("Ese usuario no esta registrado!\n")
            salir = input("Quieres salir? 1.SI | 2.No: ")
            print(f"\n{'-'*60}")
            if salir != "2":
                return False
        else:
            return (id_cliente_registrado, diccionario_clientes[id_cliente_registrado]["Nombre"], diccionario_clientes[id_cliente_registrado]["Apellidos"])

def buscar_salon(diccionario_salones: dict):
    """
    Permite buscar y seleccionar un salón por su ID.
    Si el salón no existe, da la opción de salir o volver a intentar.
    """
    while True:
        mostrar_datos_salon(diccionario_salones)
        try:
            id_salon_registrado = int(input("Escribe el id del salon que quiere reservar: "))
        except:
            print("\nDebes de ingresar un numero entero!")
            print(f"\n{'-'*60}")
            continue

        if id_salon_registrado not in diccionario_salones.keys():
            print("Ese salon no esta registrado!\n")
            salir = input("Quieres salir? 1.SI | 2.No: ")
            print(f"\n{'-'*60}")
            if salir != "2":
                return False
        else:
            datos = diccionario_salones[id_salon_registrado]
            return (
                id_salon_registrado,
                datos["Nombre_salon"],
                datos["Cupo"],
                datos["Turno"]["Matutino"],
                datos["Turno"]["Vespertino"],
                datos["Turno"]["Nocturno"]
            )
        
def consultar_reservaciones_por_fecha(reservaciones: dict):
    """
    Consulta y muestra todas las reservaciones dentro de un rango de fechas en formato de tabla.
    Si no hay reservaciones en ese rango, muestra un mensaje.
    Valida el formato de las fechas ingresadas por el usuario.
    """
    if not reservaciones:
        print("No hay reservaciones registradas.")
        return
    while True:
        fecha_inicio = input("Fecha inicial (DD/MM/YYYY): ")
        fecha_fin = input("Fecha final (DD/MM/YYYY): ")
        try:
            fecha_inicio_dt = datetime.datetime.strptime(fecha_inicio, "%d/%m/%Y").date()
            fecha_fin_dt = datetime.datetime.strptime(fecha_fin, "%d/%m/%Y").date()
            if fecha_inicio_dt > fecha_fin_dt:
                print("La fecha inicial no puede ser mayor que la fecha final.")
                continue
            break
        except ValueError:
            print("Formato de fecha inválido. Intenta de nuevo (DD/MM/YYYY).")
            continue

    lista = []
    for datos in reservaciones.values():
        try:
            fecha_r = datetime.datetime.strptime(datos["fecha_reservacion"], "%d/%m/%Y").date()
        except:
            continue
        if fecha_inicio_dt <= fecha_r <= fecha_fin_dt:
            lista.append([
                datos["id_sala"],
                datos["nombre_cliente"],
                datos["nombre_evento"],
                datos["fecha_reservacion"],
                datos["turno"].upper()
            ])
    print("\n" + "*"*70)
    print(f"** REPORTE DE RESERVACIONES DEL {fecha_inicio} AL {fecha_fin} **")
    print("*"*70)
    if lista:
        print(tabulate(lista, headers=["SALA", "CLIENTE", "EVENTO", "FECHA", "TURNO"], tablefmt="fancy_grid"))
    else:
        print("No hay reservaciones en ese rango de fechas.")
    print("*"*70)
    print("*************** FIN DEL REPORTE ***************\n")
    """
    Consulta y muestra todas las reservaciones para una fecha específica en formato de tabla.
    Si no hay reservaciones para esa fecha, muestra un mensaje.
    """
    if not reservaciones:
        print("No hay reservaciones registradas.")
        return
    fecha = input("¿Para qué fecha deseas consultar las reservaciones? (DD/MM/YYYY): ")
    lista = []
    for datos in reservaciones.values():
        if datos["fecha_reservacion"] == fecha:
            lista.append([
                datos["id_sala"],
                datos["nombre_cliente"],
                datos["nombre_evento"],
                datos["turno"].upper()
            ])
    print("\n" + "*"*70)
    print(f"**      REPORTE DE RESERVACIONES PARA EL DÍA {fecha}      **")
    print("*"*70)
    if lista:
        print(tabulate(lista, headers=["SALA", "CLIENTE", "EVENTO", "TURNO"], tablefmt="fancy_grid"))
    else:
        print("No hay reservaciones para esa fecha o la reservación no existe.")
    print("*"*70)
    print("*************** FIN DEL REPORTE ***************\n")

def editar_nombre_reservacion(reservaciones: dict):
    """
    Permite editar el nombre del evento de una reservación existente.
    El usuario debe indicar un rango de fechas para buscar reservaciones.
    Se muestran las reservaciones encontradas y el usuario elige el folio a editar.
    """
    if not reservaciones:
        print("No hay reservaciones registradas.")
        return
    print("Editar nombre de reservación")
    fecha_inicio = input("Fecha inicial (DD/MM/YYYY): ")
    fecha_fin = input("Fecha final (DD/MM/YYYY): ")
    try:
        fecha_inicio_dt = datetime.datetime.strptime(fecha_inicio, "%d/%m/%Y").date()
        fecha_fin_dt = datetime.datetime.strptime(fecha_fin, "%d/%m/%Y").date()
    except:
        print("Formato de fecha inválido.")
        return

    eventos = []
    for folio, r in reservaciones.items():
        try:
            fecha_r = datetime.datetime.strptime(r["fecha_reservacion"], "%d/%m/%Y").date()
        except:
            continue
        if fecha_inicio_dt <= fecha_r <= fecha_fin_dt:
            eventos.append((folio, r))

    if not eventos:
        print("No hay reservaciones en ese rango.")
        return

    tabla = [[folio, r["nombre_evento"], r["fecha_reservacion"], r["turno"]] for folio, r in eventos]
    print(tabulate(tabla, headers=["Folio", "Evento", "Fecha", "Turno"], tablefmt="fancy_grid"))

    while True:
        try:
            folio = int(input("Ingresa el folio a editar o Enter para cancelar: ") or 0)
        except:
            print("Folio inválido.")
            return
        seleccionado = None
        for f, r in eventos:
            if f == folio:
                seleccionado = r
                break
        if seleccionado:
            break
        else:
            print("Folio inválido.")
            return

    while True:
        nuevo_nombre = input("Nuevo nombre del evento: ").strip()
        if nuevo_nombre != "" and (not nuevo_nombre.isdigit()):
            seleccionado["nombre_evento"] = nuevo_nombre
            print("Evento actualizado.")
            return
        print("El nombre no puede estar vacío.")

def agregar_reservacion(clientes, salones, reservaciones, id_reservaciones_contador):
    usuario_encontrado = buscar_cliente(clientes)
    if not usuario_encontrado:
        print("Error: La operacion se cancelo! volviendo al menu principal...")
        return id_reservaciones_contador

    while True:
        print(f"\nBienvenido {usuario_encontrado[1]} {usuario_encontrado[2]}")
        fecha_reservacion = convertir_str_a_date()
        if not fecha_reservacion:
            print(f"{'-'*60}\n")
            print("--AVISO: Operación cancelada!, volviendo al menú principal...--")
            print(f"\n{'-'*60}")
            break
        fecha_actual = datetime.datetime.today().date()
        diferencia = (fecha_reservacion - fecha_actual).days
        if diferencia < 2:
            print("Error: No puedes hacer tu reservación, debe ser con dos días de anticipación!\n")
            continue

        print("\nFecha aceptada!, ahora vamos a elegir el salón\n")
        salon_encontrado = buscar_salon(salones)
        if not salon_encontrado:
            print("Error: Ese salón no esta registrado!, volviendo al menú de registro de sala...")
            print(f"\n{'-'*60}")
            continue
        print("\nId de salón aceptado!, ahora vamos a elegir el turno\n")
        while True:
            turno = input("Elige turno (Matutino / Vespertino / Nocturno): ").strip().capitalize()
            if turno not in ["Matutino", "Vespertino", "Nocturno"]:
                print("Turno inválido, intenta de nuevo.")
                continue
            break

        ocupado = False
        for r in reservaciones.values():
            if (r["id_sala"] == salon_encontrado[0] and
                r["fecha_reservacion"] == fecha_reservacion.strftime("%d/%m/%Y") and
                r["turno"] == turno):
                ocupado = True
                break

        if ocupado:
            print("Ese turno ya está reservado en esa sala para esa fecha.")
            continue

        while True:
            nombre_evento = input("Escribe el nombre del evento: ").strip()
            if nombre_evento == "" or nombre_evento.isdigit():
                print("El nombre no puede estar vacío. Intenta de nuevo.")
                continue
            break

        folio = id_reservaciones_contador
        reservaciones[folio] = {
            "id_cliente": usuario_encontrado[0],
            "nombre_cliente": f"{usuario_encontrado[1]} {usuario_encontrado[2]}",
            "nombre_evento": nombre_evento,
            "id_sala": salon_encontrado[0],
            "nombre_salon": salon_encontrado[1],
            "fecha_reservacion": fecha_reservacion.strftime("%d/%m/%Y"),
            "turno": turno
        }

        id_reservaciones_contador += 1

        print(f"\nReservación registrada con éxito. Folio: {folio}\n")
        print("-" * 60)
        break

    return id_reservaciones_contador

def main():
    """
    Función principal que muestra el menú y gestiona el flujo del sistema de reservaciones.
    """
    id_reservaciones_contador = 2
    clientes = {
        1: {"Nombre": "Fabian", "Apellidos": "Santana Dolores"},
        2: {"Nombre": "Carlos", "Apellidos": "Hernandez Casas"},
        3: {"Nombre": "Alvaro", "Apellidos": "Salazar  Gonzalez"}
    }
    salones = {
        1: {"Nombre_salon": "Treviño Hernandez", "Cupo": 300, "Turno": {"Matutino": True, "Vespertino": True, "Nocturno": True}},
        2: {"Nombre_salon": "Emiliano Zapata", "Cupo": 200, "Turno": {"Matutino": True, "Vespertino": True, "Nocturno": True}}
    }
    reservaciones = {
        1: {"id_cliente": 1, "nombre_cliente": "Fabian Zantana Dolores", "nombre_evento": "Coferencia sobre ciber seguridad", "id_sala": 1, "nombre_salon": "Treviño Hernandez", "fecha_reservacion": "12/09/2026", "turno": "Vespertino"}
    }
    while True:
        print(f"{'-'*10} Sistema para el registro de salas de coworking {'-'*10}\n")
        print("Bienvenido al menu de opciones...\n")
        print("1. Reservar una sala")
        print("2. Editar el nombre de la reservacion")
        print("3. Consultar reservaciones")
        print("4. Registrar un cliente")
        print("5. Registrar una sala")
        print("6. Salir")
        op = input("Que opcion eliges? ")

        if op == "6":
            print("Saliendo del sistema...")
            break
        elif op == "1":
            id_reservaciones_contador = agregar_reservacion(clientes, salones, reservaciones, id_reservaciones_contador)
        elif op == "2":
            editar_nombre_reservacion(reservaciones)
        elif op == "3":
            consultar_reservaciones_por_fecha(reservaciones)
        elif op == "4":
            registrar_cliente(clientes)
        elif op== "5":
            registrar_salon(salones)
        else:
            print("\nEsa opción no existe!\n")
            continue

if __name__ == "__main__":
    main()