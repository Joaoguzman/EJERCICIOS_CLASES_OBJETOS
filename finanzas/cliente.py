import uuid

class Cliente:
    def __init__(self, nombre, saldo):
        self.nombre=nombre
        self.id= uuid.uuid4() #genera id automatico
        self.saldo=saldo # linea de credito ?

    def girar(self, monto_a_girar):
        self.saldo = self.saldo - monto_a_girar
        #verificar que el saldo a girar no exeda con lo que tengo en la cuenta

    def abonar(self, monto_a_depositar):
        self.saldo = self.saldo + monto_a_depositar

    def mostrar_saldo(self):
        return "{}".format(self.saldo)