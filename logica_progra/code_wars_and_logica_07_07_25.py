# def open_or_senior(data:list):
#     categories=[]
#     for x in data:
#         if x[0]>=55 and x[1]>7:
#             categories.append("Senior")
#         else:
#             categories.append("Open")
#     return categories
# print(open_or_senior([[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))

# def find_next_square(sq:int):
#     perfect_square=sq**0.5
#     if not ".0" in str(perfect_square):
#         print(perfect_square)
#         return None
#     else:
#         while True:
#             sq+=1
#             if sq**0.5 ==perfect_square+1:
#                 return sq

# print(find_next_square(114 ))

#Logica de programacion 16/07/25
# https://www.python.org/

# comentario en python
'''
hola este es otro comeentario
'''
""""
otra forma de comentar
"""""
# mi_primera_variable=1
# MI_PRIMERA_CONSTANTE=2

# print("Tipos de datos")
# mi_primer_str:str="hola"
# mi_primer_int:int=3
# mi_primer_float:float=2.3
# mi_primer_bool:bool=True
# mi_primer_list:list=[5]
# mi_primer_tuple:tuple=8,9
# mi_primer_set:set={1,"r",True}
# mi_primer_dict:dict={1:"Hola"}
# lista_variables=[mi_primer_str,
# mi_primer_int,
# mi_primer_float,
# mi_primer_bool,
# mi_primer_list,
# mi_primer_tuple,
# mi_primer_set,
# mi_primer_dict]

# for x in lista_variables:
#     print(type(x))

# print("Hola mi lenguaje favorito es python")


# #tipos de operadores
# #arimeticos{+,-,*,/,%,**,//}
# print("\nop aritmeticos")
# print(f"suma: 10 + 3= {10+3}")
# print(f"resta: 10 - 3= {10-3}")
# print(f"multiplicacion: 10 * 3= {10*3}")
# print(f"division: 10 / 3= {10/3}")
# print(f"modulo: 10 % 3= {10%3}")
# print(f"potenciacion: 10 ** 3= {10**3}")
# print(f"division entera: 10 // 3= {10//3}")

# print("\nop de comparacion")
# print(f"mayor que: 10<8= {10<8}")
# print(f"menor que: 10>8= {10>8}")
# print(f"igual que: 10==8= {10==8}")
# print(f"disintto a: 10!=10= {10!=10}")
# print(f"mayor o igual que: 10<=8= {10<=8}")
# print(f"menor o igual que: 10>=8= {10>=8}")

# print("\nop logicos")
# print(f"and o && solo si 1 y 1 = 1: {0>-8 and 10!=10}")
# print(f"or o || si 1 y 0 = 1: {0>-8 or 10!=10}")
# print(f"not o ! 0'= 1: {0>-8 and (not (10!=10))}")

# print("op asignacion")
# my_second_variable=2 #asignacion
# print(my_second_variable)
# my_second_variable+=1 #suma y asignacion
# print(my_second_variable)
# my_second_variable -=1 #resta y asignacion
# print(my_second_variable)
# my_second_variable *=1 #mltiplicacion y asignacion
# print(my_second_variable)
# my_second_variable /=1 #division y asignacion
# print(my_second_variable)
# my_second_variable **=1 #potenciacion y asignacion
# print(my_second_variable)
# my_second_variable //=1 #division entera y asignacion
# print(my_second_variable)

# print("\nop de identidad")
# print(my_second_variable)
# my_new_number=2.0
# print(f"my_second_variable is my_new_number {my_second_variable is my_new_number}")  #comparacion del valor en memoria, las posiocioens en memoria son distintas
# my_new_number=my_second_variable
# print(f"my_second_variable is my_new_number {my_second_variable is my_new_number}")
# print(f"my_second_variable is my_new_number {my_second_variable is not my_new_number}")

# print("\nop de petenecia / conjutos ")
# print(f"'F' in 'Fabian': {'F' in 'Fabian'}")
# print(f"'F' in 'Fabian': {'F' not in 'Fabian'}")

