import uuid

class Cliente:
    def __init__(self, nombre_cliente, saldo_cliente):
        self.nombre_cliente=nombre_cliente
        self.id= uuid.uuid4() #genera id automatico
        self.saldo_cliente=saldo_cliente # linea de credito ?
        
    def saldo_personal(self):
        return self.saldo_cliente

    def girar(self, monto_a_girar):
        if self.saldo_cliente <= monto_a_girar:#verificar que el saldo a girar no exeda con lo que tengo en la cuenta
            self.saldo_cliente = self.saldo_cliente - monto_a_girar
        else:
            return f'No tienes saldo suficiente'

    def abonar(self, monto_a_depositar):
        self.saldo_cliente = self.saldo_cliente + monto_a_depositar

    def mostrar_saldo(self):
        return "{}".format(self.saldo_cliente)

class Financiera(Cliente):
    def __init__(self, nombre_institucion, saldo_institucional):
        self.nombre_institucion=nombre_institucion
        self.id= uuid.uuid4() #genera id automatico
        self.saldo_institucional=saldo_institucional
        self.lista_clientes = []
        
    def agregar_cliente(self, nombre_cliente, saldo_cliente):
        Cliente.__init__(self, nombre_cliente, saldo_cliente)
        diez_porciento = int(self.saldo_institucional * 0.1)
        if saldo_cliente <= diez_porciento: 
            #self.saldo_institucional = self.saldo_institucional - linea_credito
            self.diez_porciento = diez_porciento
            #Nuevo atributo Asignando linea de credito que solicitó
            self.saldo_cliente = saldo_cliente
            self.lista_clientes.append(Cliente(nombre_cliente, saldo_cliente))
            return True #retorno verdad si se agregó el cliente a la financiera
        else:
            return False
        
    def eliminar_cliente(self, cliente):
        for clientes in self.lista_clientes:
            if cliente == clientes:
                self.lista_clientes.remove(cliente)
            else:
                return False
            
    def mis_clientes(self):
        for cliente in self.lista_clientes:
            print("id: ", cliente.id)
            print("Nombre: ", self.nombre_cliente)
            print("Saldo: ", self.saldo_cliente)
        
    def transferir(self, cliente_origen, cliente_destino):
        pass
    def giros_totales(self):
        pass
    def abonos_totales(self):
        pass    
    def mostrar_saldo_institucional(self):
        print("Saldo institucional: ", self.saldo_institucional)
        

