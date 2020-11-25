import uuid

class Cliente:
    def __init__(self, nombre, saldo):
        self.nombre=nombre
        self.id= uuid.uuid4() #genera id automatico
        self.saldo=saldo # linea de credito ?
        self.linea_credito = 0

    def girar(self, monto_a_girar):
        print(self.nombre," girando: ", monto_a_girar)
        saldo_auxiliar = self.saldo - monto_a_girar

        if saldo_auxiliar >= -1000000: 
            self.saldo = self.saldo - monto_a_girar
            return monto_a_girar
        else:
            print("Error, supera el credito! ")
            print("Su saldo es: ", self.saldo)
            print("Su linea de credito max es 1000000\n")
            return False

    def abonar(self, monto_a_depositar):
        print(self.nombre, " abonando: ", monto_a_depositar)
        self.saldo = self.saldo + monto_a_depositar
        return monto_a_depositar

    def mostrar_saldo(self):
        return "El saldo de {} es: {}".format(self.nombre ,self.saldo)