# print("\nop de bits")
# a=3  #0011
# b=10 #1010
# print(f"and o & a & b= {a & b}") #1 y  1 =1 / compara cada bit y cumple con su condicion para ser uno = 0010
# print(f"or o | a | b= {a | b}") #1 y  0 =1 =1011
# print(f"xor o | a | b= {a ^ b}") #1 y 1 =0, 0 y 0=0 = 1001
# print(f"not o ~ ~b= {~b}") #inversion/complemento A1
# print(f"desplazamiento a la der. >> a >> numero de desplazamientos= {b>>2}") #0010
# print(f"desplazamiento a la izq. << a << numero de desplazamientos= {b<<2}") #101000

# #Estuctras de control
# print("\nEstuctras de control condicional")
# my_str="Fabian"

# if my_str=="fabian":
#     print("my_str es fabian")
# elif my_str=="FabiaN":
#     print("my_str es FabiaN")
# else:
#     print("my_str es Fabian")

# print("\nEstuctras de control iterativas")

# for x in range(0,10):
#     print(x)

# print("\n")
# i=0
# while i<=10:
#     i+=1
#     print(i)

# print("\nEstuctras de excepciones")

# try:
#     print(1/1)
# except:
#     print("Algo malo paso")
# finally:
#     print("Fin del manejo de excepciones")

# # DIFICULTAD EXTRA (opcional):
# # Crea un programa que imprima por consola todos los números comprendidos
# # entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.

# for x in range(10,56):
#     if x%2==0 and x%3!=0 and x!=16:
#         print(x)

# # Funciones definidas por el usario

# #simple
# def My_firs_funtion():
#     print("\nHola!")

# My_firs_funtion()
# My_firs_funtion()

# # con retorno

# def my_second_funcion() ->str:
#     return "Hola python!"

# print(my_second_funcion())

# # con argmento

# def my_third_funcioon(name:str):
#     return(f"Hola {name}")

# print(my_third_funcioon("fabian"))

# # con argmentos

# def mensaje_nombre (greet,name):
#     return(f"{greet}, {name}")

# print(mensaje_nombre("hola","papus"))

# # con argmentos predeterminados

# def mensaje_nombre (greet,name:str="python"):
#     return(f"{greet}, {name}")

# print(mensaje_nombre("hola"))

# # con argmentos posicionales

# def mensaje_nombre (greet,name):
#     return(f"{greet}, {name}")

# print(mensaje_nombre(name="Fabian",greet="hola"))

# # con retorno de varios valores

# def multiple_return ():
#     return "hola","fabi"

# print(multiple_return())
# greet,name =multiple_return()
# print(greet)
# print(name)

# # con un numero n de variables
# def variablee_arg_greeet(*names):
#     for name in names:
#         print(f"hola {name}")

# variablee_arg_greeet("fabi","cas","dolores")

# # con un numero n de variables con palabra clave
# def variable_key_arg_greet(**names):
#     for key,value in names.items():
#         print(f"hola {value} {key}")

# variable_key_arg_greet(lenguaje="pyhon",name="fabi",nickname="cas",agee="36")

# #ffunciones dentro de funciones

# def outer_functtion():
#     def inner_funtion():
#         print("hola desde la funcion interna")
#     inner_funtion()#llamada a la funcion interna para mostrar el reultado al llamar a la funcion externa

# outer_functtion()

# #funciones del sistema
# print("hola:)")
# print(len("hola"))
# print(type(34))

# #funciones recursivas
# #factoial de un numero
# #caso base: si el numero es igual a 1 su factorial es 1

# def factorial_n(n:int):
#     if n==1:
#         return 1
#     else:
#         return n*factorial_n(n-1)

# print(factorial_n(4))
# #funciones recursivas
# #suma de los primeros n numeros naturales
# #caso base: si el numero es igual a 1 su factorial es 1

# #suma de n numeros naturales

# def suma_n(n:int):
#     if n==1:
#         return 1
#     else:
#         return n+suma_n(n-1)


# #suma_n(4) 4 + 6 = [10]
# #suma_n(3) 3 + 3 = 6
# #suma_n(2)= 2 + 1 = 3



# print(suma_n(4))

# #numero de digios en un numero entero

# def suma_digitos_n(n:int):
#     if n<10:
#         return 1
#     else:
#         return  1+suma_digitos_n(n//10)

# print(suma_digitos_n(2097))

