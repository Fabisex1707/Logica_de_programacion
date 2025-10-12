from tabulate import tabulate
import datetime
import json
import os

ARCHIVO_REGISTRO = "Registro_Acabado.json"

def cargar_estado_inicial():
    """
    Carga el estado guardado anteriormente desde el archivo JSON.
    Si no existe, retorna diccionarios vacíos e informa al usuario.
    """
    print("\n" + "="*70)
    print(" "*15 + "SISTEMA DE RESERVACIONES DE SALAS")
    print("="*70)
    print(" Buscando registros anteriores...")
    
    if os.path.exists(ARCHIVO_REGISTRO):
        try:
            with open(ARCHIVO_REGISTRO, 'r') as archivo:
                estado = json.load(archivo)
            
            clientes = {int(id_clientes): datos_clientes for id_clientes, datos_clientes in estado.get("clientes", {}).items()}
            salones = {int(id_salones): datos_salones for id_salones, datos_salones in estado.get("salones", {}).items()}
            reservaciones = {int(id_reservaciones): datos_reservaciones for id_reservaciones, datos_reservaciones in estado.get("reservaciones", {}).items()}
            
            print("Datos anteriores encontrados y cargados exitosamente")
            print("="*70 + "\n")
            
            return clientes, salones, reservaciones
            
        except json.JSONDecodeError:
            print("El archivo existe pero está corrupto.")
            print("Iniciando con registros vacíos...")
            print("="*70 + "\n")
            return {}, {}, {}
        
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            print("Iniciando con registros vacíos...")
            print("="*70 + "\n")
            return {}, {}, {}
    
    else:
        print("No se encontraron registros anteriores.")
        print("Iniciando con registros vacíos...")
        print("="*70 + "\n")
        return {}, {}, {}

def guardar_estado_final(clientes, salones, reservaciones):
    """
    Guarda todos los datos en el archivo JSON antes de salir del programa.
    """
    print("\n" + "="*70)
    print("SALIENDO DEL SISTEMA...")
    print("="*70)
    guardar = input("¿Desea guardar los cambios antes de salir? (s/n): ").lower().strip()
            
    if guardar == 's':
            try:
                estado = {
                    "clientes": clientes,
                    "salones": salones,
                    "reservaciones": reservaciones
                }
                
                with open(ARCHIVO_REGISTRO, 'w') as archivo:
                    json.dump(estado, archivo, indent=4, ensure_ascii=False)
                
                print("\n" + "="*70)
                print("GUARDANDO ESTADO DEL SISTEMA...")
                print("="*70)
                print(f"Datos guardados exitosamente en '{ARCHIVO_REGISTRO}'")
                print("="*70)
                print("\n Saliendio ...\n")
                return True
                
            except Exception as e:
                print(f"\n Error al guardar datos: {e}")
                print(" Los cambios NO se guardaron.\n")
                return False
    elif guardar == 'n':
        print("\n  Los cambios NO se guardaron.")
    return False

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
        print("\n--Se ha registrado correctamente al cliente.--\n")
        mostrar_datos_clientes(diccionario_cliente)
        break


def registrar_salon(diccionario_salones: dict):
    """
    Registra un nuevo salón en el diccionario de salones.
    Solicita nombre, cupo y disponibilidad de turnos, valida los datos y agrega el salón.
    """
    while True:
        print(f"\n{'*'*70}")
        print("\tVamos a registrar una sala nueva.")
        print(f"{'*'*70}\n")
        nombre_salon = input("\nEscribe el nombre del salón a registrar o [Enter] para cancelar: ").strip().upper()
        if nombre_salon:
            if nombre_salon.strip()=='' or (not (all(letra.isalpha() or letra.isspace() for letra in nombre_salon))):
                print("El nombre del salon solo debe contener letras!\n")
                continue

            cupo_str = input(f"Escribe el cupo para el salón '{nombre_salon}': ").strip()   
            try:
                cupo = int(cupo_str)
            except:
                print(f"\n{'*'*70}")
                print("--ERROR: Debes escribir solo numero enteros.--")
                print(f"{'*'*70}\n")
                continue
                
            # Genera un nuevo ID para el salón y lo agrega al diccionario
            id_salon = max(diccionario_salones.keys(), default=0) + 1
            diccionario_salones[id_salon] = {
                "Nombre_salon": nombre_salon,
                "Cupo": cupo,
                "Turno": {"Matutino": True, "Vespertino": True, "Nocturno": True}
            }
            print(f"\n{'*'*70}")
            print(f"¡El salón '{nombre_salon}' se ha registrado correctamente con el ID {id_salon}!")
            print(f"{'*'*70}\n")
            mostrar_datos_salon(diccionario_salones)
            print(f"{'-'*70}\n")
        else:
            print(f"\n{'*'*70}")
            print("\t--AVISO: Operación cancelada, volviendo al menu principal.--")
            print(f"{'*'*70}\n")
            break

