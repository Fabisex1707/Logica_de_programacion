#entradas 
#nombre_empleado, fecha_de_nacimiento,lista_empleados, lista_de_empleados_mayores,fecha_actual,edad_minima
# #
#procesos
# formato de fecha dd/mm/aaaa
# salida del programa por enter
# empleados mayores que n edad minima
# #
#salida
# tabulacion de empleados mayores que edad minima n#
import datetime
from tabulate import tabulate

def check_str_a_datetime(dt_string:str) ->bool:
    """Retorna True en caso de que dt_string tenga el formato correcto para la fecha, dd/mm/aaaa, en caso contrario retorna False"""
    try:
        datetime.datetime.strptime(dt_string,"%d/%m/%Y").date()
        return True
    except:
        return False

def calcula_edad_por_fecha_de_nacimiento(dt_string:str) -> int|str:
    """Calcula y retorna la edad del usario a dia de hoy, es un texto y el formato para la fecha es 'dd/mm/aaaa'."""
    try:
        TODAY=datetime.datetime.today().date()
        date_of_birth=datetime.datetime.strptime(dt_string,"%d/%m/%Y").date()
        if (TODAY.month,TODAY.day)>(date_of_birth.month,date_of_birth.day):
            return TODAY.year-date_of_birth.year
        else:
            return (TODAY.year-date_of_birth.year)-1
    except ValueError as e:
        return(f"details: el formato no coincide! {e}")

def main():
    lista_empleados=[]
    lista_empleados_mayores=[("Nombre","Fecha de nacimiento")]

    while True:    
        print(f'\n{"*"*10} Vamos a registrar empleados {"*"*10}')
        nombre_empleado=input("Dame el nombre del empleado o [Enter] para salir: ")
        if nombre_empleado.strip()=="":
            break
        elif not all(letra.isalpha() or letra.isspace() for letra in nombre_empleado.upper()):
            print("El nombre no debe contener numeros o caracteres especiales!")
            continue
        fecha_de_nacimiento=input("Dame la fecha de nacimiento del empleado (dd/mm/aaaa): ")
        if check_str_a_datetime(fecha_de_nacimiento):
            lista_empleados.append((nombre_empleado,fecha_de_nacimiento))
        else:
            print("Formato de fecha incorrecta!\n")
            continue

    if lista_empleados:
        edad_minima=input("Dime la edad mimina que estas buscando: ")
        for empleado in lista_empleados:
            edad_empelado=calcula_edad_por_fecha_de_nacimiento(empleado[1])
            if edad_empelado>int(edad_minima):
                lista_empleados_mayores.append(empleado)
        if lista_empleados_mayores[1::]:
            print(f'\n{"*"*10} Empelados que superan la edad minima {"*"*10}')
            print(tabulate(lista_empleados_mayores[1::],headers=lista_empleados_mayores[0],tablefmt="fancy_grid"))
        else:
            print("\nNo hay trabajadores que superen la edad minima!")

if __name__=="__main__":
    main()






