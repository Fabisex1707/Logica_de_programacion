import math
import random
import datetime
import time
#modulo math
# print(math.floor(3))#nos retornar el entero mas cercano hacia atras del 0
# print(math.ceil(31.1))#nos retornar el entero mas cercano hacia adelante del 0

# print(math.trunc(-3.9))#devuelve solo la parte entera de un numro decimal

# print(math.factorial(5))
# print(math.pow(3,2))# x a la potencia y
# print(math.sqrt(4))
# print(f"{math.pi:.4f}")
# print(math.isclose(100,4,rel_tol=1,abs_tol=1e-6))#numeros grandes,rel_tol=% 1==100%
# contador = 0
# incremento = 0.1

# while not math.isclose(contador, 1, abs_tol=0.1):
#     print(contador)
#     contador += incremento

#modulo random
# [1,2,"b",True,9.0]
# b=[1,2,3,4,5,6]
# print(random.randrange(8))
# print(random.randrange(8,20))
# print(random.randrange(20,2,-1))
# print(random.randint(8,20))
# print(random.random())
# print(random.choice([1,2,"b",True,9.0]))
# print(random.choices([1,2,"b",True,9.0],k=3))
# print(b)
# random.shuffle(b)
# print(b)

#modulo datetime
#crea tu hora
# hora=datetime.time(17,50,45,2)
# print(type(hora))
# print(hora)
# print(hora.hour)
# print(hora.minute)
# print(hora.second)
# print(hora.microsecond)
# #crea tu fecha
# fecha_actual=datetime.datetime.today()
mi_fecha=datetime.date(2025,9,9)
print(type(mi_fecha.month))
# #formato a una fecha que creamos nosotros
# print(mi_fecha.strftime("%d-%B-%y"))
# print(type(fecha_actual))
# print(fecha_actual)
# print(fecha_actual.day)
# print(fecha_actual.month)
# print(fecha_actual.year)

# fecha_capturada=input("Dame una fecha dd/mm/aaaa  HH:MM:SS: \n")
# #de str a objeto datetime
# fecha_procesada=datetime.datetime.strptime(fecha_capturada,"%d/%m/%Y  %H:%M:%S")
# print(fecha_procesada.strftime("%A/%B/%y"))
# print(type(fecha_capturada))
# print(type(fecha_procesada))
# print(fecha_capturada)
# print(fecha_procesada)

# #calculos con datetime
# #adelnata n dias desde hoy
# print(fecha_actual)
# no_dias=int(input(f"Dime cuantos dias quieres adelantar a partir de hoy {fecha_actual}: \n"))
# new_date=fecha_actual+datetime.timedelta(days=+no_dias,hours=+3)
# print(new_date)

#edad por la fecha de nacimiento
# my_date_of_birth=input("Dime tu fecha de nacimiento dd/mm/aaaa: \n")
# new_date=datetime.datetime.strptime(my_date_of_birth,"%d/%m/%Y").date()
# age=datetime.datetime.today().year-new_date.year
# print(age)







