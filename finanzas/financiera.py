import uuid

class Financiera:
    def __init__(self, nombre, saldo_institucional):
        self.nombre=nombre
        self.id= uuid.uuid4() #genera id automatico
        self.saldo_institucional=saldo_institucional
        self.clientes_list = []
        self.total_clientes = int(self.saldo_institucional / 1000000)
        self.contador_clientes = 0

    def agregar_cliente(self, nuevo_cliente):
        diez_porciento = int(self.saldo_institucional * 0.1)
        if nuevo_cliente.linea_credito <= diez_porciento:
            #controlo cantidad de clientes que acepta mi banco
            if self.contador_clientes <= self.total_clientes:
                nuevo_cliente.linea_credito = 1000000
                self.clientes_list.append(nuevo_cliente)
                #agrego saldo cliente al saldo institucional
                self.saldo_institucional = self.saldo_institucional + nuevo_cliente.saldo
                #Actualizo total de clientes permitidos
                self.total_clientes = int(self.saldo_institucional / 1000000)
                self.total_clientes -= 1
                self.contador_clientes += 1
                print("Cliente Creado!")
                return True
            elif self.total_clientes == 0:
                print("Error! ")
                return False
            else:
                print("Error! ")
        else:
            print("Error! ")
            return False
        
    def eliminar_cliente(self, cliente_a_eliminar):
        if cliente_a_eliminar in self.clientes_list:
            self.clientes_list.remove(cliente_a_eliminar)
            return True
            print("{} Eliminado Satisfactoriamente".format(cliente_a_eliminar.nombre))
        else:
            print("{} no es nuestro cliente".format(cliente_a_eliminar.nombre))
            return False

    def mis_clientes(self):
        for cliente in self.clientes_list:
            print("id: ", cliente.id)
            print("Nombre: ", cliente.nombre)
            print("Saldo: ", cliente.saldo)
            print("Linea de Credito: ", cliente.linea_credito)
        
    def transferir(self, cliente_origen, cliente_destino, monto):
        pass
    def giros_totles(self):
        pass
    def abonos_totales(self):
        pass
    def mostrar_saldo_institucional(self):
        print("Saldo institucional: ",self.saldo_institucional)
        

