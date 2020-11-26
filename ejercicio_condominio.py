import uuid

class Condominio:
    def __init__(self, direccion, lista_administrador, num_guardias, 
                num_unidades_habitacionales, lista_unidades,
                lista_residentes, lista_personal_mantenimiento, id_condominio):

        self.direccion = direccion
        self.lista_administrador = lista_administrador #recibe una lista de nombre de administradores 
        self.num_guardias = num_guardias
        self.lista_guardias = []
        self.num_unidades_habitacionales = num_unidades_habitacionales
        self.lista_unidades = lista_unidades
        self.cuenta_corriente = cuenta_corriente
        self.resgistro_gasto_comun = {} #diccionario { "mes": monto de gasto comun}
        self.lista_residente = []
        self.lista_personal_mantenimiento = lista_personal_mantenimiento
        #self.id = uuid.uuid4() 
        self.id = id_condominio
        
    def get_direccion(self):
        # retorna direccion
        pass
    
    def set_direccion(self):
        # cambia la direccion por una nueva
        pass
    
    def set_administrador(self):
        # cambia un administrador por uno nuevo de la lista_administrador
        pass
    
    def get_administrador(self):
        # retorna lista de administradores
        pass
    
    def del_guardia(self):
        #borra el guardia de la lista_guardia
        pass

    def get_guardias(self):
        # retorna lista de los guardias agregados
        pass
    
    def get_unidades(self):
        # retorna la lista de las unidades habitacionales
        pass
    
    def agregar_residente(self):
        #agregar residente a lista_residente
        pass
    
    def agregar_personal_mantenimiento(self):
        #agregar personal a lista_personal mantenimiento
        pass
    
    def calcular_gasto_comun(self):
        #calcular gasto comun del condominio
        pass
    
    def imprimir_gasto_comun(self):
        #imprime informacion de gasto comun
        #por mes / todo
        pass

    def agregar_guardia(self):
        #agregar guardia a lista_guardia
        #considerar numero de guardia predefinido >> num_guardia <<
        pass


#Creación de clases Guardia, UnidadHabitacional, CuentaCorriente con 3 atributos y 4 métodos.
class Guardia:
    def __init__(self, nombre, apellido, rut, nombre_condominio):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut
        self.nombre_condominio = nombre_condominio
        
    def comenzar_turno(self):
        # return hora de comienzo de trabajo
        pass
    
    def terminar_turno(self):
        # return hora de finalizacion de turno y duracion de jornada
        pass
    
    def ronda_vigilancia(self):
        # recorrer condominio
        pass
    
    def registrar_visita(self):
        # registra visitas entrantes y salientes ( unidad habitacional de destino/origen )
        pass
    

# casa1 = UnidadHabitacional( 1A, 120, ["pepa", "popi", "pancha"], 4)

class UnidadHabitacional:
    
    def __init__(self, numero_identificador, metros_cuadrados, lista_habitantes, num_vehiculos):

        self.numero_identificador = numero_identificador
        self.metros_cuadrados = metros_cuadrados
        self.lista_habitantes = lista_habitantes
        self.num_vehiculos = num_vehiculos # ***** podria estar en condominio el numero total de estacionamientos
        
    
    def agregar_habitante(self):
        #agrega un habitante nuevo a lista_habitante
        pass
    
    def agregar_vehiculo(self):
        #agregar un vehiculo a lista de vehiculos
        pass
    
    def gasto_comun_habitacional(self, gasto_comun_total, num_unidades_habitacionales):
        # calcula el gasto particular de mi unidad habitacional segun mis metros cuadrados
        # retonar gasto correspondiente.
        pass
    
    def get_lista_habitantes(self):
        # retirnar lista de habitantes de esta unidad habitacional
        pass
    



class CuentaCorriente:

    def __init__(self, banco, numero_cuenta, nombre_condominio):
        self.banco = banco
        self.numero_cuenta = numero_cuenta
        self.nombre_condominio = nombre_condominio
        self.saldo = 0

    def pagar(self):
        # 
        pass
    
    def metodo2(self):
        pass
    
    def metodo3(self):
        pass
    
    def metodo4(self):
        pass

