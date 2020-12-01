class UnidadHabitacional:
    
    def __init__(self, numero_identificador):

        self.numero_identificador = numero_identificador
        self.metros_cuadrados = 100
        self.lista_habitantes = []
        self.num_vehiculos = 0 # ***** podria estar en condominio el numero total de estacionamientos
        
    
    def agregar_habitante(self, nombre, apellido, rut):
        #agrega un habitante nuevo a lista_habitante
        self.lista_habitantes.append(tuple(nombre +" "+ apellido, rut))
    
    def agregar_vehiculo(self):
        #agregar un vehiculo a lista de vehiculos
        pass
    
    def get_lista_habitantes(self):
        # retirnar lista de habitantes de esta unidad habitacional
        pass
    
