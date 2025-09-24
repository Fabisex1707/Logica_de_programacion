#Ev1: programa para registrar eventos en salas
from tabulate import tabulate
import datetime
def registrar_salon(registro_salones:dict,contador_id:int,nombre:str,cupo:int):
    registro_salones[contador_id]={"Nombre":nombre,"Cupo":cupo,"Turno":{"Matutino":True,"Vespertino":True,"Nocturno":True}}
    return f"Se registro con exito el salon {nombre}!"

def mostrar_datos_clientes(diccionario_clientes:dict):
    lista_clientes_con_orden=[]
    for id_cliente,datos in diccionario_clientes.items():
        lista_clientes_con_orden.append([datos["Apellidos"],datos["Nombre"],id_cliente])
    lista_clientes_con_orden.sort(key=lambda index_lista: index_lista[2])
    print(tabulate(lista_clientes_con_orden,headers=["Apellidos","Nombre Cliente","Id Cliente"],tablefmt="fancy_grid"))

def mostrar_datos_salon(diccionario_clientes:dict):
    lista_salas_con_orden=[]
    for id_sala,datos in diccionario_clientes.items():
        lista_salas_con_orden.append([id_sala,datos["Nombre_salon"],datos["Cupo"],datos["Turno"]["Matutino"],datos["Turno"]["Vespertino"],datos["Turno"]["Nocturno"]])
    lista_salas_con_orden.sort(key=lambda index_lista: index_lista[0])
    print(tabulate(lista_salas_con_orden,headers=["Id de la sala","Nombre de la sala","Cupo","Turno matutino","Turno Vespertino","Turno Nocturno"],tablefmt="fancy_grid"))

def buscar_cliente(diccionario_clientes:dict)->bool | tuple:
    while True:
        mostrar_datos_clientes(diccionario_clientes)
        try:
            id_cliente_registrado=int(input("Escribe tu numero de cliente: "))
        except:
            print("Debes de ingresar un numero entero!")
            continue
                
        if not id_cliente_registrado in diccionario_clientes.keys():
            print("Ese usario no esta registrado!\n")
            salir=input("Quieres salir? 1.SI | 2.No: ")
            print(f"\n{'-'*60}")
            if salir!="2":
                return False
        else:
            return (id_cliente_registrado,diccionario_clientes[id_cliente_registrado]["Nombre"],diccionario_clientes[id_cliente_registrado]["Apellidos"])
    

def main():
    #Contador que genera un id en serie para el registro de reservaciones
    id_reservaciones_contador=2
    #Estructuras de datos que almacenan los datos de los clientes y salones registrados
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
                    print(f"Bienvenido {usario_encontrado[1]} {usario_encontrado[2]}")
                    str_fecha_evento=input("Escribe la fecha de tu evento (DD/MM/YYYY) o [Enter] para cancelar la operacion: ")
                    if str_fecha_evento.strip()=='':
                        break
                    try:
                        fecha_reservacion=datetime.datetime.strptime(str_fecha_evento,"%d/%m/%Y").date()
                    except:
                        print("El formato de la fecha es invalida digitela de nuevo!")
                        continue
                    fecha_actual=datetime.datetime.today().date()
                    fecha_limite=fecha_reservacion+datetime.timedelta(days=-2)
                    if not fecha_limite>=fecha_actual:
                        print("Error: No puedes hacer tu reservacion, debe ser con dos dias de anticipacion!\n")
                        continue
                    print("Ahora vamos a elejir el salon\n")
                    mostrar_datos_salon(salones)
                    


            else:
                print("\n--AVISO: Operacion candelada!, volviendo la menu principal...--\n")
                continue
        else:
            print("\nEsa opciopn no existe!\n")
            continue


if __name__=="__main__":
    main()


