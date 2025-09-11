from abc import ABC,abstractmethod
from random import shuffle
from datetime import datetime,date,timedelta


#ejercicios aplicando srp, ocp, lsp
# ejercicio 1: Tienes una clase base Vehiculo con un método mover().
# Necesitas implementar Coche, Bicicleta y Barco.
# Asegúrate de que cualquier Vehiculo pueda ser usado donde se espere uno, sin romper LSP.
# Haz que main() reciba una lista de vehículos y llame a mover() sin saber cuál es cuál.
# 🎯 Objetivo: Evitar que subclases como Barco rompan el contrato (por ejemplo, requiriendo atributos adicionales que la base no pide).

# class Vehiculo(ABC):
#     @abstractmethod
#     def mover(self):
#         pass

# class Bicicleta(Vehiculo):
#     def mover(self):
#         print("mover la bici pedaleando!")

# class Coche(Vehiculo):
#     def __init__(self,tengo_llaves:bool=True):
#         super().__init__()
#         self.llave=tengo_llaves

#     def mover(self):
#         if self.llave:
#             print("enciende el coche con las llaves y pisa el acelerador!")
#         else:
#             print("No tengo las llaves no puedo moverme!")


# class Barco(Vehiculo):
#     def __init__(self,leven_anclas:bool=True):
#         super().__init__()
#         self.anclas=leven_anclas
#     def mover(self):
#         #majea todas las validaciones de este metodo aqui, pues te dice que la debes de usar pero no como
#         if self.anclas:
#             print(f"Leva las anclas y sarpa!")
#         else:
#             print("no podemos sarpar porque no hemos elevado las anclas!")


# def moverme(vehiculo:Vehiculo):
#     vehiculo.mover()

# def main():
#     lista_de_vehiculos=[]
#     try:
#         bici=Bicicleta()
#         carro=Coche(False)
#         boat=Barco(False)
#         lista_de_vehiculos.extend([bici,carro,boat])
#     except ValueError as e:
#         print(e)
#     shuffle(lista_de_vehiculos)
#     for vehiculo in lista_de_vehiculos:
#         moverme(vehiculo)

# if __name__=="__main__":
#     main()


# Ejercicio 2 — Procesador de archivos

# Clase base ProcesadorArchivo con método procesar().
# Subclases: ProcesarPDF, ProcesarWord, ProcesarImagen.

# Cumple OCP para que agregar un nuevo tipo de archivo no modifique el código que procesa.

# Cumple LSP asegurando que todas las subclases funcionen de forma intercambiable.

# 🎯 Objetivo: Evitar que una subclase cambie la firma de procesar() o tenga requerimientos que otras no tienen.

# 


# Ejercicio 3 — Cuentas bancarias

# Clase base CuentaBancaria con métodos depositar(monto) y retirar(monto).
# Subclases: CuentaCorriente, CuentaAhorro, CuentaInversion.

# Cumple SRP separando la lógica de depósito/retiro de la presentación o reportes.

# Cumple OCP si mañana agregas CuentaCripto sin tocar el código principal.

# Cumple LSP asegurando que todas las cuentas mantengan el mismo comportamiento esperado (por ejemplo, no permitir que una subclase cambie retirar para cobrar comisiones ocultas sin avisar).

# 🎯 Objetivo: Detectar si una implementación de retirar rompe las expectativas.

class CuentaBancaria(ABC):
    @abstractmethod
    def depositar(self,monto:float):
        pass
    @abstractmethod
    def retirar(self,monto:float):
        pass

class CuentaCorriente(CuentaBancaria):
    def __init__(self,saldo:float):
        super().__init__()
        self.saldo=saldo
    def depositar(self,monto:float):
        self.saldo+=monto
        print(f"Deposito ${monto:,.2f} en mi cuenta corrriente, mi saldo actual es ${self.saldo:,.2f}")
    def retirar(self,monto:float):
        if monto<self.saldo:
                self.saldo-=monto
                print(f"Retiro ${monto:,.2f} de mi cuenta de corrriente, el saldo actual es {self.saldo:,.2f}")
        else:
            print(f"Saldo insufuciente! usted tiene solo ${self.saldo:,.2f}")

class CuentaAhorro(CuentaBancaria):
    def __init__(self,saldo:float):
        super().__init__()
        self.saldo=saldo
    def depositar(self,monto:float):
        self.saldo+=monto
        print(f"Deposito ${monto:,.2f} en mi cuenta de ahorro, mi saldo actual es ${self.saldo:,.2f}")

    def retirar(self,monto:float):
        if monto<self.saldo:
            self.saldo-=monto
            print(f"Retiro ${monto:,.2f} de mi cuenta de ahorro, el saldo actual es {self.saldo:,.2f}")
        else:
            print(f"Saldo insufuciente! usted tiene solo ${self.saldo:,.2f}")

class CuentaConPlazo(CuentaBancaria):
    @abstractmethod
    def puedo_retirar(self)->bool:
        pass

class CuentaInversion(CuentaConPlazo):
    def __init__(self,saldo:float,plazo_inversion_años:int):
        super().__init__()
        self.saldo=saldo
        self.fecha_actual=datetime.today().date()
        self.fecha_inicio_inversion=date(2025,9,4)
        self.plazo_inversion=plazo_inversion_años

    def depositar(self,monto:float):
        self.saldo+=monto
        print(f"Deposito ${monto:,} en mi cuenta de inversion, mi saldo actual es ${self.saldo:,.2f}")
    
    def puedo_retirar(self):
        fecha_limite=date(self.fecha_inicio_inversion.year+1,self.fecha_inicio_inversion.month,self.fecha_inicio_inversion.day)
        return self.fecha_actual>=fecha_limite

    def retirar(self,monto:float):
        if self.puedo_retirar():
            if monto<self.saldo:
                self.saldo-=monto
                print(f"Retiro ${monto:,} de mi cuenta de inversion, el saldo actual es {self.saldo:,.2f}")
            else:
                print(f"Saldo insufuciente! usted tiene solo ${self.saldo:,.2f}")
        else:
            print(f"Aun no puedes reitirar dinero hasta que pase el plazo de {self.plazo_inversion} año(s)")

def usar_cuenta(cuenta:CuentaBancaria,monto:float,depositar:bool=True):
    if depositar:
        cuenta.depositar(monto)
    else:
        cuenta.retirar(monto)


def main():
    lista_cuentas_bancarias=[]
    corriente=CuentaCorriente(2000)
    ahorros=CuentaAhorro(1500)
    inversion=CuentaInversion(3000,1)
    lista_cuentas_bancarias.extend([corriente,ahorros,inversion])
    shuffle(lista_cuentas_bancarias)
    for cuenta in lista_cuentas_bancarias:
        usar_cuenta(cuenta,200,False)

if __name__=="__main__":
    main()
    


