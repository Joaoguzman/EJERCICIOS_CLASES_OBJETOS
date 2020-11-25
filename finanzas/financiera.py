import uuid

class Financiera:
    def __init__(self, nombre, saldo_institucional):
        self.nombre=nombre
        self.id= uuid.uuid4() #genera id automatico
        self.__saldo_institucional=saldo_institucional
        self.clientes = []
        self.total_clientes = int(self.__saldo_institucional / 1000000)
        self.contador_clientes = 0

    def agregar_cliente(self, nuevo_cliente):
        diez_porciento = int(self.__saldo_institucional * 0.1)
        if nuevo_cliente.linea_credito <= diez_porciento:
            #controlo cantidad de clientes que acepta mi banco
            if self.contador_clientes <= self.total_clientes:
                nuevo_cliente.linea_credito = 1000000
                self.clientes.append(nuevo_cliente)
                #agrego saldo cliente al saldo institucional
                self.__saldo_institucional = self.__saldo_institucional + nuevo_cliente.saldo
                #Actualizo total de clientes permitidos
                self.total_clientes = int(self.__saldo_institucional / 1000000)
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
        if cliente_a_eliminar in self.clientes:
            self.clientes.remove(cliente_a_eliminar)
            return True
            print("{} Eliminado Satisfactoriamente".format(cliente_a_eliminar.nombre))
        else:
            print("{} no es nuestro cliente".format(cliente_a_eliminar.nombre))
            return False

    def mis_clientes(self):
        for cliente in self.clientes:
            print("id: ", cliente.id)
            print("Nombre: ", cliente.nombre)
            print("Saldo: ", cliente.saldo)
            print("Linea de Credito: ", cliente.linea_credito)
        
    def transferir(self,c_origen, b_destino ,c_destino, monto):
        print(c_origen.nombre, " está transfiriendo ", monto, " a ", c_destino.nombre)
        giro = self.clientes[self.clientes.index(c_origen)].girar(monto)
        #se descuenta de saldo institucional al hacer un gira con saldo negativo
        if giro:
            print(giro)
            #Actualizando saldo institucional de financiera de origen
            print("saldo giro: ", giro)
            self.saldo_institucional -= giro
            #abonando en cuenta de destino
            abono = b_destino.clientes[b_destino.clientes.index(c_destino)].abonar(giro)
            #Actualizando saldo institucional de financiera destino
            b_destino.saldo_institucional += abono
            print("Transferencia exitosa")
        
        
    def giros_totles(self):
        pass
    def abonos_totales(self):
        pass
    def mostrar_saldo_institucional(self):
        print("Saldo institucional: ",self.__saldo_institucional)
        
    @property
    def saldo_institucional(self):
        return self.__saldo_institucional

    @saldo_institucional.setter
    def saldo_institucional(self, saldo_institucional):
        #print("cambiando atributo encapsulado saldo_institucional")
        self.__saldo_institucional = saldo_institucional

