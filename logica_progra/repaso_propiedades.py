class CuentaBancaria:
    def __init__(self,titular:str,saldo:float):
        if saldo<0:
            raise ValueError("El saldo inicial no puede ser negativo!")
        self._titular=titular
        self._saldo=saldo



    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self,new_saldo):
        if new_saldo<0:
            raise ValueError("No se pueden asignar saldos negativos!")
        self._saldo=new_saldo

    def depositar(self,cantidad:float):
        if cantidad<0:
            raise ValueError("No se permiten depositos negativos!")
        
        self._saldo+=cantidad

    def retirar(self,cantidad:float):
        if cantidad<0:
            raise ValueError("No se permiten retiros negativos")
        elif cantidad>self._saldo:
            raise ValueError("No puedes retirar cantidades mayores a tu saldo")
        self._saldo-=cantidad
        

persona_uno=CuentaBancaria("Fabi",1000)

print(persona_uno.titular)
print(persona_uno.saldo)
persona_uno.depositar(500)
print(persona_uno.saldo)
persona_uno.retirar(200)
print(persona_uno.saldo)
persona_uno.retirar(2000)



