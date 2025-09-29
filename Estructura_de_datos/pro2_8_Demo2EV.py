from tabulate import tabulate
import datetime

def convertir_str_a_date():
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
    while True:
        mostrar_datos_clientes(diccionario_cliente)
        try:
            nombre = input("Dame un nombre o nombres a registrar: ").strip()
            apellido = input("Dame tus apellidos a registrar: ").strip()

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
            break

        except:
            print("Ocurrio un error")        

def mostrar_datos_clientes(diccionario_clientes: dict):
    lista_clientes_con_orden = []
    for id_cliente, datos in diccionario_clientes.items():
        lista_clientes_con_orden.append([datos["Apellidos"], datos["Nombre"], id_cliente])
    lista_clientes_con_orden.sort(key=lambda index_lista: index_lista[0])
    print(tabulate(lista_clientes_con_orden, headers=["Apellidos", "Nombre Cliente", "Id Cliente"], tablefmt="fancy_grid"))

def estado_turno(valor: bool) -> str:
    return "Disponible" if valor else "No disponible"

def mostrar_datos_salon(diccionario_salones: dict):
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

    while True:
        nuevo_nombre = input("Nuevo nombre del evento: ").strip()
        if nuevo_nombre != "":
            seleccionado["nombre_evento"] = nuevo_nombre
            print("Evento actualizado.")
            return
        print("El nombre no puede estar vacío.")
    




    
        

def main():
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
            usuario_encontrado = buscar_cliente(clientes)
            if usuario_encontrado:
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
                    print(f"Datos del salon que eligió el usuario: {salon_encontrado}")
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
                        if nombre_evento == "":
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
            else:
                print("\n--AVISO: Operación cancelada!, volviendo al menú principal...--\n")
                continue
        elif op == "2":
            editar_nombre_reservacion(reservaciones)
        elif op == "3":
            consultar_reservaciones_por_fecha(reservaciones)
        elif op == "4":
            registrar_cliente(clientes)
        else:
            print("\nEsa opción no existe!\n")
            continue
        



if __name__ == "__main__":
    main()