def mostrar_datos_clientes(diccionario_clientes: dict):
    """
    Muestra todos los clientes registrados en formato de tabla ordenada por apellidos.
    """
    if diccionario_clientes:
        lista_clientes_con_orden = []
        for id_cliente, datos in diccionario_clientes.items():
            lista_clientes_con_orden.append([datos["Apellidos"], datos["Nombre"], id_cliente])
        lista_clientes_con_orden.sort(key=lambda index_lista: index_lista[0])
        print(tabulate(lista_clientes_con_orden, headers=["Apellidos", "Nombre Cliente", "Id Cliente"], tablefmt="fancy_grid"))
        return True
    else:
        print(f"\n{'*'*70}")
        print("\t--AVISO: No hay clientes aun.--")
        print(f"{'*'*70}\n")
        return False

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
    return diccionario_salones

def mostrar_datos_salon_disponible_para_una_fecha(fecha_de_reservacion_dt: str, diccionario_salones: dict, diccionario_reservaciones: dict):
    """
    Muestra salones indicando qué turnos están ocupados para la fecha indicada.
    No modifica diccionario_salones original.
    """
    # normalizar fecha a objeto date si viene como string
    if isinstance(fecha_de_reservacion_dt, datetime.date):
        fecha_dt = fecha_de_reservacion_dt
    else:
        try:
            fecha_dt = datetime.datetime.strptime(str(fecha_de_reservacion_dt), "%d/%m/%Y").date()
        except:
            print("Fecha inválida.")
            return None

    # construir mapping id_sala -> set(turnos) reservados en esa fecha
    reservados_por_sala = {}
    for folio, datos_r in diccionario_reservaciones.items():
        try:
            fr = datetime.datetime.strptime(datos_r.get("fecha_reservacion", ""), "%d/%m/%Y").date()
        except:
            continue
        if fr == fecha_dt:
            id_sala = datos_r.get("id_sala")
            turno = datos_r.get("turno", "").capitalize()
            if id_sala is None or turno == "":
                continue
            reservados_por_sala.setdefault(id_sala, set()).add(turno)

    # si no hay reservaciones para la fecha, mostrar todos los salones tal cual
    if not reservados_por_sala:
        print("\n--No hay salones reservados para esa fecha, mostrando todos los salones disponibles.--\n")
        mostrar_datos_salon(diccionario_salones)
        return diccionario_salones

    # construir tabla sin mutar el diccionario original
    lista_salas_con_orden = []
    salas_con_turnos_ocupados = {}
    for id_sala, datos in diccionario_salones.items():
        reservados = reservados_por_sala.get(id_sala, set())
        mat = False if "Matutino" in reservados else datos["Turno"].get("Matutino", False)
        ves = False if "Vespertino" in reservados else datos["Turno"].get("Vespertino", False)
        noc = False if "Nocturno" in reservados else datos["Turno"].get("Nocturno", False)

        lista_salas_con_orden.append([
            id_sala,
            datos.get("Nombre_salon", ""),
            datos.get("Cupo", ""),
            estado_turno(mat),
            estado_turno(ves),
            estado_turno(noc)
        ])

        salas_con_turnos_ocupados[id_sala] = {
            "Nombre_salon": datos.get("Nombre_salon", ""),
            "Cupo": datos.get("Cupo", ""),
            "Turno": {
                "Matutino": mat,
                "Vespertino": ves,
                "Nocturno": noc
            }
        }
    lista_salas_con_orden.sort(key=lambda index_lista: index_lista[0])
    print(tabulate(lista_salas_con_orden, headers=["Id de la sala", "Nombre de la sala", "Cupo", "Turno matutino", "Turno Vespertino", "Turno Nocturno"], tablefmt="fancy_grid"))
    return salas_con_turnos_ocupados

def buscar_cliente(diccionario_clientes: dict):
    """
    Permite buscar y seleccionar un cliente por su ID.
    Si el cliente no existe, da la opción de salir o volver a intentar.
    """
    while True:
        if mostrar_datos_clientes(diccionario_clientes):
            try:
                id_cliente_registrado = int(input("Escribe tu numero de cliente: "))
            except:
                print("\nDebes de ingresar un numero entero!")
                print(f"\n{'-'*60}")
                continue

            if id_cliente_registrado not in diccionario_clientes.keys():
                print("\n--Ese usuario no esta registrado!--\n")
                salir = input("Quieres salir al menu principal? 1.SI | 2.No: ")
                print(f"\n{'-'*60}")
                if salir != "2":
                    print("AVISO: La operacion se cancelo! volviendo al menu principal...\n")
                    return False
            else:
                return (id_cliente_registrado, diccionario_clientes[id_cliente_registrado]["Nombre"], diccionario_clientes[id_cliente_registrado]["Apellidos"])
        else:
            return False


