# Instrucciones
# Codifique un programa que presente un menú con las siguientes opciones:

# [A]gregar
# [C]onsultar
# [X]Salir

# Las acciones a realizar son:

# AGREGAR - Solicita tres datos al usuario: Nombres(str), Apellidos(str) y antigüedad(int) para almacenarlos como un registro. Considere que de manera automática debe generar una clave 
# única a cada nuevo registro que se almacene.

# CONSULTAR -  Solicita la clave del registro que se desea consultar, si la clave no existe se le debe informar al usuario pero en caso de que exista deberá mostrar los datos 
# registrados para dicha clave.

# SALIR: Deberá salir de la solución


# **Nota: Deberá proteger su código contra excepciones que pudieran detener su ejecución. Ejemplo: (Un dato proporcionado no cumple con el tipo esperado, así que deberá volverse a 
# solicitar ese único dato hasta que cumpla con la especificación)
from tabulate import tabulate

def reviar_texto(menaje:str) ->str:
    texto=input(menaje)
    while texto.strip()=="" or not all(letra.isalpha() or letra.isspace() for letra in texto):
        print("No se permiten solo espacios en blanco o numeros dentro del nombre!")
        texto=input("Dime tu nombre(s): ")
    return texto



def main():
    lista_empleados:list[tuple]=[]
    indice=-1
    while True:
        print(f"\n{'-'*10} Bienvenido a la empresa Fabi's {'-'*10}")
        print("Que quieres hacer el dia de hoy? ")
        print("A. Agregar")
        print("C. consultar")
        print("X. Salir")
        opcion=input("Que opcion elijes: ")

        if opcion.upper()=="A":
            print(f"\n{'-'*10} Vamos a registrar un empleado {'-'*10}")
            nombre=reviar_texto("Dime tu nombre(s): ")
            apellido=reviar_texto("Dime tu apellidos: ")
            antiguedad=input("Años de antiguedad en la empresa: ")
            while not antiguedad.isdigit():
                print("\nSolo se permiten numeros!")
                antiguedad=input("Años de antiguedad en la empresa: ")
            antiguedad=int(antiguedad)
            indice+=1
            lista_empleados.append((indice,nombre.upper(),apellido.upper(),antiguedad))
        elif opcion.upper()=="C":
            if lista_empleados:
                print(f"\n{'-'*10} Vamos a buscar un empleado {'-'*10}")
                clave=input("Dime la clave que quires consultar: ")
                for indice,nombre,apellido,antiguedad in lista_empleados:
                    if str(indice)==clave:
                        print(tabulate([[indice,nombre,apellido,antiguedad]],headers=["Clave","Nombre del empleado","Apellidos del empleado","Antiguedad (años)"],tablefmt="fancy_grid"))
                        break
                else:
                    print("\nNo se encontro ese indice!")
                    continue
            else:
                print("\nNo hay empeladdos registrados!")
                continue
        elif opcion.upper()=="X":
            break
        else:
            print("Esa opcion no es valida!")

if __name__=="__main__":
    main()
