import uuid

class Financiera:
    def __init__(self, nombre, saldo_institucional):
        self.nombre=nombre
        self.id= uuid.uuid4() #genera id automatico
        self.saldo_institucional=saldo_institucional
        self.clientes = []

    def agregar_cliente(self, nuevo_cliente, linea_credito):
        diez_porciento = int(self.saldo_institucional * 0.1)
        if linea_credito <= diez_porciento: 
            #self.saldo_institucional = self.saldo_institucional - linea_credito
            self.diez_porciento = diez_porciento
            #Nuevo atributo Asignando linea de credito que solicitó
            nuevo_cliente.linea_credito = linea_credito
            self.clientes.append(nuevo_cliente)
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
    def giros_totles(self):
        pass
    def abonos_totales(self):
        pass
    def mostrar_saldo_institucional(self):
        print("Saldo institucional: ",self.saldo_institucional)
        

