'''''
Estás desarrollando un sistema de pagos en línea para una tienda virtual.

Requisitos iniciales:

El sistema debe permitir procesar pagos con diferentes métodos (tarjeta de crédito, PayPal y criptomonedas).

El sistema debe poder notificar al cliente cuando el pago fue exitoso, usando diferentes medios 
(correo electrónico, SMS, notificación en app).
En el futuro se espera:
Agregar más métodos de pago sin afectar lo que ya funciona.
Incorporar nuevas formas de notificación.
Facilitar pruebas unitarias para verificar que los pagos y notificaciones funcionan correctamente, 
sin necesidad de conectarse a servicios externos reales.
'''''
from abc import ABC, abstractmethod
from random import shuffle
class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self,monto:float):
        pass

class Notificacion(ABC):
    @abstractmethod
    def notificar(self,mensaje:str):
        pass

class PagoTarjetaCredito(MetodoPago):
    def procesar_pago(self, monto):
        return f"Se va a pagar con tarjeta de credito el monto de ${monto}..."
    
class PagoPaypal(MetodoPago):
    def procesar_pago(self, monto):
        return f"Se va a pagar con Paypal el monto de ${monto}..."

class PagoCripto(MetodoPago):
    def procesar_pago(self, monto):
        return f"Se va a pagar con Criptomoneda el monto de ${monto}..."
    
class NotificacionCorreo(Notificacion):
    def notificar(self,mensaje):
        return f"correo: {mensaje}"

class NotificacionSMS(Notificacion):
    def notificar(self,mensaje):
        return f"SMS: {mensaje}"

class NotificacionApp(Notificacion):
    def notificar(self,mensaje):
        return f"NotiApp: {mensaje}"
    
def pagar_y_notificar(metodopago:MetodoPago,notificacion:Notificacion,monto:float,mensaje:str):
    return f"{metodopago.procesar_pago(monto)}\n{notificacion.notificar(mensaje)}"

def main():
    lista_metodos_y_noti=[]

    pago_paypal=PagoPaypal()
    pago_tarjeta_credito=PagoTarjetaCredito()
    pago_con_cripto=PagoCripto()

    notificar_sms=NotificacionSMS()
    notificar_correo=NotificacionCorreo()
    notificar_app=NotificacionApp()
    
    lista_metodos_y_noti.extend([(pago_paypal,notificar_correo),(pago_con_cripto,notificar_app),(pago_tarjeta_credito,notificar_sms)])
    
    shuffle(lista_metodos_y_noti)

    for metodo,notificacion in lista_metodos_y_noti:
        print(f"{pagar_y_notificar(metodo,notificacion,200,"El pago se hizo de manera exitosa!")}\n")

if __name__=="__main__":
    main()






    