# #inversion de cadena
# def cadena_invertida_n(cadena:str):
#     if len(cadena)<=1:
#         return cadena
#     else:
#         return  cadena_invertida_n(cadena[1::]) + cadena[0]

# print(cadena_invertida_n("FA"))

# def cadena_inverida(cadena:str):
#     return ''.join(letra for letra in cadena[::-1])

# print(cadena_inverida("FA"))

# def numero_aparaciones_n(texto1:str,texto2:str):
#     counter1=0
#     for x in range(1,101):
#         if x%3==0 and x%5==0:
#             print(f"{texto1} y {texto2}")
#         elif x%3==0:
#             print(texto1)
#         elif x%5==0:
#             print(texto2)
#         else:
#             counter1+=1
#     return counter1

# print(numero_aparaciones_n("hola","papu"))



#Estructura de datos en python 

#lista 
# my_first_lista=[]
# my_first_lista.append(True)
# print(my_first_lista)
# new=my_first_lista.copy()
# print(new)
# my_first_lista.extend([1,2,3,4,5,6,7,8,9,10,1])
# print(my_first_lista)
# print(my_first_lista.count(True))
# try:
#     print(my_first_lista.index(10,2))
# except ValueError as e:
#     print (e)

# my_first_lista.insert(1,"fabi")
# print(my_first_lista)
# print(my_first_lista.pop(1))
# print(my_first_lista)
# my_first_lista.remove(1)
# print(my_first_lista)
# my_first_lista.reverse()
# print(my_first_lista)
# my_first_lista.sort()
# print(my_first_lista)
# my_first_lista.clear()
# print(my_first_lista)

# #tuple
# my_first_tuple=1,2,1,1,1 #inmutable
# print(my_first_tuple.count(1))
# print(my_first_tuple.index(1,3))

# #set | conjuntos | no orden y no repetidos
# my_first_set={'A','B','C','X','Z'}
# my_second_set={'A','B'}
# print(my_first_set)
# my_first_set.add(10)
# print(my_first_set)
# print(my_first_set.difference(my_second_set)) # gardalo en otra variable
# #my_first_set.difference_update(my_second_set) #guarda la diferencia en el mismo set
# my_first_set.discard(20)#no lanza excepcion en caso de no encontrar el elemento
# try:
#     my_first_set.remove(1000000)
# except KeyError as e:
#     print(f"this element doesn't exist: {e}")
# print(my_first_set.intersection(my_second_set))#lo guardas dentro de una variable
# #my_first_set.intersection_update(my_second_set)# se guarda en el mismo set
# print(my_first_set.isdisjoint(my_second_set))
# print(my_second_set.issubset(my_first_set))
# print(my_first_set.issubset(my_second_set))
# print(my_first_set.issuperset(my_second_set))
# print(my_first_set)
# print(my_first_set.pop())# borrar aleatoriamente
# print(my_first_set)
# print(my_first_set.symmetric_difference(my_second_set))
# my_first_set.symmetric_difference_update(my_second_set)
# print(my_first_set)
# print(my_first_set.union(my_second_set))

# #dict
# my_first_dict={"Name":"Fabian","Lastname":"Castro Dolores","Age":20, "Status":True}
# print(my_first_dict.fromkeys([10,20,30],"Fabi"))#creacion de unn dict con llaves distintas coj un valor en comun 
# print(my_first_dict.get("Color","details: that key doesn't exist"))
# print(my_first_dict.items())
# print(my_first_dict.keys())
# print(my_first_dict.values())
# print(my_first_dict.pop("Name","details: that key doesnt exist"))
# print(my_first_dict)
# try:
#     print(my_first_dict.pop("Name"))
# except KeyError as e:
#     print(f"this key doesn't exist {e}")
# print(my_first_dict.popitem())# borra el ultimo par
# print(my_first_dict)
# print(my_first_dict.setdefault("Color","White"))#agregar mas elemntos, llave y op valor
# print(my_first_dict)
# my_first_dict.update({"country":["Mexico",'peru','bolovia'],"state":"Nuevo Leon","City":"Monterrey"})#agregar varios pares de llave:valor
# print(my_first_dict)