def buscar_salon(diccionario_salones: dict,):
    """
    Permite buscar y seleccionar un salón por su ID.
    Si el salón no existe, da la opción de salir o volver a intentar.
    """
    while True:
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
    Consulta y muestra todas las reservaciones para una fecha específica en formato de tabla.
    Pregunta al usuario si desea exportar los resultados a un archivo JSON.
    """
    if not reservaciones:
        print("No hay reservaciones registradas.")
        return
    while True:
        fecha = input("¿Para qué fecha deseas consultar la reservacion? (DD/MM/YYYY): ")
        try:
            fecha_dt = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
            fecha = fecha_dt.strftime("%d/%m/%Y")
            break
        except ValueError:
            print("Formato de fecha inválido. Intenta de nuevo (DD/MM/YYYY).")
            continue

    lista = []
    for datos in reservaciones.values():
        if datos["fecha_reservacion"] == fecha:
            lista.append({
                "SALA": datos["id_sala"],
                "CLIENTE": datos["nombre_cliente"],
                "EVENTO": datos["nombre_evento"],
                "FECHA": datos["fecha_reservacion"],
                "TURNO": datos["turno"].upper()
            })
    print("\n" + "*"*70)
    print(f"** REPORTE DE RESERVACIONES PARA EL DÍA {fecha} **")
    print("*"*70)
    if lista:
        print(tabulate(
            [[d["SALA"], d["CLIENTE"], d["EVENTO"], d["FECHA"], d["TURNO"]] for d in lista],
            headers=["SALA", "CLIENTE", "EVENTO", "FECHA", "TURNO"],
            tablefmt="fancy_grid"
        ))
        exportar = input("\n¿Desea exportar el reporte a JSON? (s/n): ").strip().lower()
        if exportar == "s":
            with open("reporte_reservaciones.json", "w") as f:
                json.dump(lista, f, ensure_ascii=False, indent=4)
            print("\nReporte exportado a 'reporte_reservaciones.json'.")
    else:
        print("No hay reservaciones para esa fecha.")
    print("*"*70)
    print("*************** FIN DEL REPORTE ***************\n")

def editar_nombre_reservacion(reservaciones: dict):
    """
    Permite editar el nombre del evento de una reservación existente, 
    el usuario debe indicar una fecha para buscar la reservacion.
    """
    if reservaciones:
        print(f"{'-'*70}")
        print("\tVamos a editar el nombre de una reservación")
        print(f"{'-'*70}\n")
        fecha_inicio = input("Fecha inicial (DD/MM/YYYY): ")
        fecha_fin = input("Fecha final (DD/MM/YYYY): ")
        try:
            fecha_inicio_dt = datetime.datetime.strptime(fecha_inicio, "%d/%m/%Y").date()
            fecha_fin_dt = datetime.datetime.strptime(fecha_fin, "%d/%m/%Y").date()
        except:
            print(f"{'*'*70}")
            print("--ERROR: Formato de fecha inválido.--")
            print(f"{'*'*70}\n")
            return None

        eventos = []
        for folio, datos_reservacion in reservaciones.items():
            try:
                fecha_r = datetime.datetime.strptime(datos_reservacion["fecha_reservacion"], "%d/%m/%Y").date()
            except:
                continue
            if fecha_inicio_dt <= fecha_r <= fecha_fin_dt:
                eventos.append((folio, datos_reservacion))

        if not eventos:
            print(f"{'*'*70}")
            print("--AVISO:No hay reservaciones en ese rango.--")
            print(f"{'*'*70}\n")
            return None

        tabla = [[folio, datos_reservacion["nombre_evento"], datos_reservacion["fecha_reservacion"], datos_reservacion["nombre_salon"], datos_reservacion["turno"]] for folio, datos_reservacion in eventos]
        print(tabulate(tabla, headers=["Folio", "Nombre del evento", "Fecha", "Nombre de la sala", "Turno"], tablefmt="fancy_grid"))

        # pedir folio hasta que sea válido o cancelar
        while True:
            folio_str = input("Ingresa el folio a editar o Enter para cancelar: ")
            if folio_str.strip() == "":
                print(f"{'-'*60}\n")
                print("--AVISO: Operación cancelada!, volviendo al menú principal...--")
                print(f"\n{'-'*60}\n")
                return None
            try:
                folio_sel = int(folio_str)
            except:
                print(f"{'*'*70}")
                print("--ERROR: Solo se admiten numeros enteros.--")
                print(f"{'*'*70}\n")
                print(tabulate(tabla, headers=["Folio", "Nombre del evento", "Fecha", "Nombre de la sala", "Turno"], tablefmt="fancy_grid"))
                continue

            seleccionado = next((datos for f, datos in eventos if f == folio_sel), None)
            if seleccionado is None:
                print(f"{'-'*60}\n")
                print("\t\t--Folio inválido.--")
                print(f"\n{'-'*60}\n")
                print(tabulate(tabla, headers=["Folio", "Nombre del evento", "Fecha", "Nombre de la sala", "Turno"], tablefmt="fancy_grid"))
                continue
            break

        # editar nombre
        while True:
            nuevo_nombre = input("Nuevo nombre del evento: ").strip()
            if nuevo_nombre == "" or nuevo_nombre.isdigit():
                print("El nombre no puede estar vacío o contener solo numeros.\n")
            else:
                seleccionado["nombre_evento"] = nuevo_nombre
                print("Evento actualizado.\n")
                print(f"{'-'*70}")
                return
    else:
        print("No hay reservaciones registradas.")
        return None

def agregar_reservacion(clientes, salones, reservaciones):
    usuario_encontrado = buscar_cliente(clientes)
    if usuario_encontrado:
        while True:
            print(f"\n{'*'*70}")
            print(f"\tBienvenido {usuario_encontrado[1]} {usuario_encontrado[2]}")
            print(f"{'*'*70}\n")
            fecha_reservacion = convertir_str_a_date()
            if fecha_reservacion:
                fecha_actual = datetime.datetime.today().date()
                diferencia = (fecha_reservacion - fecha_actual).days
                if diferencia < 2:
                    print("Error: No puedes hacer tu reservación, debe ser con dos días de anticipación!\n")
                    continue

                print("\n--Fecha aceptada!, ahora vamos a elegir el salón--\n")
                if reservaciones:
                    salones_reservados=mostrar_datos_salon_disponible_para_una_fecha(fecha_reservacion,salones,reservaciones)
                else:
                    salones_reservados=mostrar_datos_salon(salones)
                salon_encontrado = buscar_salon(salones)
                if salon_encontrado:
                    print("\nId de salón aceptado!, ahora vamos a elegir el turno\n")
                    while True:
                        turno = input("Elige turno (Matutino / Vespertino / Nocturno): ").strip().capitalize()
                        try:
                            if salones_reservados[salon_encontrado[0]]["Turno"][turno]:
                                print(f"\n{'*'*70}")
                                print("\t--Turno aceptado!--")
                                print(f"{'*'*70}\n")
                            else:
                                print(f"\n{'*'*70}")
                                print(f"--Error: El turno {turno} no está disponible en ese salón, elija otro por favor.--")
                                print(f"{'*'*70}\n")
                                continue
                        except KeyError:
                            print(f"Esa sala no maneja ese turno, elija otor por favor.\n")
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

                    folio = max(reservaciones.keys(), default=0) + 1
                    reservaciones[folio] = {
                        "id_cliente": usuario_encontrado[0],
                        "nombre_cliente": f"{usuario_encontrado[1]} {usuario_encontrado[2]}",
                        "nombre_evento": nombre_evento,
                        "id_sala": salon_encontrado[0],
                        "nombre_salon": salon_encontrado[1],
                        "fecha_reservacion": fecha_reservacion.strftime("%d/%m/%Y"),
                        "turno": turno
                    }

                    print(f"\nReservación registrada con éxito. Folio: {folio}\n")
                    print("-" * 60)
                    break
                else:
                    print("Error: Ese salón no esta registrado!, volviendo al menú de registro de sala...")
                    print(f"\n{'-'*60}")
                    continue
            else:
                print(f"{'-'*60}\n")
                print("--AVISO: Operación cancelada!, volviendo al menú principal...--")
                print(f"\n{'-'*60}")
                break
        return None
    else:
        return None

def main():
    """
    Función principal que muestra el menú y gestiona el flujo del sistema de reservaciones.
    Ahora incluye carga y guardado automático del estado.
    """
    clientes, salones, reservaciones = cargar_estado_inicial()
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
            guardar_estado_final(clientes, salones, reservaciones)
            break
        elif op == "1":
            agregar_reservacion(clientes, salones, reservaciones)
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