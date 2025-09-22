#Ev1: programa para registrar eventos en salsas

def registrar_salon(registro_salones:dict,contador_id:int,nombre:str,cupo:int):
    registro_salones[contador_id]={"Nombre":nombre,"Cupo":cupo,"Turno":{"Matutino":True,"Vespertino":True,"Nocturno":True}}
    return f"Se registro con exito el salon {nombre}!"

def main():
    #Contador que genera un id en serie para el registro de reservaciones
    id_reservaciones_contador=2
    #Estructuras de datos que almacenan los datos de los clientes y salones registrados
    clientes={1:{"Nombre":"Fabian","Apellidos":"Castro Dolores"},
              2:{"Nombre":"Carlos","Apellidos":"Hernnadez Casas"}}

    salones={1:{"Nombre":"Treviño Hernandez","Cupo":300,"Turno":{"Matutino":True,"Vespertino":True,"Nocturno":True}},
             2:{"Nombre":"Emiliano Zapata","Cupo":200,"Turno":{"Matutino":True,"Vespertino":True,"Nocturno":True}}}
    
    reservaciones={}
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
            id_cliente_registrado=int(input("Escribe tu numero de cliente: "))
            while not (id_cliente_registrado in clientes.keys()):
                print("Ese numero de cliente no esta registrado!, intente de nuevo\n")
                id_cliente_registrado=int(input("Escribe tu numero de cliente: "))
                salir=input("Quieres salir? 1.SI | 2.No: ")
                if salir!="2":
                    print("saliendo..")
                    break
            else:
                print("Este proceso continuara...")
        else:
            print("\nEsa opciopn no existe!\n")
            continue


if __name__=="__main__":
    main()


