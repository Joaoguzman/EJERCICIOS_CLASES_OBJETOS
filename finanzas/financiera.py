import uuid

class Cliente:
    def __init__(self, nombre_cliente, saldo_cliente, rut):
        self.nombre_cliente=nombre_cliente
        self.id= uuid.uuid4() #genera id automatico
        self.saldo_cliente=saldo_cliente # linea de credito ?
        self.rut = str(rut)
        self.giros_cliente = []
        self.suma_giros = sum(self.giros_cliente)
        self.abonos_cliente = []
        self.suma_abonos = sum(self.abonos_cliente)

    def saldo_personal(self):
        return self.saldo_cliente

    def girar(self, monto_a_girar):
        if self.saldo_cliente >= monto_a_girar:#verificar que el saldo a girar no exeda con lo que tengo en la cuenta
            self.saldo_cliente = self.saldo_cliente - monto_a_girar
            self.giros_cliente.append(float(monto_a_girar))
            self.suma_giros = sum(self.giros_cliente)
        else:
            print('No tienes saldo suficiente')

    def abonar(self, monto_a_depositar):
        self.saldo_cliente = self.saldo_cliente + monto_a_depositar
        self.abonos_cliente.append(float(monto_a_depositar))
        self.suma_abonos = sum(self.abonos_cliente)
    def mostrar_saldo(self):
        return "{}".format(self.saldo_cliente)

class Financiera(Cliente):
    def __init__(self, nombre_institucion, saldo_institucional):
        self.nombre_institucion=nombre_institucion
        self.id= uuid.uuid4() #genera id automatico
        self.saldo_institucional=saldo_institucional
        self.lista_clientes = []
        self.total_giros = []
        self.total_abonos = []
        self.total_saldo_clientes = []

    def agregar_cliente(self, cliente):        
        #self.saldo_cliente = saldo_cliente
        #self.nombre_cliente = nombre_cliente
        diez_porciento = int(self.saldo_institucional * 0.1)
        self.diez_porciento = diez_porciento
        diez_porciento = int(self.saldo_institucional * 0.1)
        if cliente.saldo_cliente <= diez_porciento: 
            #self.saldo_institucional = self.saldo_institucional - linea_credito
            #Nuevo atributo Asignando linea de credito que solicitó
            self.lista_clientes.append(cliente)
            self.saldo_institucional = self.saldo_institucional + cliente.saldo_cliente
            return f'Agregado {cliente.nombre_cliente}' #retorno verdad si se agregó el cliente a la financiera
        else:
            return False
        
    def eliminar_cliente(self, rut):
        for clientes in self.lista_clientes:
            if str(rut) == clientes.rut:
                self.saldo_institucional = self.saldo_institucional - clientes.saldo_cliente
                self.lista_clientes.remove(clientes)                
                print("Cliente eliminado")
            
    def mis_clientes(self):
        for cliente in self.lista_clientes:
            print("id: ", cliente.id)
            print("Nombre: ", cliente.nombre_cliente)
            print("Saldo: ", cliente.saldo_cliente)
        
    def transferir(self, cliente_origen, cliente_destino, monto):
        cliente_origen.saldo_cliente = cliente_origen.saldo_cliente - monto
        cliente_destino = cliente_destino.saldo_cliente - monto
        return True
        
    def giros_totales(self):
        self.total_giros = []
        for clientes in self.lista_clientes:
            self.total_giros.append(clientes.suma_giros)
        print("El total de giros de los clientes de la institución es: ", sum(self.total_giros))

    def abonos_totales(self):
        self.total_abonos = []
        for clientes in self.lista_clientes:
            self.total_abonos.append(clientes.suma_abonos)
        print("El total de abonos de los clientes de la institución es: ", sum(self.total_abonos))

    def mostrar_saldo_institucional(self):
        self.total_saldo_clientes = []
        for cliente in self.lista_clientes:
            self.total_saldo_clientes.append(cliente.saldo_cliente)
        total_saldo = sum(self.total_saldo_clientes)
        self.saldo_institucional = self.saldo_institucional + total_saldo
        print("Saldo institucional: ", self.saldo_institucional)
        

