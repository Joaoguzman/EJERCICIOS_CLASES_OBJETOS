class UnidadHabitacional:
    
    def __init__(self, numero_identificador, metros_cuadrados, lista_habitantes, num_vehiculos):

        self.numero_identificador = numero_identificador
        self.metros_cuadrados = metros_cuadrados
        self.lista_habitantes = []
        self.num_vehiculos = num_vehiculos # ***** podria estar en condominio el numero total de estacionamientos
        
    
    def agregar_habitante(self, nombre, apellido, rut):
        #agrega un habitante nuevo a lista_habitante
        self.lista_habitantes.append(tuple(nombre, apellido, rut))
    
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
    
