import uuid


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




class Condominio:
    def __init__(self,direccion, administrador,
                num_unidades_habitacionales, banco, numero_cuenta):

        self.direccion = direccion
        self.lista_administrador = administrador #recibe lista de administrador
        self.lista_guardias = []

        self.num_unidades_habitacionales = num_unidades_habitacionales
        self.lista_unidades = []
        self.__genera_numeracion()
        
        CuentaCorriente.__init__(self,banco, numero_cuenta)

        self.registro_gasto_comun = {} #diccionario { "mes": monto de gasto comun}
        self.lista_residente = []
        self.lista_personal_mantenimiento = []
        self.id = uuid.uuid4()


    def __genera_numeracion(self):
        for dpto in range(1,self.num_unidades_habitacionales):
            for piso in range(2):
                self.lista_unidades.append(str(piso)+str(0)+str(dpto))

    def get_direccion(self):
        # retorna direccion
        return self.direccion

    def set_direccion(self, direccion_nueva):
        # cambia la direccion por una nueva
        self.direccion = direccion_nueva

    def set_administrador(self, administrador_extraer, administrador_incluir):
        # cambia un administrador por uno nuevo de la lista_administrador
        self.lista_administrador = administrador_incluir

    def get_administrador(self):
        # retorna lista de administradores
        return self.lista_administrador
    
    def agregar_guardia(self, nuevo_guardia):
        #agregar guardia a lista_guardia
        self.lista_guardias.append(nuevo_guardia)  
    
    def del_guardia(self, rut_guardia):
        #borra el guardia de la lista_guardia
        for guardia in self.lista_guardias:
            print(guardia)
            if rut_guardia == guardia.rut:
                self.lista_guardias.remove(guardia)
            else:
                print("Guardia no está en la lista")

    def get_guardias(self):
        return self.lista_guardias
        # retorna lista de los guardias agregados
    
    def get_unidades(self):
        return self.lista_unidades
        # retorna la lista de las unidades habitacionales

    def agregar_personal_mantenimiento(self, nuevo_personal_mantenimiento):
        self.lista_personal_mantenimiento.append(nuevo_personal_mantenimiento)
        #agregar personal a lista_personal mantenimiento

    def calcular_gasto_comun(self, num_unidades_habitacionales,valor): #cálculo aproximado mientras agregamos sueldos y gastos
        return valor / num_unidades_habitacionales
        #calcular gasto comun del condominio

    def imprimir_lista_personal(self):
        print("Lista Personal Condominio")
        print("")
        for administrador in self.lista_administrador:
            print("Administrador: ", administrador)
        print("")
        for guardia in self.lista_guardias:
            print("Lista Guardias: ", guardia.nombre)
        print("")
        for personal_mantenimiento in self.lista_personal_mantenimiento:
            print("Lista Personal Mantenimiento: ", personal_mantenimiento) 


    def agregar_residente(self, nombre):
        #agregar residente a lista_residente
        self.lista_residente.append(nombre)
    
    
    
    

    
       

        #imprime lista completa del personal del condominio 


