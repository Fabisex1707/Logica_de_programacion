#Ev1: programa para registrar eventos en salas
from tabulate import tabulate
import datetime
def convertir_str_a_date():
    while True:
        str_fecha_evento=input("Escribe la fecha de tu evento (DD/MM/YYYY) o [Enter] para cancelar la operacion: ")
        if str_fecha_evento.strip()=='':
            return False
        try:
            fecha_reservacion=datetime.datetime.strptime(str_fecha_evento,"%d/%m/%Y").date()
            return fecha_reservacion
        except:
            print("El formato de la fecha es invalida digitela de nuevo!")
            continue

def mostrar_datos_clientes(diccionario_clientes:dict):
    lista_clientes_con_orden=[]
    for id_cliente,datos in diccionario_clientes.items():
        lista_clientes_con_orden.append([datos["Apellidos"],datos["Nombre"],id_cliente])
    lista_clientes_con_orden.sort(key=lambda index_lista: index_lista[0])
    print(tabulate(lista_clientes_con_orden,headers=["Apellidos","Nombre Cliente","Id Cliente"],tablefmt="fancy_grid"))

def estado_turno(valor: bool) -> str:
    return "Disponible" if valor else "No disponible"

def mostrar_datos_salon(diccionario_salones:dict):
    lista_salas_con_orden=[]
    for id_sala,datos in diccionario_salones.items():
        lista_salas_con_orden.append([id_sala,
                                      datos["Nombre_salon"],
                                      datos["Cupo"],
                                      estado_turno(datos["Turno"]["Matutino"]),
                                      estado_turno(datos["Turno"]["Vespertino"]),
                                      estado_turno(datos["Turno"]["Nocturno"])])
    lista_salas_con_orden.sort(key=lambda index_lista: index_lista[0])
    print(tabulate(lista_salas_con_orden,headers=["Id de la sala","Nombre de la sala","Cupo","Turno matutino","Turno Vespertino","Turno Nocturno"],tablefmt="fancy_grid"))

def buscar_cliente(diccionario_clientes:dict)->bool | tuple:
    while True:
        mostrar_datos_clientes(diccionario_clientes)
        try:
            id_cliente_registrado=int(input("Escribe tu numero de cliente: "))
        except:
            print("\nDebes de ingresar un numero entero!")
            print(f"\n{'-'*60}")
            continue
                
        if not id_cliente_registrado in diccionario_clientes.keys():
            print("Ese usario no esta registrado!\n")
            salir=input("Quieres salir? 1.SI | 2.No: ")
            print(f"\n{'-'*60}")
            if salir!="2":
                return False
        else:
            return (id_cliente_registrado,diccionario_clientes[id_cliente_registrado]["Nombre"],diccionario_clientes[id_cliente_registrado]["Apellidos"])

def buscar_salon(diccionario_salones:dict)-> bool | tuple:
    while True:
        mostrar_datos_salon(diccionario_salones)
        try:
            id_salon_registrado=int(input("Escribe el id del salon que quiere reservar: "))
        except:
            print("\nDebes de ingresar un numero entero!")
            print(f"\n{'-'*60}")
            continue
                
        if not id_salon_registrado in diccionario_salones.keys():
            print("Ese salon no esta registrado!\n")
            salir=input("Quieres salir? 1.SI | 2.No: ")
            print(f"\n{'-'*60}")
            if salir!="2":
                return False
        else:
            return (id_salon_registrado,diccionario_salones[id_salon_registrado]["Nombre_salon"],diccionario_salones[id_salon_registrado]["Cupo"],diccionario_salones[id_salon_registrado]["Turno"]["Matutino"],diccionario_salones[id_salon_registrado]["Turno"]["Vespertino"],diccionario_salones[id_salon_registrado]["Turno"]["Nocturno"])
    

def main():
    #Contador que genera un id en serie para el registro de reservaciones
    id_reservaciones_contador=2
    #Estructuras de datos que almacenan los datos de los clientes, salones y eventos registrados
    clientes={1:{"Nombre":"Fabian","Apellidos":"Zantana Dolores"},
              2:{"Nombre":"Carlos","Apellidos":"Hernnadez Casas"}}

    salones={1:{"Nombre_salon":"Treviño Hernandez","Cupo":300,"Turno":{"Matutino":True,"Vespertino":True,"Nocturno":True}},
             2:{"Nombre_salon":"Emiliano Zapata","Cupo":200,"Turno":{"Matutino":True,"Vespertino":True,"Nocturno":True}}}
    
    reservaciones={1:{"id_cliente":1,"nombre_cliente":"Fabian","nombre_evento":"Coferencia sobre ciber seguridad","id_sala":1,"nombre_salon":"Treviño Hernandez","fecha_reservacion":"12/09/2026","turno":"Vespertino"}}
    while True:
        print(f"{'-'*10} Sistema para el registro de salas de coworking {'-'*10}\n")
        print("Bienvenido al menu de opciones...\n")
        print("1. Reservar una sala")
        print("2. Editar el nombre de la reservacion")
        print("3. Consultar reservaciones")
        print("4. Registrar un cliente")
        print("5. Registrar una sala")
        print("6. Salir")
        op=input("Que opcion elijes? ")

        if op=="6":
            print("Saliendo del sistema...")
            break
        elif op=="1":
            usario_encontrado=buscar_cliente(clientes)
            if usario_encontrado:
                while True:
                    print(f"\nBienvenido {usario_encontrado[1]} {usario_encontrado[2]}")
                    fecha_reservacion=convertir_str_a_date()
                    if not fecha_reservacion:
                        print(f"{'-'*60}\n")
                        print("--AVISO: Operacion candelada!, volviendo al menu principal...--")
                        print(f"\n{'-'*60}")
                        break
                    fecha_actual=datetime.datetime.today().date()
                    fecha_limite=fecha_reservacion+datetime.timedelta(days=-2)
                    if not fecha_limite>=fecha_actual:
                        print("Error: No puedes hacer tu reservacion, debe ser con dos dias de anticipacion!\n")
                        continue

                    print("\nFecha aceptada!, ahora vamos a elejir el salon\n")
                    salon_encontrado=buscar_salon(salones)
                    if not salon_encontrado:
                        print("Error: Ese salon no esta registrado!, volviendo al menu de registro de sala...")
                        print(f"\n{'-'*60}")
                        continue
                    print("\nId de salon aceptado!, ahora vamos a elejir el turno\n")
                    print(f"Datos del salon que elijio el usario: {salon_encontrado}")
            else:
                print("\n--AVISO: Operacion candelada!, volviendo la menu principal...--\n")
                continue
        else:
            print("\nEsa opciopn no existe!\n")
            continue


if __name__=="__main__":
    main()


