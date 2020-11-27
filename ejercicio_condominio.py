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
       # self.cuenta_corriente = cuenta_corriente
        self.registro_gasto_comun = {} #diccionario { "mes": monto de gasto comun}
        self.lista_residente = []
        self.lista_personal_mantenimiento = lista_personal_mantenimiento
        #self.id = uuid.uuid4() 
        self.id = id_condominio
        
    def get_direccion(self):
        # retorna direccion
        return self.direccion

    def set_direccion(self, direccion_nueva):
        # cambia la direccion por una nueva
        self.direccion = direccion_nueva
    
    def set_administrador(self, administrador_extraer, administrador_incluir):
        # cambia un administrador por uno nuevo de la lista_administrador
        self.lista_administrador.remove(administrador_extraer)
        self.lista_administrador.append(administrador_incluir)
    
    def get_administrador(self):
        # retorna lista de administradores
        return self.lista_administrador
    
    def agregar_guardia(self, nuevo_guardia):
        #agregar guardia a lista_guardia
        #considerar numero de guardia predefinido >> num_guardia <<
        self.lista_guardias.append(nuevo_guardia)
        pass
    
    def del_guardia(self, rut_guardia):
        #borra el guardia de la lista_guardia
        for guardia in self.lista_guardias:
            print(guardia)
            if rut_guardia == guardia.rut:
                self.lista_guardias.remove(guardia)
            else:
                print("Guardia no está en la lista")

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


class Terreno:

    def __init__(self, direccion, superficie_m2, tipo_superficie, potencial_terreno,
                valor, rol):
        self.direccion = direccion
        self.__superficie_m2 = superficie_m2
        self.__tipo_superficie = tipo_superficie
        self.__potencial_terreno = potencial_terreno
        self.__valor = valor
        self.__rol = rol

    def get_rol(self):
        return self.__rol

    def get_tipo_superficie(self):
        return self.__tipo_superficie
    
    def get_superficie_m2(self):
        return self.__superficie_m2

    def get_valor(self):
        return self.__valor
    
    def get_potencial_terreno(self):
        return self.__potencial_terreno

    def set_potencial_terreno(self, nuevo_potencial):
        self.__potencial_terreno = nuevo_potencial

condominio1 = Condominio("calle 3", ["a", "b" , "c"], 7, 5, ["a", "b"],
                        ["a", "b"], ["1", "2", "3"], 999)
guardia1 = Guardia("joao", "guzman", "19124333-1", "las brisas")
guardia2 = Guardia("joao", "guzman", "19124333-3", "las brisas")

condominio1.agregar_guardia(guardia1)
condominio1.agregar_guardia(guardia2)
condominio1.del_guardia("19124333-1")
print(condominio1.lista_guardias)
for guardia in condominio1.lista_guardias:
    print(guardia.rut)



terreno1 = Terreno("Av. mar #14656", 10000, "Regado R1", "Habitacional", 10000000, "573-26")

print(terreno1.get_rol())
print(terreno1.get_potencial_terreno())
terreno1.set_potencial_terreno("Agricola")
print(terreno1.get_potencial_terreno())