# Crea una agenda de contactos por terminal.
#  * - Debes implementar funcionalidades de búsqueda, inserción, actualización
#  *   y eliminación de contactos.
#  * - Cada contacto debe tener un nombre y un número de teléfono.
#  * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
#  *   y a continuación los datos necesarios para llevarla a cabo.
#  * - El programa no puede dejar introducir números de teléfono no numéricos y con más
#  *   de 11 dígitos (o el número de dígitos que quieras).
#  * - También se debe proponer una operación de finalización del programa.

agenda=[]


def main():
    indice=-1
    while True:
        print(f"{'_'*10} Agenda electronica {'_'*10}")
        print(f"{'_'*10} Menu {'_'*10}")
        print("1. Añadir un nuevo contacto")
        print("2. Buscar un contacto")
        print("3. Actualizar un contacto")
        print("4. Eliminar un contacto")
        print("5. Salir")
        op=input("Escribe la opcion: ")
        if op=="5":
            break
        elif op=="1":
            print(f"{'_'*10} Agregar un contacto {'_'*10}")
            name=input("Escribe el nombre del contacto: ")
            tel=input("Escribe su numero de telefono: ")
    
            if name.strip()=='' or (not (all(letra.isalpha() or letra.isspace() for letra in name.upper()))):
                print("No se pueden poner nombres en blanco o con numeros!")
                continue
            elif ((tel.isnumeric())!=True or tel==" ") and len(tel)!=10:
                print("No se pueden poner telefonos en blanco o con mas de 10 numeros!")
                continue
            else:
                indice+=1
                agenda.append([indice,name.upper(),tel])
        elif op=="2":
            if not agenda:
                print("No hay contactos que buscar")
                continue
            print(f"{'_'*10} Buscar un contacto {'_'*10}")
            search_name=input("Escribe el nombre de la persona: ")
            for elemento in agenda:
                if search_name.upper() in elemento[1]:
                    print(f"{elemento[0]}| {elemento[1]} | {elemento[2]}")
            continue
        elif op=="3":
            if not agenda:
                print("No hay contactos que actualizar")
                continue
            print(f"{'_'*10} Actualizar un contacto {'_'*10}")
            for elemento in agenda:
                print(f"{elemento[0]}| {elemento[1]} | {elemento[2]}")
            id=input("Que numero de contacto quieres cambiar? ")
            list_index=[]
            list_index.extend(str(item[0]) for item in agenda)
            print(list_index)
            if not(id in list_index):
                print("Ese indice no esta en la agenda!")
                continue

            print("1.Nombre")
            print("2.Telefono")
            op=input("Que opcion elijes? ")
            if op.split()==" ":
                continue
            if op=="1":
                name_update=input("Escribe el nuevo nombre: ")
                if name_update.strip()=='' or not all(letra.isalpha() or letra.isspace() for letra in name_update.upper()):
                    print("No se pueden poner nombres en blanco o con numeros!")
                    continue

                agenda[int(id)]=[int(id),name_update.upper(),agenda[int(id)][2]]
                print(agenda)
                continue
            if op=="2":
                new_tel=input("Escribe el nuevo numero de telefono: ")
                if ((tel.isnumeric())!=True or tel==" ") and len(tel)!=10:
                    print("No se pueden poner telefonos en blanco o con mas de 10 numeros!")
                    continue

                agenda[int(id)]=[int(id),agenda[int(id)][1],new_tel]
                print(agenda)
                continue
            else:
                print("Esa opcion no es valida!")
                continue
        elif op=="4":
            if not agenda:
                print("No hay contactos que eliminar")
                continue
            print(f"{'_'*10} Eliminar un contacto {'_'*10}")
            for elemento in agenda:
                print(f"{elemento[0]}| {elemento[1]} | {elemento[2]}")
            id=input("Que numero de contacto quieres eliminar? ")
            list_index=[]
            list_index.extend(str(item[0]) for item in agenda)
            print(list_index)
            if not(id in list_index):
                print("Ese indice no esta en la agenda!")
                continue
            item_deleted=agenda.pop(int(id))
            print(f"Se borro el indice {id} = {item_deleted}")
        else:
            print("Esa opcion no es valida!")



if __name__=="__main__":
    main()














