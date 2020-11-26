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
        self.inicio_jornada = []
        self.fin_jornada = []
        self.registro = {}
        self.registro_visita = []
        
    def comenzar_turno(self):
        # return hora de comienzo de trabajo
        from datetime import datetime
        hoy = datetime.now()
        fecha = str(hoy.day)+"/"+str(hoy.month) +"/"+str(hoy.year)
        hora = str(hoy.hour)+":"+ str(hoy.minute) +":"+ str(hoy.second)
        self.inicio_jornada.append(fecha + " | " +hora)
        list = [hora]
        self.registro[fecha] = list
    
    def terminar_turno(self):
        # return hora de finalizacion de turno y duracion de jornada
        from datetime import datetime
        hoy = datetime.now()
        fecha = str(hoy.day)+"/"+str(hoy.month) +"/"+str(hoy.year)
        hora = str(hoy.hour)+":"+ str(hoy.minute) +":"+ str(hoy.second)
        self.fin_jornada.append(fecha + " | " +hora)
        self.registro[fecha].append(hora)
    
    def ver_registro(self, entrada=False, salida=False):
        # recorrer condominio
        if salida and entrada:
            print("mostrando entra y salida")
            for indice,dia in enumerate(self.registro.items()):
                print(indice," ",dia)
        elif entrada:
            for entrada in self.inicio_jornada:
                print(entrada)
        elif salida:
            print("Mostrando salida")
            for entrada in self.fin_jornada:
                print(entrada)
        else:
            print("debe elegir una entrada")
    
    def registrar_visita(self, nombre_visita, patente):
        # registra visitas entrantes y salientes ( unidad habitacional de destino/origen )
        registro_dia =  nombre_visita + " - " + patente
        self.registro_visita.append(registro_dia)
    

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


condominio1 = Condominio("calle 3", ["a", "b" , "c"], 7, 5, ["a", "b"], ["a", "b"], ["1", "2", "3"], 999)
guardia1 = Guardia("joao", "guzman", "19124333-1", "las brisas")
guardia2 = Guardia("joao", "guzman", "19124333-3", "las brisas")

condominio1.agregar_guardia(guardia1)
condominio1.agregar_guardia(guardia2)
condominio1.del_guardia("19124333-1")
print(condominio1.lista_guardias)
for guardia in condominio1.lista_guardias:
    print(guardia.rut)



















guardia1.comenzar_turno()
guardia1.terminar_turno()

guardia1.ver_registro(entrada=True, salida=True)