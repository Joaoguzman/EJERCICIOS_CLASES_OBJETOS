import uuid

class Cliente:
    def __init__(self, nombre, saldo):
        self.nombre=nombre
        self.id= uuid.uuid4() #genera id automatico
        self.saldo=saldo # linea de credito ?
    @property
    def saldo(self):
        return self.saldo
    @saldo.setter
    def girar(self, monto_a_girar):
        self.saldo = self.saldo - monto_a_girar
        #verificar que el saldo a girar no exeda con lo que tengo en la cuenta
    @saldo.setter
    def abonar(self, monto_a_depositar):
        self.saldo = self.saldo + monto_a_depositar

    def mostrar_saldo(self):
        return "{}".format(self.saldo)

class Financiera:
    def __init__(self, nombre, saldo_institucional, cliente1, cliente2, cliente3):
        self.nombre=nombre
        self.id= uuid.uuid4() #genera id automatico
        self.saldo_institucional=saldo_institucional
        self.clientes = [cliente1, cliente2, cliente3]
    def agregar_cliente(self, nuevo_cliente, linea_credito):
        diez_porciento = int(self.saldo_institucional * 0.1)
        if linea_credito <= diez_porciento: 
            #self.saldo_institucional = self.saldo_institucional - linea_credito
            self.diez_porciento = diez_porciento
            #Nuevo atributo Asignando linea de credito que solicitó
            self.linea_credito = linea_credito
            self.clientes.append(Cliente(nuevo_cliente, linea_credito))
            return True #retorno verdad si se agregó el cliente a la financiera
        else:
            return False
        
    def eliminar_cliente(self):
        pass
    def mis_clientes(self):
        for cliente in self.clientes:
            print("id: ", cliente.id)
            print("Nombre: ", cliente.nombre)
            print("Saldo: ", cliente.saldo)
            print("Linea de Credito: ", cliente.linea_credito)
        
    def transferir(self, cliente_origen, cliente_destino):
        pass
    def giros_totales(self):
        pass
    def abonos_totales(self):
        pass    
    def mostrar_saldo_institucional(self):
        print("Saldo institucional: ", self.saldo_institucional)
        

