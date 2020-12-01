class CuentaCorriente:

    def __init__(self, banco, numero_cuenta):
        self.banco = banco
        self.numero_cuenta = numero_cuenta
        self.saldo = 0

    def pagar(self):
        print("Procesando pago")
        pass
    
    def abonar(self, monto_entrada):
        self.saldo = self.saldo + monto_entrada
        print("Monto Abonado")
    
    def girar(self, monto_salida):
        if monto_salida < self.saldo:
            self.saldo = self.saldo - monto_salida

    
    def muestra_saldo(self):
        print("Muchos millones: ", self.saldo)
